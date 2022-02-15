from flask import Flask, redirect, render_template, request, url_for
from flask_mysqldb import MySQL



app= Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Shashini@1996'
app.config['MYSQL_DB'] = 'company'

mysql = MySQL(app)




@app.route('/')
def Index() :
    
    return render_template('index.html')
        
@app.route('/insert', methods = ['POST'])
def insert () :   

    if request.method == "POST" :
        name = request.form ['emp_name']
        address = request.form ['emp_address']
        designation = request.form ['designation']
        dob = request.form ['dob']
        telephone = request.form ['telephone']
        email = request.form ['email']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employee (emp_name, emp_address, designation, dob, telephone, email) VALUES (%s, %s, %s, %s, %s, %s)", (name, address, designation, dob, telephone, email))
        mysql.connection.commit()
        return redirect(url_for('Index'))
        

if __name__ == '__main__':
    app.run(port=3307,debug=True)
