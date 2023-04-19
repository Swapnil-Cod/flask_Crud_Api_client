from flask import Flask,render_template,request, redirect, jsonify
import os
import json
import requests

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    if request.method=="GET":
        url = "http://127.0.0.1:5000/std"
        # response = urllib.request.urlopen(url)
        # data = response.read()
        # data = json.loads(data)
        # print(data)
        response = requests.get(url=url)
        data=response.text
        data1=json.loads(data)
    return render_template("index.html",users=data1)

@app.route('/add/',methods=['GET','POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')

    if request.method=="POST":
        Name = request.form['name']
        Phone = request.form['phone']
        Address = request.form['address']
        data={
            "std_name":Name ,
            "std_phoneNo":Phone ,
            "std_address": Address
        }
        url = "http://127.0.0.1:5000/std"
        resp = requests.post(url ,json=data)
        return redirect('/')

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    if request.method == 'GET':
        url = "http://127.0.0.1:5000/std"
        data={
            "std_id":id
        }
        response = requests.get(url=url,json=data)
        data1=response.text
        data2=json.loads(data1)
        return render_template('update.html',userz=data2)

    if request.method=="POST":
        Name = request.form['name']
        Phone = request.form['phone']
        Address = request.form['address']
        data={
            "std_id":id,
            "std_name":Name ,
            "std_phoneNo":Phone ,
            "std_address": Address
        }
        url = "http://127.0.0.1:5000/std"
        resp = requests.put(url ,json=data)
        return redirect('/')

@app.route('/delete/<int:id>',methods=['GET','POST'])
def delete(id):
    
        data={
            "std_id":id
        }
        url = "http://127.0.0.1:5000/std"
        resp = requests.delete(url ,json=data)
        return redirect('/')
        
if __name__=='__main__':
    app.run(port=8000,debug=True)