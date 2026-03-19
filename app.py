from flask import Flask, request, redirect, render_template
import sqlite3
import os

def init_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done INTEGER DEFAULT 0
    )
    """)
    
    conn.commit()
    conn.close()

app = Flask(__name__)

def connect():
    return sqlite3.connect("todo.db")

def get_tasks():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def add_task(title):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()

def toggle_task(task_id):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT done FROM tasks WHERE id = ?", (task_id,))
    current = cursor.fetchone()[0]
    
    new_value = 0 if current else 1
    cursor.execute("UPDATE tasks SET done = ? WHERE id = ?", (new_value, task_id))
    
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

@app.route("/")
def home():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if title:
        add_task(title)
    return redirect("/")

@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle(task_id):
    toggle_task(task_id)
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    delete_task(task_id)
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))