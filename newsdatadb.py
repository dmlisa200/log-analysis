
import psycopg2


def runs_query(query):
   ''' This is the query function that is the same for each question function,  each question
   has its own query that is inserted'''
   
   db = psycopg2.connect("dbname=news")
   c = db.cursor()
   c.execute(query)
   answer = c.fetchall()
   db.close()
   return answer
   
   
   
def top_articles():
   '''This is question 1 that finds 3 most popular articles and prints the articles names with number
   of views for each'''
    
    query =  """
        SELECT articles.title, COUNT(*) 
        FROM articles
        JOIN log
        ON log.path LIKE CONCAT('/article/%', articles.slug)
        GROUP BY articles.title
        ORDER BY COUNT(*) desc
        limit 3;
    """
    
    results = runs_query(query)
    
    print('\nMOST POPULAR ARTICLES OF ALL TIME:')
    count = 1
    for i in results:
        title = i[0]
        views = '" has ' + str(i[1]) + " views"
        print( title + views)
        count+=1
        
        
        
def top_article_authors():
   '''This is the query for question 2 that returns the top three most popular authors and prints
   the names and the number of views for each'''
    
    query = """
        SELECT authors.name, COUNT(*)
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY COUNT(*) DESC
        LIMIT 3;
    """
    
    results = runs_query(query)
    
    print('\nMOST POPULAR ARTICLE AUTHORS OF ALL TIME:')
    count = 1
    for i in results:
        print( i[0] + ' has ' + str(i[1]) + " views")
        count+=1
        
        
        
def days_with_errors():
   '''this is question 3 that finds the day with errors over 1% then prints
   the date'''
    
    
    query = """
        SELECT total.day,
           ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (
            SELECT date_trunc('day', time) "day", count(*) AS error_requests
            FROM log
            WHERE status = '404 NOT FOUND'
            GROUP BY day) AS errors
            JOIN (SELECT date_trunc('day', time) "day", count(*) AS requests
            FROM log
            GROUP BY day) AS total
            ON total.day = errors.day
            WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
            ORDER BY percent DESC;
        """    
            
    results = runs_query(query)
        
    print('\nDAYS WITH MORE THAN 1% OF REQUEST ERRORS:')
    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print(date + " has " + errors)
            
print('The Results Are:  ')
top_articles()
top_article_authors()
days_with_errors()
        
        


    
