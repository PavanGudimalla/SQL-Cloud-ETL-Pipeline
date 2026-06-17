create schema final_project2;
use final_project2;

select * from traffic;
select * from weather;

# a. Agencies issuing tickets each month
SELECT ISSUING_AGENCY_NAME, YEAR(ISSUE_DATE) AS yr, MONTH(ISSUE_DATE) AS mn, COUNT(*) AS ticket_count
FROM traffic
GROUP BY ISSUING_AGENCY_NAME, yr, mn
ORDER BY yr, mn, ISSUING_AGENCY_NAME;

# b. How many tickets have been issued by agencies since October 1, 2024?
SELECT ISSUING_AGENCY_NAME, COUNT(*) AS tickets_issued
FROM traffic
WHERE ISSUE_DATE >= '2024-10-01'
GROUP BY ISSUING_AGENCY_NAME
ORDER BY tickets_issued DESC;

# c. What is the average number of tickets issued by day of the week (i.e. Monday, Tuesday, etc.)?
SELECT DAYNAME(ISSUE_DATE) AS weekday, COUNT(*) / COUNT(DISTINCT DATE(ISSUE_DATE)) AS avg_tickets
FROM traffic
GROUP BY DAYNAME(ISSUE_DATE);

# d. How many tickets were issued during periods of rain?
SELECT COUNT(*) AS rain_tickets
FROM traffic t, weather w
WHERE DATE(t.ISSUE_DATE) = w.datetime
AND w.preciptype LIKE '%rain%';

# e. What was the total precipitation for each month?
SELECT YEAR(datetime)  AS yr,MONTH(datetime) AS mn, SUM(precip) AS total_precip
FROM weather
GROUP BY YEAR(datetime), MONTH(datetime)
ORDER BY YEAR(datetime), MONTH(datetime);

# f. What is the total fine issued each month for vehicles traveling more than 10 mph over the speed limit?
SELECT YEAR(ISSUE_DATE)  AS yr, MONTH(ISSUE_DATE) AS mn, SUM(FINE_AMOUNT)  AS total_fine
FROM traffic
WHERE VIOLATION_PROCESS_DESC LIKE '%SPEED%'
AND VIOLATION_PROCESS_DESC NOT LIKE '%1-10 MPH%'
GROUP BY YEAR(ISSUE_DATE), MONTH(ISSUE_DATE)
ORDER BY YEAR(ISSUE_DATE), MONTH(ISSUE_DATE);

# g. What is the average number of tickets written for each hour of a standard day (i.e. from 7:00-8:00am, 8:00-9:00am, etc.)?
SELECT ISSUE_TIME AS hour_of_day, COUNT(*)   AS ticket_count
FROM traffic
GROUP BY ISSUE_TIME
ORDER BY ISSUE_TIME;

# h. Compare tickets associated with accidents on rainy days vs non-rainy days.
# Accidents on rainy days
SELECT 'Rainy' AS rain_status,COUNT(*) AS accident_tickets
FROM traffic t, weather w
WHERE DATE(t.ISSUE_DATE) = w.datetime
AND w.preciptype LIKE '%rain%'
AND t.ACCIDENT_INDICATOR = 'Y';

# Accidents on non rainy days
SELECT 'Non-Rainy' AS rain_status, COUNT(*) AS accident_tickets
FROM traffic t,weather w
WHERE DATE(t.ISSUE_DATE) = w.datetime
AND w.preciptype NOT LIKE '%rain%'
AND t.ACCIDENT_INDICATOR = 'Y';






