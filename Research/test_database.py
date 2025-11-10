import pyodbc

server = 'BMVSQLQ20FW\Q20FWBMVQA'
database = 'QA_Results'
username = 'AutomatedTester'
password = 'XU#F8sxKeR'

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

cursor = conn.cursor()

cursor.execute("Select top 10 * from Test_Run_AM")

for row in cursor.fetchall():
    print(row)

conn.close()