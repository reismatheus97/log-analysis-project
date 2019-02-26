# log-analysis-project
The third project into the Udacity's Full Stack Developer Nanodegree.  
This isn't a commercial project and has only academic purposes. 

# About
This is an **internal reporting tool** that uses information from a database to discover specific informations about users and they preference. 

It analyzes a fictional newspaper site that is already running on and creating logs in a database when some page get accessed. 

The solution is written using **Python** and **PostgreSQL**.  
It explores basics concepts about:
- Connections between an application and a database server
- Querying and manipulating data (filtering, grouping, parsing)
- Use of imports, native modules of Python
- Isolation between application and the database server
- Formatting data to a better application's output
- Error handling

# Proposed questions
These are the questions the reporting tool should answer: 
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors? 

# Requirements
The project inside a virtual machine provided by [VirtualBox](https://www.virtualbox.org/) and managed by [Vagrant](https://www.vagrantup.com/)

The ```Vagrantfile``` will be used to set the VM configuration. \
With the VM built with this file and running up, we are ready to go. 

The [Python](https://www.python.org/) language can be used with versions 2 and 3.

The [PostgreSQL](https://www.postgresql.org/) relational database can be used in the most recent versions.

The ```newsdata.sql``` file provided by Udacity. Download [link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

# Running the project
1- Clone the repo to a folder on your local machine: \
```$ git clone https://github.com/reismatheus97/log-analysis-project.git``` 

2- Get into the project's folder: \
```$ cd log-analysis-project``` 

3- Copy ```log-analysis-project.py``` and ```newsdata.sql``` and paste both into the vagrant shared directory inside your virtual machine.

4- Connect to your VM and get into the vagrant shared directory: \
```$ cd / & cd /vagrant ``` 

5- Set the data:
```psql -d news -f newsdata.sql```

6- Then, run: \
```$ python log-analysis-project.py ```

