from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# -------- DATABASE SETUP --------
def init_db():
    conn = sqlite3.connect("planner.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS schedules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        time TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

# -------- HOME ROUTE --------
@app.route("/")
def home():
    return "AI Smart Planner Backend Running"

# -------- GENERATE PLAN --------
@app.route("/generate", methods=["POST"])
def generate_plan():
    data = request.json
    tasks = data.get("tasks")

    # ---- SMART AI-LIKE PLANNING ----
    priority_keywords = {
        "study": 1,
        "exam": 1,
        "project": 2,
        "meeting": 2,
        "gym": 3,
        "break": 4,
        "netflix": 5,
        "entertainment": 5
    }

    def get_priority(task):
        for word in priority_keywords:
            if word in task.lower():
                return priority_keywords[word]
        return 3

    sorted_tasks = sorted(tasks, key=get_priority)

    plan = []
    start_hour = 9

    for i, task in enumerate(sorted_tasks):
        hour = start_hour + i
        suffix = "AM" if hour < 12 else "PM"
        hour_display = hour if hour <= 12 else hour - 12
        time_slot = f"{hour_display}:00 {suffix}"
        plan.append({"task": task, "time": time_slot})

    # save to database
    conn = sqlite3.connect("planner.db")
    cursor = conn.cursor()

    for item in plan:
        cursor.execute(
            "INSERT INTO schedules (task, time) VALUES (?, ?)",
            (item["task"], item["time"])
        )

    conn.commit()
    conn.close()

    return jsonify({"schedule": plan})

# -------- VIEW HISTORY --------
@app.route("/history", methods=["GET"])
def history():
    conn = sqlite3.connect("planner.db")
    cursor = conn.cursor()
    cursor.execute("SELECT task, time FROM schedules")
    rows = cursor.fetchall()
    conn.close()

    data = [{"task": r[0], "time": r[1]} for r in rows]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)