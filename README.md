
<h1>LOG-ANALYSIS</h1>

This is a log analysis project for Udacity Intro to Programming Nanodegree Program.
It uses a python file to query a PostgreSQL database 
and answer 3 questions. 

This requires some setup.  It uses Vagrant and Virtual Box.

<h2>DIRECTIONS TO START PROGRAM:</h2>

cd to the vagrant file, this is where the python file should be<br>
`vagrant up` - starts vagrant<br>
`vagrant ssh`  - log into vagrant<br>
`cd /vagrant`  - so you are in the vagrant file<br>
`psql -d news -f newsdata.sql`  - to load the data from the sql file<br>
`psql - news`  - to get into the news file so can query<br>
`python newsdatadb.py`  - runs the python file

There are 3 tables inside the file and the problem is to answer 3 questions with queries to the 
database with python. The tables are articles, authors, and log.  Return the answers to 3 questions
in plain text.

<h3>QUESTIONS:</h3>
1.  What are the most popular 3 articles? 
2.  Who are the most popular authors?
3.  What day had errors over 1%?
