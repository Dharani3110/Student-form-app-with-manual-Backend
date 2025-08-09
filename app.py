from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student_db"
)
cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def register():
    msg = ""
    if request.method == 'POST':
        name = request.form['name']
        roll_no = request.form['roll_no']
        student_class = request.form['class']
        sql = "INSERT INTO students (name, roll_no, class) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, roll_no, student_class))
        db.commit()
        msg = "Registration successful!"
    return render_template('form.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)
