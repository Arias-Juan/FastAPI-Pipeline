/*
Number of employees hired for each job and department in 2021 divided by quarter. The
table must be ordered alphabetically by department and job.
*/


select 
 	d.department
	,j.job
	,count(he.id) filter (where date_part('quarter',to_timestamp(he.datetime,'YYYY-MM-DD')) = 1) as Q1
	,count(he.id) filter (where date_part('quarter',to_timestamp(he.datetime,'YYYY-MM-DD')) = 2) as Q2
	,count(he.id) filter (where date_part('quarter',to_timestamp(he.datetime,'YYYY-MM-DD')) = 3) as Q3
	,count(he.id) filter (where date_part('quarter',to_timestamp(he.datetime,'YYYY-MM-DD')) = 4) as Q4
from hired_employees he
left join departments d on he.department_id  = d.id
left join jobs j on he.job_id = j.id
where 1=1
and datetime != 'NaN'
and date_part('year',to_timestamp(he.datetime,'YYYY-MM-DD')) = 2021
group by department, job
order by department, job
