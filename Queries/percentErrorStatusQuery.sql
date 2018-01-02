SELECT 
    day,
    (errors::decimal /requests::decimal)*100 AS percent_of_errors
FROM(
    SELECT 
        log.time::date AS day,
        Sum(CASE WHEN log.status ='200 OK' THEN 0 ELSE 1 END) AS errors,
        count(log) AS requests
    FROM log 
    GROUP BY day
    )logStatusByDay
WHERE (errors::decimal / requests::decimal * 100) > 1