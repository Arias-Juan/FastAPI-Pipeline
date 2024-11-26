/*
List of ids, name and number of employees hired of each department that hired more
employees than the mean of employees hired in 2021 for all the departments, ordered
by the number of employees hired (descending).
*/

with aux_mean_2021 as(
select avg(hired) as mean from (
select 
	 d.id
	,count(distinct he.id) as hired
from departments d
left join hired_employees he on d.id = he.department_id
where datetime != 'NaN'
and date_part('year',to_timestamp(he.datetime,'YYYY-MM-DD')) = 2021
group by 1) as aux)

select 
	 d.id
	,d.department
	,count(distinct he.id) as hired
from departments d
left join hired_employees he on d.id = he.department_id
group by 1, 2
having count(distinct he.id) >= (select mean from aux_mean_2021)
order by hired desc