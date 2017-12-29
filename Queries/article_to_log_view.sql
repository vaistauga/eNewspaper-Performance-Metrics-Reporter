
--This query was used to construct the article_to_log view
--The query only uses the logs which returned '200 OK' code. 
--This was done to remove the possibility of accidental match betweeen non-existant URL and article name
CREATE VIEW article_to_log AS
    SELECT 
        articles.id AS article_id,
        url_slug.slug_derived_from_URL,
        url_slug.log_id
        FROM 
            articles 
            LEFT JOIN
                (SELECT 
                    --Remove the leading text from URL leaving only the slug
                    split_part(path, '/article/',2) AS slug_derived_from_URL,
                    id AS log_id
                    FROM log
                    WHERE 
                        status='200 OK'
                    )url_slug
                    ON (slug = url_slug.slug_derived_from_URL
                    )