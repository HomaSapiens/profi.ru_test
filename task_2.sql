select department, count(*) as "number of devs"
from employees
where position = 'Software Developer'
group by department having (count(*) < 5)
order by department;
