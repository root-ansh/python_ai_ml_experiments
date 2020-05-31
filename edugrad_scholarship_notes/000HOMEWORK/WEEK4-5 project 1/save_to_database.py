import mysql.connector
import csv

#-------1. read database-creation SQL file--------------------
filename="CreateDatabaseAndTables.sql"
all_sql=""
with open(filename,'r',newline='') as f:
    all_sql=f.read()
print('successfully read all sql commands')

#-------2. create datbase from this string--------------------
all_sql = all_sql.replace('\n','')
sql_list = all_sql.split(';')
mDB = mysql.connector.connect(host='localhost',user='root',passwd='1234')
cursr=mDB.cursor()
for command in sql_list:
    cursr.execute(command)
print('successfully executed all sql commands. database is ready')

#------3. load csv file --------------------------------------
filename="naukri_spider/naukri_dataanalytics.csv"
all_csv=[]
with open(filename,'r',newline='') as f:
    reader= csv.reader(f)
    all_csv=list(reader)
print('successfully read csv file')
#------4. split the location data ----
for i in range(len(all_csv)):
    all_csv[i][3]=all_csv[i][3].split(',')
    
print('sucessfully performed operations on the csv data')

#------5. insert this data into database ---------------------
#mDB, cursr created in section 2

for row in all_csv:
    try:
        COMMAND1="INSERT INTO DATA_ANALYST_NCR \
            (`JOB_TITLE`,`LINK`,`COMPANY_NAME`,`EXPERIENCE_REQUIRED`,`KEYSKILLS`,\
            `JOB_DESCRIPTION`,`SALARY`,`DATE_POSTED`,`LAST_UPDATED_ON`)\
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,NOW())"
        cursr.execute(COMMAND1,(row[0],row[1],row[2],row[4],row[5],row[6],row[7],row[8]))

        job_id=cursr.lastrowid
        COMMAND2="INSERT INTO LOCATION_JOBS (`JOB_ID`,`LOCATION`)VALUES(%s,%s)"
        for i in row[3]:
            cursr.execute(COMMAND2,(job_id,i))
        mDB.commit()
        print("added to database successfully")
    except:
        mDB.rollback()
        print("error occurred while adding the following row:")
        print(str(row))

mDB.close()

#-------------------------------------------------------------
