SELECT  status, 
        count(status) AS NumberOfErrors,
        --date_trunc('day', time) AS day
        log.time::date AS day
    FROM log
    WHERE status != '200 OK'
    GROUP BY status, day
    ORDER BY NumberOfErrors DESC