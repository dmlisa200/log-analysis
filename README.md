
<h1>LOG-ANALYSIS</h1>

This is a log analysis project for Udacity Intro to Programming Nanodegree Program.
It uses a python file to query a PostgreSQL database 
and answer 3 questions. 

This requires some setup.  It uses a virtual machine need to install Vagrant and Virtual Box.   This also requires
this SQL file [newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)<br>
unzip the file and put it and the newsdatadb.py in a folder called log_analysis in the vagrant directory.

<h2>DIRECTIONS TO START PROGRAM:</h2>

cd to the vagrant file<br>
`vagrant up` - starts vagrant<br>
`vagrant ssh`  - log into vagrant<br>
`cd /vagrant`  - so you are in the vagrant file<br>
`cd log_analysis`  -  in the log_analysis file
`psql -d news -f newsdata.sql`  - to load the data from the sql file<br>
`psql - news`  - to get into the news file so can query<br>
`python newsdatadb.py`  - runs the python file

There are 3 tables inside the file and the problem is to answer 3 questions with queries to the 
database with python. The tables are articles, authors, and log.  Return the answers to 3 questions
in plain text.

<h3>QUESTIONS:</h3>
1.  What are the most popular 3 articles?<br>
2.  Who are the most popular authors?<br>
3.  What day had errors over 1%?
