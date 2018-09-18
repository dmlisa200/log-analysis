# log-analysis
log analysis project for Udacity Intro to Programming Nanodegree program
This project uses Vagrant and Virtual Box
cd to the vagrant file, this is where the python file should be
vagrant up - to start vagrant
vagrant ssh - to log into vagrant
cd /vagrant - so you are in the vagrant file 
psql -d news -f newsdata.sql  - to load the data from the sql file so can query 
psql -d news   - to get into the news file so can query
There are 3 tables inside the file and the problem is to answer 3 questions with queries to the database with python.  
run the python file  - python newsdatadb.py
It returns answers to 3 questions in plain text
