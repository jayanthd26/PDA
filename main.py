import urllib.request
from flask import Flask, request, redirect, jsonify,render_template
from werkzeug.utils import secure_filename
import db2 
import json
import db_connect as db
from flask import Response
import mail

app = Flask(__name__)

@app.route('/details/', methods=['POST'])
def addOne():

    data = request.get_json()
    print("heloo",data)
    print(data['usn'])
    return jsonify({'name' : 'Registered','status':'True'})

@app.route('/facultylogin/', methods=['POST'])
def login():

    data = request.get_json()
    print("heloo",data)
    print(data['usn'])
    print(data['pass'])
    
    p=db2.read(data['usn'])

    if(p==''):
        st="Not Registered!"
    elif(p==data['pass']):
        st="Success!"
    else:
        st="Incorrect Password!"
    return jsonify({'status':st})


@app.route('/slogin/', methods=['POST'])
def slogin():

    data = request.get_json()
    print(data['usn'])
    print(data['pass'])

    p=db2.sread(data['usn'])

    if(p==''):
        st="Not Registered!"
    elif(p==data['pass']):
        st="Success!"
    else:
        st="Incorrect Password!"
    return jsonify({'status':st})



@app.route('/fsign/', methods=['POST'])
def fsign():
    data = request.get_json()
    print("heloo",data)
    print(data)
    if((db.facsignup(data['usn'],data['name'],data['email'],data['pass']))==1):
        return jsonify({'name' : 'Registered','status':'True'})
    return jsonify({'name' : 'Not Registered','status':'False'})


@app.route('/qns/', methods=['POST'])
def qns():
    data = request.get_json()
    print("heloo",data)
    if((db.add_ques(data['fusn'],data['ques'],data['stime'],data['etime'],data['tname'],data['tcode']))==1):
        return jsonify({'status':'True'})
    return jsonify({'status':'False'})

    

@app.route('/test/', methods=['POST'])
def test():
    data = request.get_json()
    print("heloo",data)
    #print(data['stdusn'])

    qns_end=(data['stdusn'])
    print("qdb2",qns_end)
    a,b=(db2.sqns(qns_end))
    print("Nandaa",a,b)
    js=(db.ret_test(a,b))
    print("Heyyyyyyy",js) 
    # return jsonify({"i":"i"})

    #js = [ {"id":"1","end_time":"2020-05-23 16:45:00","test_name":"Physics"}, { "id" : "1891","a": "Naaga","b": "Nanda","c": "jeeva","d": "Jaya","qns": "What is my name?"},{"id" : "1893","a": "1","b": "2","c": "3","d": "4","qns": "Which sem?"},{"id" : "1793","qns": "Tell me abt urslef?"},{"id" : "1633","qns": "Explain abt clg?"}]

    return Response(json.dumps(js),  mimetype='application/json')

@app.route('/next/',methods=['POST'])
def next():
    print("NEXTTTT")
    data = request.get_json()
    print(data['usn'])
    print(data['crt'])
    print("uuuu",data) 
    if(data['crt']=='1'):
        print("CUT")
        db2.mcq_update(data['tid'],data['usn'])
    else:
        db2.des_update(data['tid'],data['usn'],data['crt'])
    

    return jsonify({'st':'True'})

@app.route('/sregister/', methods=['POST'])
def sr():
    data = request.get_json()
    print("heloo",data)
    print(data)
    print(type(data['name']))
    print(type(data['pass']))
    print(type(data['usn']))
    print(type(data['class']))
    print(type(data['email']))
    if((db.stu_signup(data['name'],data['usn'],data['class'],data['email'],data['pass']))==1):
        return jsonify({'name' : 'Registered','status':'True'})
    return jsonify({'name' : 'Not Registered','status':'False'})



@app.route('/ftest/', methods=['POST'])
def ftest():
    data = request.get_json()
    print("id",data)
    print(data['fusn'])
    
    qns_end=(data['fusn'])
    print("fusn",qns_end)
    js=(db.f_test(qns_end))

    return Response(json.dumps(js),  mimetype='application/json')


@app.route('/ftid/', methods=['POST'])
def ftid():
    data = request.get_json()
    print(data['tid'])

    qns_end=(data['tid'])
    print("fusn",qns_end)
    js=(db.f_tid(int(qns_end)))

    return Response(json.dumps(js),  mimetype='application/json')


@app.route('/email/',methods=['POST'])
def email():
    print("EMAILL")
    data = request.get_json()

    print(data)

    mail.mail(db2.tread(data['tid']))

    return jsonify({'st':'True'})




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)

