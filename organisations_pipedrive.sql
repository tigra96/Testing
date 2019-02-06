CREATE OR REPLACE VIEW tableau.pipedrive_organisations_showcase AS (
WITH companies as (
    select pipedrive_id,
           min(date_res)::date as org_add_date,
           count(distinct corp_students.student_id) as org_all_time_students,
           count(distinct class.id) as org_total_students,
           count(distinct case when pay_num = 1 then corp_students.student_id else null end) as org_attracted_students,
           count(distinct case when pay_num = 1 then class.id else null end) as org_attracted_students_classes,
           count(distinct student_company_history.student_id) as org_current_students,
           count(distinct case when student_company_history.student_id is not null then class.id else null end) as org_current_students_classes,
           count(distinct case when class.type = 'trial' then corp_students.student_id else null end) as org_trial_students
    from corp_stat.corp_students
    join skyeng_stat.student_company
      on student_company.id = corp_students.company_id
    left join skyeng_stat.class 
      on class.student_id = corp_students.student_id
      and class.removed_at is null
      and class.teacher_id not in (select * from test_users)
      and class.student_id not in (select * from test_users)
    inner join skyeng_stat.class_status 
      on class.id = class_status.class_id
      and class_status.status in ('success', 'failed_by_student', 'canceled_not_marked')
    left join public.student_company_history
        on student_company_history.student_id = corp_students.student_id
        and GETDATE() - 1 between start_date and end_date
    group by pipedrive_id

)


SELECT organisations.active_flag,
       organisations.add_time,
       organisations.lost_deals_count::int + 
            organisations.won_deals_count::int + 
                organisations.open_deals_count::int as deals_count,
       organisations.id,
       organisations.last_activity_date,
       organisations.last_activity_id,
       organisations.lost_deals_count,
       organisations.name,
       organisations.narrow_sector,
       organisations.open_deals_count,
       companies.org_add_date,
       companies.org_attracted_students,
       companies.org_current_students,
       companies.org_total_students,
       companies.org_trial_students,
       organisations.org_size,
       organisations.owner_id,
       owners.name as owner_name,
       organisations.phone,
       organisations.update_time,
       organisations.web_site,
       organisations.wide_sector,
       organisations.won_deals_count
FROM pipedrive.organisations
LEFT JOIN pipedrive.users owners ON organisations.owner_id = owners.id
LEFT JOIN companies ON organisations.id = companies.pipedrive_id 
) WITH NO SCHEMA BINDING;

SELECT *
FROM tableau.pipedrive_organisations_showcase
LIMIT 1000