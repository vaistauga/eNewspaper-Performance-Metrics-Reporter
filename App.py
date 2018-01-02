'''This module is used to connect to and use PostgreSQL database '''
import psycopg2

DBNAME = "news"


def most_viewed_articles():
    ''' This method return the most articles sorted by the
    number of views they received'''

    # Query used to retreive the data
    query = '''
        select count(article_id) AS views, articles.title, article_id
        FROM article_to_log JOIN articles ON (id = article_id)
        GROUP BY article_id, articles.title
        ORDER BY views DESC
    '''

    # Execute the query
    connection = psycopg2.connect(database=DBNAME)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()

    # return results
    for i in result:
        print("{0} views --- '{1}'".format(i[0], i[1]))


def most_read_authors():
    '''This method returns list of outhors ordered by the
    ammount of views their articles received'''

    # The SQL query which return the data
    query = '''
    SELECT authors.name, count(authors.name)
    FROM
        (articles JOIN article_to_log ON id = article_to_log.article_id)
        JOIN authors
        ON author = authors.id
    GROUP BY authors.name
    '''

    # Execute the query
    connection = psycopg2.connect(database=DBNAME)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()

    # format and print results
    for i in result:
        print("{1} --- {0} views".format(i[1], i[0]))


def request_errors_by_day():
    '''This method lists the days on which the number
    of HTTP requests with error status exceeded 1'''

    # The SQL query which return the data
    query = '''
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
    '''

    # Execute the query
    connection = psycopg2.connect(database=DBNAME)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()

    # format and print results
    for i in result:
        print("day: {0} --- Error percent: {1}%".format(i[0], round(i[1], 2)))
