import sqlite3
from flask import Flask, request,jsonify
app = Flask(__name__) # create object for Flask

connection = sqlite3.connect('poc.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE if not exists user(id int not null primary key, name text, password text, city text,country text , pinocde int ,age int)')
connection.commit()
connection.close()



@app.route('/register', methods = ['POST'])
def register():
    try:

        user = request.get_json()
        password = request.json['password']
        if len(password) > 8:
            return jsonify({'error': 'password should be less than 8 character'})
        connection = sqlite3.connect('poc.db')
        cursor = connection.cursor()
        cursor.execute("insert into user values ('{}','{}','{}','{}','{}','{}','{}')".format(user['id']
                                                                                                 ,user['name']
                                                                                                 ,user['password']
                                                                                                 ,user['city']
                                                                                                 ,user['country']
                                                                                                 ,user['pincode']
                                                                                                 ,user['age']))
        connection.commit()
        connection.close()
        return "User created successfully....."
    except:
        print("Error occured while creating records")


@app.route('/update',  methods = ['POST'])
def updatefunc():
    user = request.get_json()
    connection = sqlite3.connect('poc.db')
    cursor = connection.cursor()

    return "changed successfully.."

@app.route('/delete',  methods = ['POST'])
def deletefunc():
    user = request.get_json()
    connection = sqlite3.connect('poc.db')
    cursor = connection.cursor()
    cursor.execute("delete from user where id = '{}'".format(user['id']))
    connection.commit()
    return "User deleted  successfully.."

@app.route('/showuser')
def showall():
    connection = sqlite3.connect('poc.db')
    cursor = connection.cursor()
    records = cursor.execute('select id,name,city,country,pincode,age from user')
    return jsonify({'user': list(records)})


@app.route('/show')
def show():
    connection = sqlite3.connect('poc.db')
    cursor = connection.cursor()
    records = cursor.execute('select id,country from user')
    return jsonify({'user': list(records)})

app.run(port=8000)