
import psycopg2

DBNAME = "news"

def most_requested_articles():
    #The SQL query which return the data
    query = '''
        select count(article_id) AS views, articles.title, article_id
        FROM article_to_log JOIN articles ON (id = article_id)
        GROUP BY article_id, articles.title
        ORDER BY views DESC
        LIMIT 3
    '''

    #Execute the query
    connection = psycopg2.connect(database=DBNAME)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    
    ## return results
    return result

