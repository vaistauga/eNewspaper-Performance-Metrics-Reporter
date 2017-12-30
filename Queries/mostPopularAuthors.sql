SELECT authors.name, count(authors.name)
    FROM 
        (articles JOIN article_to_log ON id = article_to_log.article_id)
        JOIN authors
        ON author = authors.id    
    GROUP BY authors.name