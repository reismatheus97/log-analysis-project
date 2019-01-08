#! /usr/bin python

import psycopg2
from datetime import datetime

DBNAME = "news"
db = psycopg2.connect(database=DBNAME)


def welcome():
    print("\n#########################################################")
    print("########## Welcome to the Log Analysis Project ##########")
    print("##########        github: reismatheus97        ##########")
    print("#########################################################")


def end():
    print("\n#########################################################")
    print("#######################   Bye ...    ####################")
    print("#########################################################")


def answer1():
    print("\nAnswer 1: \n    Loading...")
    cursor = db.cursor()
    cursor.execute("""
        select articles.title, t.views
        from articles
        join (select substr(log.path, 10) as path, count(*) as views
                from log where path like '/article%'
                group by log.path order by 2 desc limit 3) as t
        on articles.slug = t.path order by t.views desc;
    """)
    rows = cursor.fetchall()
    print("    - Results:")
    for row in rows:
        print("      %s - %d views" % (row[0], row[1]))
    cursor.close()


def answer2():
    print("\nAnswer 2: \n    Loading...")
    cursor = db.cursor()
    cursor.execute("""
    select authors.name, count(authors.id) as views
        from log, articles, authors
        where substr(log.path, 10) = articles.slug and
                articles.author = authors.id 
        group by authors.id order by views desc;
    """)
    rows = cursor.fetchall()
    print("    - Results:")
    for row in rows:
        print("      %s - %d views" % (row[0], row[1]))
    cursor.close()


def answer3():
    print("\nAnswer 3: \n    Loading...")
    cursor = db.cursor()
    cursor.execute("""
        select
            to_date(day,'YYYY-MM-DD'),
            round((TotalErrors*100)::decimal/(OnePercent*100),2) 
                as Error_Percentage
        from (select 
                substr(to_char(date_trunc('day', time), 'YYYY-MM-dd'),1,10) 
                    as OnePercentDay,
                count(*)/100
                    as OnePercent
                from log group by 1) as a,
            (select 
                substr(to_char(date_trunc('day', time), 'YYYY-MM-dd'),1,10)
                    as day,
                count(*) as TotalErrors
                from log where status like '4%' group by 1) as b
        where (a.OnePercentDay = b.day) and (a.OnePercent < b.TotalErrors);
    """)
    rows = cursor.fetchall()
    print("    - Results:")
    for row in rows:
        print('      {:{dfmt}}'.format(row[0], dfmt='%Y-%m-%d') +
              ' - ' +
              str(row[1]) +
              '%')
    cursor.close()


def main():
    try:
        welcome()
        answer1()
        answer2()
        answer3()
        end()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        db.close()


main()
