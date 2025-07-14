# 🖥️ Inventory Management Web App
Welcome to the Inventory Management Web App! This Flask + MySQL project fetches and displays instance details from a database in a modern, responsive web UI using Bootstrap and DataTables.

📜 Overview
This application allows you to view server or instance metadata (like name, type, IP, creation time, etc.) stored in a MySQL database. It presents the data in a searchable, paginated table within a web interface. The app also includes author attribution and a basic API route.

🚀 Features
📊 Displays instance data in a dynamic, searchable table using DataTables.

🧩 Connects to a MySQL database to fetch real-time data.

🧾 Clean Bootstrap-based UI.

📡 API-ready structure (Flask route /ajaxfile).

🪪 Trademark/footer attribution: Created by Arpit © 2025

⚙️ How It Works
Flask Backend: Handles routing, database connection, and serving templates.

MySQL Integration: Connects to the instance_details database and fetches data from the instance_info_new table.

Data Fetching: Uses a get_inventory_from_db() Python function to run a SELECT * query.

Frontend Display:

Loads index.html using Jinja.

Displays instance data using DataTables (with AJAX and pagination).

API Route: A simple /admin route shows app authorship information.

📦 Installation
Make sure you have the following installed:

Python 3.x

Flask

mysql-connector-python

MySQL Server (local or remote)

Install dependencies using:

bash
Copy
Edit
pip install flask mysql-connector-python
🏁 Getting Started
1️⃣ Clone the Repository:
bash
Copy
Edit
git clone https://github.com/arpit-litoria/python_projects.git
cd python_projects/inventory_app
2️⃣ Set up your MySQL database:
Database name: instance_details

Table: instance_info_new

Fields: id, instance_name, instance_type, instance_ip, instance_id, deployment_id

3️⃣ Start the Flask App:
bash
Copy
Edit
python app.py
Visit: http://localhost:80 in your browser.

🔗 Routes
Route	Description
/	Main inventory dashboard
/admin	Simple author attribution page
/ajaxfile	Backend data route for DataTables

🧾 Credits
Created by Arpit © 2025
Made with Flask, MySQL, Bootstrap & ❤️

