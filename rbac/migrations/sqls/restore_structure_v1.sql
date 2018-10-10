create or replace function rbac_restore_structure() returns void
language plpgsql
as $$
declare
	upload_cursor cursor for select * from rbac_permissionupload;
	group_id integer;
	action_id integer;
begin
	-- temporary table for containing added/updated group ids. On the end all groups that doesn't present in table will be deleted.
	drop table if exists updated_groups;
	create temp table updated_groups(id integer);

	-- temporary table for containing added/updated permission ids. At the end all permissions that doesn't present in table will be deleted.
	drop table if exists updated_permissions;
	create temp table updated_permissions(id integer);

	-- parse data
	for record_row in upload_cursor loop
		-- insert permission
		insert into rbac_action(name, codename, created_at, modified_at) values(record_row.name, record_row.codename, now(), now())
		on conflict (codename) do update set name=record_row.name, modified_at = now() where rbac_action.codename = record_row.codename;
		-- update temporary table, puts id of created/updated permission
		insert into updated_permissions(id) select id from rbac_action where rbac_action.codename = record_row.codename;
		-- take care of permission group
		if record_row.group is not null then
		 	if not exists(select id from auth_group where name = record_row.group limit 1) then
				insert into auth_group(name) values(record_row.group);
			end if;
			select id into group_id from auth_group where name = record_row.group;
			select id into action_id from rbac_action where rbac_action.codename = record_row.codename;
			-- connect the permission with the group
			insert into rbac_actiontogroup(action_id, group_id, created_at, modified_at) values(action_id, group_id, now(), now()) on conflict do nothing;
			-- update the temporary table, puts id of created/updated group
			insert into updated_groups(id) values(group_id);
		end if;
	end loop;
	-- remove unused items, permissions and groups rows
	-- collecting data of a groups that should be deleted
	drop table if exists groups_to_delete;
	create temp table groups_to_delete(id integer);
	insert into groups_to_delete(id)
		select g.id	from (select ug.id from (select auth_group.id
					from auth_group
						left join updated_groups on updated_groups.id = auth_group.id
					where updated_groups.id is null) ug
				left join auth_group_permissions on auth_group_permissions.group_id = ug.id
			where auth_group_permissions.group_id is null) g;
	-- collecting data of a actions that should be deleted
	drop table if exists actions_to_delete;
	create temp table actions_to_delete(id integer);
	insert into actions_to_delete(id)
		select rbac_action.id
			from rbac_action
				left join updated_permissions on rbac_action.id = updated_permissions.id
			where updated_permissions.id is null;
	-- remove a connection data between action and group
	delete from rbac_actiontogroup
		where rbac_actiontogroup.action_id in (select id from actions_to_delete);
	delete from rbac_actiontogroup
		where rbac_actiontogroup.group_id in (select id from groups_to_delete);
	-- remove group data
	delete from auth_group
		where auth_group.id in (select id from groups_to_delete);
	-- remove actions data
	delete from rbac_action
	where rbac_action.id in (select id from actions_to_delete);
	-- cleans all unnessesary stuctures
	drop table if exists updated_permissions, updated_groups, groups_to_delete, actions_to_delete;
end;
$$;