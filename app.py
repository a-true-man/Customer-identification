from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
from db import get_client, add_client, update_client, get_all_clients
current_client = None
import json, os


app = Flask(__name__)

RECENT_PATH = 'data/recent.json'
current_calls = []   # רשימת לקוחות נוכחיים (יכולה להכיל מספר)

@app.route("/")
def index():
    clients = get_all_clients()
    return render_template("index.html", clients=clients)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        status = request.form["status"]
        notes = request.form["notes"]
        add_client(name, phone, status, notes)
        return redirect(url_for("index"))
    return render_template("add_client.html")

@app.route("/clients")
def all_clients():
    clients = get_all_clients()
    return render_template("client_list.html", clients=clients)

@app.route("/edit/<phone>", methods=["GET", "POST"])
def edit(phone):
    print("Phone to edit:", phone)
    client = get_client(phone)
    print("Client from DB:", client)
    if request.method == "POST":
        name = request.form["name"]
        status = request.form["status"]
        notes = request.form["notes"]
        update_client(phone, name, status, notes)
        return redirect(url_for("index"))
    return render_template("edit.html", client=client)

def load_recent():
    if os.path.exists(RECENT_PATH):
        return json.load(open(RECENT_PATH, 'r'))
    return []

def save_recent(lst):
    with open(RECENT_PATH, 'w') as f:
        json.dump(lst[:30], f, ensure_ascii=False)

@app.route('/api/incoming_call', methods=['GET','POST'])
def incoming_call():
    phone = request.values.get('ApiPhone','').strip()
    hangup = request.values.get('hangup')  # ימות שולחים למשל hangup=yes
    client = get_client(phone) or {'phone': phone, 'name': None, 'status': None, 'notes': ''}

    # אם זו שיחת hangup → העבר ל־recent והסר מ־current
    if hangup:
        # העבר לרשימת recent
        recent = load_recent()
        recent.insert(0, client)
        save_recent(recent)
        # הסר מהרשימה הנוכחית
        current_calls[:] = [c for c in current_calls if c['phone'] != phone]
    else:
        # call start → הוסף ל־current_calls אם לא קיים
        if not any(c['phone']==phone for c in current_calls):
            current_calls.append(client)

    # בונה את ההודעה שמוחזרת לימות
    if client['name']:
        msg = f"שלום {client['name']} אתה מזוהה כלקוח {client['status']},"
    else:
        msg = "שלום לא מזוהה,"

    return Response(msg, status=200, mimetype='text/plain; charset=utf-8')


@app.route('/api/current_clients')
def api_current_clients():
    return jsonify(current_calls), 200

@app.route('/api/recent_clients')
def api_recent_clients():
    return jsonify(load_recent()), 200

@app.route("/settings", methods=['GET', 'POST'])
def settings():
    return render_template('settings.html')

@app.route("/save_settings", methods=["POST"])
def save_settings():
    line_number = request.form.get("line_number")
    password = request.form.get("password")

    # שמירה לקובץ או לבסיס נתונים - כאן דוגמה פשוטה לקובץ
    with open("settings.json", "w", encoding="utf-8") as f:
        json.dump({
            "line_number": line_number,
            "password": password
        }, f, ensure_ascii=False)

    return redirect(url_for("settings"))
    
if __name__ == "__main__":
    app.run(debug=True)
# app.py