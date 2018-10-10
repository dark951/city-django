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
end;
$$;