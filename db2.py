import mysql.connector
from mysql.connector import Error

def read(key):
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         sql_fetch_query = """SELECT password from faculty where usn=%s"""
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query,(key,))
         record = cursor.fetchall()

         if(len(record)==0):
             return ''

         return str(record[0][0])

    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def sread(key):
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         sql_fetch_query = """SELECT password from student where usn=%s"""
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query,(key,))
         record = cursor.fetchall()

         if(len(record)==0):
             return ''

         return str(record[0][0])

    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def sqns(key):
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         sql_fetch_query = """SELECT class from student where usn=%s"""
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query,(key,))
         record = cursor.fetchall()[0][0]

         print("aaa")
         print(record)

         sql_fetch_query=""" select test_id,tname,questions,end_time from test where sta_time<ADDTIME(now(),"5:30:00") and end_time>ADDTIME(now(),"5:30:00") and tcode=%s;  """

         cursor.execute(sql_fetch_query,(record,))
         record =cursor.fetchall()
         #record[0][3]=str(record[0][3])
         print("ee",record)
         if len(record)==0:
             return 0,0
         return (record[0][:3]),str(record[0][3])

    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def tread(key):
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         sql_fetch_query = """select stu_id,answers,tot_marks from score where test_id=%s"""
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query,(key,))
         record = cursor.fetchall()

    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         sql_fetch_query = """select fca_usn,questions,tname from test where test_id=%s"""
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query,(key,))
         record1 = cursor.fetchall()
         
        

         #return record,record1

    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         sql_fetch_query = """select email from faculty where usn=%s"""
         print(sql_fetch_query)
         key=record1[-1][0]
         cursor.execute(sql_fetch_query,(key,))
         em = cursor.fetchall()


         return record,record1,em

    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1


    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def mcq_update(test_id,stu_id):
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         sql_fetch_query = """update score set tot_marks=tot_marks +1 where test_id=%s and stu_id=%s"""
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query,(test_id,stu_id,))
         
         connection.commit()
         record=cursor.rowcount
         
         if(record==0):
             try:                 
                 sql_fetch_query = """insert into score values(%s,%s,'',1)"""
                 print(sql_fetch_query)
                 print(cursor.execute(sql_fetch_query,(test_id,stu_id,)))
                 connection.commit()
                 return 1
          

             except mysql.connector.Error as error:
                 print("Failed to read data from MySQL table {}".format(error))
                 return -1

         return record 

    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def des_update(test_id,stu_id,ans):
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         sql_fetch_query = """UPDATE score SET answers = CONCAT(answers, %s) WHERE test_id =%s and stu_id=%s"""
         print(sql_fetch_query)
         ans=ans+"`~#%"
         cursor.execute(sql_fetch_query,(ans,test_id,stu_id,))
         connection.commit()
         record=cursor.rowcount

         print("yeeepppp",record,ans)

         if(record==0):
             try:

                 sql_fetch_query = """insert into score values(%s,%s,%s,0)"""
                 print(sql_fetch_query)
                 print(cursor.execute(sql_fetch_query,(test_id,stu_id,ans,)))
                 connection.commit()
                 return 1


             except mysql.connector.Error as error:
                 print("Failed to read data from MySQL table {}".format(error))
                 return -1

         return record

    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



#print(des_update("72","3",'Nanda'))
#print(sqns('12345'))
#print(read("01jst17cso64"))

#print(tread(72))

#print(sqns(222))
