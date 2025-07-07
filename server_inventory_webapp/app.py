from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL database credentials
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'pass'
DB_NAME = 'instance_details'

@app.route('/')
def index():
    inventory = get_inventory_from_db()
    return render_template('index.html', inventory=inventory)


@app.route('/admin')
def home():
    return '<footer style="font-size:14px; text-align:center; margin-top:20px;">Created by Arpit © 2025</footer>'

def get_inventory_from_db():
    db = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = db.cursor()

    query = "SELECT * from instance_info_new"
    cursor.execute(query)
    rows = cursor.fetchall()
    inventory = [{'id': row[0], 'instance_name': row[1], 'instance_type': row[2], 'instance_ip': row[3], 'instance_id': row[4], 'deployment_id': row[5]} for row in rows]

    db.close()
    return inventory

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)
