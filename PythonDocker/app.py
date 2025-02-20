from flask import Flask, render_template
import mysql.connector
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="db"
    )
    cursor = conn.cursor()
    cursor.execute("select * from students")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
