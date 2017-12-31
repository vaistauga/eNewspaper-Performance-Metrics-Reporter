
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
    for i in result:
        print("{0} -- {1}".format(i[0], i[1]))
        

def most_read_authors():
    #The SQL query which return the data
    query = '''
    SELECT authors.name, count(authors.name)
    FROM 
        (articles JOIN article_to_log ON id = article_to_log.article_id)
        JOIN authors
        ON author = authors.id    
    GROUP BY authors.name
    '''

    #Execute the query
    connection = psycopg2.connect(database=DBNAME)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    
    ## format and print results       
    for i in result:
        print("{0} -- {1}".format(i[1], i[0]))

def request_errors_by_day():
    #The SQL query which return the data
    query = '''
    SELECT  status, 
        count(status) AS NumberOfErrors,
        --date_trunc('day', time) AS day
        log.time::date AS day
    FROM log
    WHERE status != '200 OK'
    GROUP BY status, day
    ORDER BY NumberOfErrors DESC
    '''

    #Execute the query
    connection = psycopg2.connect(database=DBNAME)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    
    ## format and print results       
    for i in result:
        print('Error count: {0} -- day: {1}'.format(i[1], i[2]))