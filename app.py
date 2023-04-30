import os
from flask import Flask
import mysql.connector

app = Flask(__name__)

# configure db
mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or 'localhost'
db = mysql.connector.connect(
    host=mysql_database_host,
    user="db_user",
    password="Passw0rd",
    database="employee_db"
)


@app.route("/", methods=['GET'])
def main():
    return "Welcome!"

@app.route('/how are you', methods=['GET'])
def hello():
    return 'I am good, how about you?'

@app.route('/read from database', methods=['GET'])
def get_employees():
    # Fetch data from employees table
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees")
    results = cursor.fetchall()

    # Join all the data into a string
    employee_data = ""
    for row in results:
        employee_data += f"{row[1]} {row[2]} ({row[3]}) - Hired on {row[5]} with a salary of ${row[6]}\n"

    # Return the joined string
    return employee_data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
