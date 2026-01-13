1)--Recyclable and Low Fat Products
select product_id from products where low_fats='Y' and recyclable ='Y'

#################################################

2)--Find Customer Referee
SELECT name FROM customer WHERE referee_id <> 2 OR referee_id IS NULL;

--Solution 2
SELECT name
FROM Customer
WHERE --nvl(referee_id,0)!=2 is used in oracle
COALESCE(referee_id,0) <> 2;--converts null to 0

#################################################

3)--Big Countries
select name , population, area from world where area >= 3000000 or population >= 25000000

#################################################

4)--Article Views I
select distinct(author_id) as id from views where author_id=viewer_id order by 1;

#################################################

5)--Invalid tweet
select tweet_id from Tweets where length(content)>15; --char_length

#################################################

6)--Replace Employee ID With The Unique Identifier
select u.unique_id, e.name from Employees e left join EmployeeUNI u on u.id=e.id

#################################################

7)--Product Sales Analysis I
select p.product_name, s.year, s.price from
sales s , product p where s.product_id=p.product_id;

#################################################

8)--Customer Who Visited but Did Not Make Any Transactions
select v.customer_id,count(v.visit_id) as count_no_trans
from visits v left join transactions t on v.visit_id = t.visit_id where transaction_id IS NULL
group by customer_id
--Solution 2
SELECT customer_id, COUNT(visit_id) as count_no_trans 
FROM Visits
WHERE visit_id NOT IN (
	SELECT visit_id FROM Transactions
	)
GROUP BY customer_id

#################################################

9)--Rising Temprature
select w1.id from weather w1 join weather w2 on (DATEDIFF(w1.recordDate,w2.recordDate) = 1) where w1.temperature > w2.temperature;

--With laG
SELECT id
FROM (
    SELECT
        id,
        recordDate,
        temperature,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
        LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM weather
) t
WHERE
    DATEDIFF(recordDate, prev_date) = 1
    AND temperature > prev_temp;

--If dates are guaranteed to be consecutive
SELECT id
FROM (
    SELECT
        id,
        temperature,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp
    FROM weather
) t
WHERE temperature > prev_temp;

#################################################

10)-- Average Time of Process per Machine
select a.machine_id,
round(avg(b.timestamp-a.timestamp),3) as processing_time
from activity a, activity b where 
a.machine_id=b.machine_id and
a.process_id=b.process_id and
a.activity_type='start' and 
b.activity_type='end'
group by a.machine_id;

SELECT 
    machine_id,
    ROUND(SUM(CASE WHEN activity_type='start' THEN timestamp*-1 ELSE timestamp END)*1.0
    / (SELECT COUNT(DISTINCT process_id)),3) AS processing_time
FROM 
    Activity
GROUP BY machine_id

WITH ProcessTimes AS (
    SELECT 
        a.machine_id,
        a.process_id,
        MAX(CASE WHEN a.activity_type = 'start' THEN a.timestamp END) AS start_time,
        MAX(CASE WHEN a.activity_type = 'end' THEN a.timestamp END) AS end_time
    FROM 
        Activity a
    GROUP BY 
        a.machine_id,
        a.process_id
),
Durations AS (
    SELECT 
        machine_id,
        (end_time - start_time) AS duration
    FROM 
        ProcessTimes
)
SELECT 
    machine_id,
    ROUND(AVG(duration), 3) AS processing_time
FROM 
    Durations
GROUP BY 
    machine_id;

#################################################

11) --emp bonus<100
select a.name, b.bonus from employee a left join bonus b  on a.empid=b.empid where coalesce(b.bonus,0)<1000

#################################################

12)--Students and Examination
select s1.student_id, s1.student_name, s.subject_name,count(e.subject_name) as attended_exams
from students s1 join  subjects s left join examinations e on s1.student_id=e.student_id and
 s.subject_name=e.subject_name
group by s1.student_id, s.subject_name order by s1.student_id, s.subject_name;

#################################################

13)--Managers with at Least 5 Direct Reports
select a.name from 
employee a join employee b 
on a.id=b.managerid
group by b.managerid
having count(*)>=5;

#################################################

14)--Confirmation Rate
select f.user_id,cast(COALESCE(sum(f.case_action)/count(f.action),0)as decimal(10,2)) as confirmation_rate from
(
select s.user_id, c.action,case when c.action='timeout' then 0
                                when c.action='confirmed' then 1
                                else null
                            END as case_action
from signups s left join Confirmations c on s.user_id=c.user_id
) as f
group by f.user_id;
--Solution 2
select s.user_id,ROUND(COALESCE(SUM(IF(c.action = 'confirmed', 1, 0)) / COUNT(c.user_id),0), 2) AS confirmation_rate
from signups s left join Confirmations c on s.user_id=c.user_id
group by c.user_id;

#################################################

15)--Not Boring Movies
select * from cinema where id%2=1 and description<>"boring"
order by rating desc;

#################################################

16)--Average Selling Price
select p.product_id,ifnull(round((sum(u.units*p.price)/sum(u.units)),2),0)average_price 
from prices p left join unitssold u on 
p.product_id=u.product_id and u.purchase_date between p.start_date and p.end_date
group by product_id;

#################################################

17)--Project Employees I
select p.project_id, round(avg(e.experience_years),2) average_years
from project p left join employee e on e.employee_id = p.employee_id
group by project_id;

#################################################

18)--Percentage of Users Attended a Contest
select contest_id,round(((count(r.user_id)/(select count(u.user_id) from users u))*100),2) percentage  
from register r 
group by contest_id
order by 2 desc,1;

#################################################

19)--Queries Quality and Percentage
select query_name , 
round((sum(rating/position)/count(query_name)),2)quality ,
round(((sum((case when rating < 3 then 1 else 0 END))/count(query_name))*100),2) poor_query_percentage
from queries where query_name is not null
group by query_name;

#################################################

20)--Monthly Transactions I
select DATE_FORMAT(trans_date, '%Y-%m') as month,
country, 
count(DATE_FORMAT(trans_date, '%Y-%m')) as trans_count,
sum(case when state='approved' then 1 else 0 end) as approved_count,
sum(amount) as trans_total_amount,
sum(case when state='approved' then amount else 0 end) as approved_total_amount
from transactions
group by month , country;

#################################################

21)--Immediate Food Delivery II
with customer as
(
    select *,
    row_number() over (partition by customer_id order by customer_id, order_date) as customer_number from delivery
)
select
round((sum(case when order_date=customer_pref_delivery_date then 1 else 0 end )/count(*))*100,2) as immediate_percentage
from customer where customer_number=1;

#################################################

22)--Game Play Analysis IV
SELECT ROUND(COUNT(t2.player_id)/COUNT(t1.player_id),2) AS fraction
FROM
(SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id) t1 LEFT JOIN Activity t2
ON t1.player_id = t2.player_id AND DATEDIFF(t2.event_date , t1.first_login)=1 

#################################################

23)--Number of unique subjects taught by each teacher
select distinct(teacher_id), count(distinct(subject_id)) as cnt from teacher 
group by teacher_id;

#################################################

24)--User Activity for the Past 30 Days I
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE (activity_date > "2019-06-27" AND activity_date <= "2019-07-27")
GROUP BY activity_date;

#################################################

25)--Product Sales Analysis III
with Customer as
(
    select * , rank() over (partition by product_id order by product_id,year) as year_number
    from sales
) 
select customer.product_id,customer.year as first_year,customer.quantity,customer.price
from customer  where customer.year_number=1

#################################################

26)--Classes more then 5 students
select class from
courses 
group by class
having count(student)>=5;

#################################################

27)--Find Followers Count
select user_id , count(user_id) as followers_count from followers
group by user_id 
order by 1 asc;

#################################################

28)--Biggest Single Number
select max(MN.num) as num from (select *,count(num) from mynumbers
group by num
having count(num)=1) as MN;

#################################################

29)--Customer Who Bought all Products
SELECT  customer_id FROM Customer GROUP BY customer_id
HAVING COUNT(distinct product_key) = (SELECT COUNT(product_key) FROM Product)

--Solution 2
SET @PROCOUNT := (SELECT COUNT(DISTINCT product_key) FROM Product);
SELECT DISTINCT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = @PROCOUNT;

#################################################

30)--The Number of Employees Which Report to Each Employee
select e1.employee_id, e1.name, count(e2.reports_to) as reports_count , round(avg(e2.age),0) as average_age
from employees e1 join employees e2 on  e1.employee_id=e2.reports_to
group by e1.employee_id,e1.name
order by e1.employee_id;

#################################################

31)--Primary department of each employee
select distinct(employee_id),department_id from employee 
where employee_id in (select employee_id from employee 
group by employee_id having count(*)=1 ) or primary_flag='Y';

#################################################

32)--Triangle Judgement
select x,y,z, (case when (x+y)>z and (y+z)>x and (x+z)>y then 'Yes' else 'No' END) as triangle from triangle;

#################################################

33)--Consecutive Numbers
select distinct(num_1) as ConsecutiveNums
from (Select num as num_1,
lead(num,1) over () as num_2,
lead(num,2) over () as num_3
from logs
order by id
) as A
where num_1=num_2 and
num_2=num_3;

#################################################

34)--Product Price at a Given Date
select distinct product_id, 10 as price from Products where product_id not in(select distinct product_id from Products where change_date <='2019-08-16' )
union 
select product_id, new_price as price from Products where (product_id,change_date) in (select product_id , max(change_date) as date from Products where change_date <='2019-08-16' group by product_id)

#################################################

35)--Last Person to Fit in the Bus
with bus as 
(
select q1.*, sum(q2.weight)  as last from queue q1 inner join queue q2 
on q1.turn>=q2.turn
group by q1.turn
order by q1.turn
)
select person_name from bus where last<=1000 
order by last desc limit 1;

--Solution 2
SELECT PERSON_NAME FROM (
SELECT PERSON_ID, PERSON_NAME, 
SUM(weight) OVER (ORDER BY TURN) AS RT FROM QUEUE) T1 WHERE RT<=1000 
ORDER BY RT DESC LIMIT 1;

#################################################

36)--Count salary catagory
select 
"Low Salary" as category,
(select count(*) from accounts where income<20000) as accounts_count
union all
select 
"Average Salary" as category,
(select count(*) from accounts where income between 20000 and 50000) as accounts_count
union all
select 
"High Salary" as category,
(select count(*) from accounts where income>50000) as accounts_count

#################################################

37)--Employees whos manager left the company
select e1.employee_id from employees e1 
where e1.salary< 30000 and e1.manager_id not in (select employee_id from employees) order by 1;

#################################################

38)--Exchange seats
select
    --last ID
 case when id =(select max(id) from seat) and id %2=1
      then id 
     --odd ID
      when id %2=1 
      then id+1
      --even ID
      else id-1 END as id,
    student from seat
    order by id;

#################################################

39)--Movie rating
with ratings as 
(
    select mr.*,m.title ,u.name from movierating mr left join users u on mr.user_id=u.user_id
    left join movies m on mr.movie_id=m.movie_id

) 
(select name as results 
from ratings
group by name
order by count(*) desc,name
limit 1)

Union all

(select title from ratings 
where date_format(created_at,"%Y-%m")='2020-02'
group by title
order by avg(rating) desc,title
limit 1)
;

#################################################

40)--Restaurant Growth
SELECT 
    visits.visited_on AS visited_on,
    SUM(c.amount) AS amount, 
    ROUND(SUM(c.amount) / 7.0, 2) AS average_amount
FROM (
    SELECT DISTINCT visited_on 
    FROM Customer
    WHERE DATEDIFF(
        visited_on, 
        (SELECT MIN(visited_on) FROM Customer)
    ) >= 6
) visits 
LEFT JOIN Customer c 
ON DATEDIFF(visits.visited_on, c.visited_on) BETWEEN 0 and 6
GROUP BY visits.visited_on;

#################################################

41)--Friend Requests II: Who Has the Most Friends
select  id, count(*) as num
from
(select requester_id as id from RequestAccepted
union all
select accepter_id from RequestAccepted) as requests
group by id
order by num desc
limit 1;

#Solution 2

select 
    requester_id as id,
    (   select count(t.requester_id) 
        from RequestAccepted t
        where t.requester_id = id or t.accepter_id = id
    ) as num
from RequestAccepted
group by id
order by num desc
limit 1;

#################################################

42)--Investments in 2016
select round(sum(tiv_2016),2) as tiv_2016
from insurance
where tiv_2015 in (
    select tiv_2015
    from insurance
    group by tiv_2015
    having count(*)>1

) and (lat,lon) in (select lat, lon
    from insurance
    group by lat, lon
    having count(*)<=1)

#################################################

43)--Department top 3 salaries
with Sal as
(
  select *, dense_rank() over ( partition by departmentId order by salary desc) as row_num from employee

)
select d.name as department,
e.name as employee,e.salary as salary
from 
sal e left join department d on e.departmentId=d.id 
where row_num<=3;

#################################################

44)--Fix name in a table
select user_id, concat(upper(left(name,1)),lower(substring(name,2,length(name)))) as name from users order by 1;

#################################################

45)--Patients With a Condition
SELECT *
FROM Patients
WHERE conditions LIKE '% DIAB1%' OR 
      conditions LIKE 'DIAB1%'
--Solution 2
select * from Patients where conditions regexp '\\bDIAB1';

#################################################

46)--delete duplicate email_ids	
delete p1 from person p1 , person p2 where p1.email=p2.email and p1.id>p2.id;
 #################################################

47)--2nd highest salary

select max(salary) as "SecondHighestSalary" from Employee 
where salary<
(select max(salary) from Employee);
--Solution 2
select salary as SecondHighestSalary from employee group by salary order by salary desc limit 1,1;  
--Soluion 3
with T as
( select * ,dense_rank() over (order by salary desc) as row_id from employee )select salary as SecondHighestSalary from T where row_id=2;

#################################################

48)--Group sold product by date
select sell_date,count(distinct product) as num_sold, 
GROUP_CONCAT(distinct product order by product asc SEPARATOR ',')products from Activities
group by sell_date
;

#################################################

49)--List of products ordered in a month
select product_name, sum(unit) as unit from 
 orders o join products p on p.product_id=o.product_id where
date_format(o.order_date,"%Y-%m")='2020-02' 
group by 1 having unit>=100

#################################################

50)--Find valid email id
select * 
from Users 
where mail regexp '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'

#################################################
1070. Product Sales Analysis III
with first_year_sales as (
    select
        product_id,
        min(year) first_year
    from sales
    group by product_id
)

select  s.product_id,
        f.first_year,
        s.quantity,
        s.price
from first_year_sales f join sales s
on f.product_id = s.product_id
and s.year = f.first_year

--or 
with year_ranks as (
select product_id , 
year as first_year ,
quantity,
price,
dense_rank() over (partition by product_id order by year) as year_rank
from sales
)

select 
product_id , 
first_year ,
quantity,
price
from year_ranks where year_rank = 1

##########################################
	550. Game Play Analysis IV
WITH first_login AS (
  SELECT player_id, MIN(event_date) AS first_date
  FROM Activity
  GROUP BY player_id
)
SELECT ROUND(
  COUNT(DISTINCT a.player_id) / (SELECT COUNT(*) FROM first_login),
  2
) AS fraction
FROM first_login f
JOIN Activity a
  ON a.player_id = f.player_id
 AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY);

WITH first_login AS (
  SELECT player_id, MIN(event_date) AS first_date
  FROM Activity
  GROUP BY player_id
)
SELECT ROUND(
  COUNT(DISTINCT a.player_id) / (SELECT COUNT(*) FROM first_login),
  2
) AS fraction
FROM first_login f
JOIN Activity a
  ON a.player_id = f.player_id
 AND DATEDIFF(a.event_date, f.first_date) = 1;
################################################


