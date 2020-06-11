import mysql.connector
from math import sin, cos, sqrt, atan2,radians
from mysql.connector import Error
import random as rd
import sys
def read():
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         print("a:")
         sql_fetch_query = """SELECT * from student"""
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query)
         record = cursor.fetchall()


         return record

    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def fca_reg(usn,name,email,pas):

    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         print("a:")
        # sql_fetch_query = """insert into faculty (usn,name,email,password)values('01jst17cso63','jayant','asdwed','1345678');"""
        # print(sql_fetch_query)
         cursor.execute('''insert into faculty (usn,name,email,password) values('01jst17cso63','jayant','asdwed','1345678')''')
         record = cursor.fetchall()


         return record

    except mysql.connector.Error as error:
         print("Failed to read data from MySQL table {}".format(error))
         return -1

    finally:
         if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




def facsignup(usn,name,email,password):
    try:
        connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
        cursor = connection.cursor()
        sql_fetch_query = """insert into faculty(usn,name,email,password) values(%s,%s,%s,%s);
"""
        print(sql_fetch_query)
        print(cursor.execute(sql_fetch_query,(usn,name,email,password,)))
        connection.commit()
        return 1

    except mysql.connector.Error as error:
        print("Failed to read data from MySQL table {}".format(error))
        return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#print(fca_reg('sads'))
#print(facsignup('01jst17cso63','jayant','asdwed','1345678'))


def stu_signup(name,usn,clas,email,password):
    try:
        connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
        cursor = connection.cursor()
        sql_fetch_query = """insert into student(name,usn,class,email,password) values(%s,%s,%s,%s,%s);
"""
        print(sql_fetch_query)
        print(cursor.execute(sql_fetch_query,(name,usn,clas,email,password,)))
        connection.commit()
        return 1

    except mysql.connector.Error as error:
        print("Failed to read data from MySQL table {}".format(error))
        return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#print(stu_signup('jay','01JST17CS064','CSA','asdwed','1345678'))
def add_ques(usn,ques,stime,etime,tname,tcode):
    try:
        connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
        cursor = connection.cursor()
        sql_fetch_query = """insert into test(fca_usn,questions,sta_time,end_time,tname,tcode) values(%s,%s,%s,%s,%s,%s);
"""
        print(sql_fetch_query)
        print(cursor.execute(sql_fetch_query,(usn,ques,stime,etime,tname,tcode,)))
        connection.commit()
        return 1

    except mysql.connector.Error as error:
        print("Failed to read data from MySQL table {}".format(error))
        return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#print(add_ques('abcd','1~`#^1,,,1,,,1,,,1,,,1~`^2~`#^2,,,2,,,2,,,2,,,2~`^33333333333333333^~`','2020-05-23 08:00:16','2020-05-25 18:01:56','te3','abc'))

def ret_test(test_code,etime):
    if test_code==0:
        return [{'id':'000'}]
    try:
        print((test_code))
        txt=str(test_code[2])
        print(txt)
        print("Got")
        li_ja=[]
        for i in txt.split("~`^"):
            s=i.split('~`#^')
            #print(len(s))
            if len(s[0])==0:
                break
            elif len(s)==1:
                dic={'id':str(rd.randint(1,9)+1660),'qns':s[0]}
            else:
                op=s[1].split(',,,')
                print("Herre",op)
                dic={'id':str(ord(op[4])+1793),'a':op[0],'b':op[1],'c':op[2],'d':op[3],'qns':s[0]}
            li_ja.append(dic)
        print('111')
        f=[({'id':1,'end_time':etime,'tid':str(test_code[0]),'test_name':str(test_code[1])})]
        f.extend(li_ja)
        return f
        
    except :
        print(sys.exc_info())
        return -1
'''    
import db2
a,b=(db2.sqns('12345'))
print(ret_test(a,b))
'''
def f_test(f_usn):
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         print("a:")
         sql_fetch_query = """SELECT * from test where fca_usn=%s"""
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query,(f_usn,))
         record = cursor.fetchall()
         print(record)
         if len(record)==0:
             return [{'tid':"000"}]
         f_li=[]
         for i in record:
        
            dic={'tid':str(i[0]),'tname':str(i[5]),'etime':str(i[4])}
            f_li.append(dic)
        
         return f_li


    except mysql.connector.Error as error:
        print("Failed to read data from MySQL table {}".format(error))
        return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

print(f_test('qwe'))


def f_tid(tid):
    try:
         connection = mysql.connector.connect(host= "ec2-13-233-208-238.ap-south-1.compute.amazonaws.com",port=3306,database="pda",user= "ec2-user@13.233.208.238",password= "Hello123@")
         cursor = connection.cursor()
         print("a:")
         sql_fetch_query = """SELECT * from test where test_id=%s"""
         print(sql_fetch_query)
         cursor.execute(sql_fetch_query,(tid,))
         record = cursor.fetchall()
         txt=str(record[0][2])
         li_ja=[]
         for i in txt.split("~`^"):
             s=i.split('~`#^')
             #print(len(s))
             if len(s[0])==0:
                 break
             elif len(s)==1:
                 dic={'id':str(rd.randint(1,9)+1660),'qns':s[0]}
             else:
                 op=s[1].split(',,,')
                 dic={'id':str(ord(op[4])+1793),'a':op[0],'b':op[1],'c':op[2],'d':op[3],'qns':s[0]}
             li_ja.append(dic)
         f=[{'id':1,'start_time':str(record[0][3]),'end_time':str(record[0][4]),'tid':str(record[0][0]),'test_name':str(record[0][5])}]
         f.extend(li_ja)

         return f


    except mysql.connector.Error as error:
        print("Failed to read data from MySQL table {}".format(error))
        return -1

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#print(f_tid(62))

