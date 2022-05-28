SELECT *
FROM dataset_1;

SELECT weather, temperature
FROM dataset_1;

SELECT DISTINCT weather 
FROM dataset_1;

SELECT *
FROM dataset_1 LIMIT 10;

SELECT DISTINCT passanger
FROM dataset_1;

SELECT DISTINCT time
FROM dataset_1;

SELECT *
FROM dataset_1
where destination = 'Home';

select *
from dataset_1
order by coupon;

select destination as 'Desti'
from dataset_1 limit 10;

select *-- this is comment using two desh --
from dataset_1;

select occupation
from dataset_1
group by occupation;

select weather,
AVG(temperature) AS 'Avg_temp'
from dataset_1
group by weather;

select weather,
count (temperature) as 'count_temp'
from dataset_1
group by weather;

select weather,
count(distinct temperature) as 'count_dist_temp'
from dataset_1
group by weather;

select weather,
sum(temperature) as 'sum_temp'
from dataset_1
group by weather;

select weather,
min(temperature) as 'mini_temp'
from dataset_1
group by weather;

select weather,
max(temperature) as 'max_temp'
from dataset_1
group by weather;

select occupation
from dataset_1
group by occupation
having occupation = 'Student';

select *
from dataset_1
union
select * from table_to_union;

select *
from dataset_1
union
select *
from table_to_union;

select distinct destination
from (select *
from dataset_1
union
select *
from table_to_union);

select destination, passanger
from (select *
from dataset_1
where passanger = 'Alone');

select *
from dataset_1
where weather like 'Sun%';

select distinct temperature
from dataset_1
where temperature between 29 and 75;

select occupation
from dataset_1
where occupation in ('Sales & Related', 'Management');

select 
        destination,
        weather,
        avg(temperature) over (partition by weather) as 'avg_temp_by_weather'
from dataset_1;

select 
        destination,
        weather,
        avg(temperature) over (partition by weather order by destination) as 'avg_temp_by_weather'
from dataset_1;

select 
       destination,
       weather,
       ROW_NUMBER () over (Partition by weather order by destination) as 'avg_temp_by_weather'
from dataset_1;

select 
       destination,
       weather,
       RANK () over (Partition by weather order by destination) as 'avg_temp_by_weather'
from dataset_1;

SELECT destination,
weather,
dense_rank () over (partition by weather order by destination) as 'avg_temp_by_weather'
from dataset_1;

select time, NTILE (50) over (order by time)
from dataset_1;

select destination, time, LAG(row_count,1, '99999') over (ORDER BY row_count) as 'LaggedCount'
from dataset_1;

select destination, time, LEAD(row_count, 1, '99999') over ( ORDER BY row_count) as 'LeadCount'
from dataset_1;