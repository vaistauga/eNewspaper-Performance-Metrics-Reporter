SELECT  
        log.time::date AS day,
        sum(CASE WHEN log.status = '200 OK' THEN 0 ELSE 1 END) AS Errors,
        count(*) AS requests,
        log.status,
        totalRequests
    FROM    log 
            JOIN 
                (SELECT count(status) AS totalRequests,
                --sum(CASE WHEN log.status = '200 OK' THEN 0 ELSE 1 END) AS Errors,
                log.time::date as dayx
                FROM log
                GROUP BY dayx) as x 
            ON x.dayx = log.time::date 
    GROUP BY status, day, totalRequests
--ORDER BY NumberOfErrors DESC