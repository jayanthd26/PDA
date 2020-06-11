import xlsxwriter 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

def mail(x):

    print("Hereeeeeeeeeeeeeeee ",(x))
    email=x[-1][-1][-1]
    ans=x[0]
    txt= x[-2][-1][-2]
    fac_usn=x[-2][-1][0]
    qn=[]
    for i in txt.split("~`^")[:-1]:
                if (i.find("~`#^") == -1):
                     qn.append(i)
         
            
            
    workbook = xlsxwriter.Workbook(fac_usn+'.xlsx')   
    worksheet = workbook.add_worksheet("My sheet") 
    
    row = 0
    col = 1
    
    worksheet.write(row, 0, "Student USN")
    
    for i in qn:
        worksheet.write(row, col, i)
        col+=1
        
    worksheet.write(row, col, "MCQ Marks Obtained")
    
    l=col
    col=0
    row=1
    
    for a in ans:
        worksheet.write(row, col, a[0])
        col+=1
        for i in a[1].split("`~#%")[:-1]:
                  worksheet.write(row, col, i)
                  col+=1
        worksheet.write(row, l, a[-1])
        row+=1
        col=0
    
    workbook.close()   
    
    print(email,ans,"ufff")
                
    fromaddr = "nandakrishna.achar@gmail.com"
    toaddr = email
    
    msg = MIMEMultipart() 
    
    msg['From'] = "nandakrishna.achar@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Test Results" 
    body = "Answers of all students are recorded here : " 
    msg.attach(MIMEText(body, 'plain')) 
    
    filename = fac_usn+".xlsx"
    path="/home/ec2-user/PDA/"
    
    attachment = open(path+filename, "rb") 
    
    p = MIMEBase('application', 'octet-stream')  
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
     
    msg.attach(p) 
    
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, "nanda1999007") 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit() 
    
    print("Donee")

#mail(([(2, 'DA`~#%DA`~#%', 0), (3, 'DA`~#%Nanda`~#%', 0)], [('123', 'who is the boss~`#^jee,,,jay,,,nan,,,nag,,,a~`^Who is the yalsu~`^who is the player~`#^jee,,,jay,,,nanda,,,nag,,,c~`^Who is the family man~`^', 'test3')], [('jeevanthdayalu@gmail.com',)]))

