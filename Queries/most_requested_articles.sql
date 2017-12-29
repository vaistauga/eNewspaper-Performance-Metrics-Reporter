-- Query used to get the three most requested viwed articles from the website
select count(article_id) AS views, articles.title, article_id
    FROM article_to_log JOIN articles ON (id = article_id)
    GROUP BY article_id, articles.title
    ORDER BY views DESC
    LIMIT 3