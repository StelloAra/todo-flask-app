import sqlite3

def connect():
    return sqlite3.connect("todo.db")

def add_task(title):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()
    print("Uppgift tillagd!")

def show_tasks():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    
    tasks = cursor.fetchall()
    
    print("\n--- Dina uppgifter ---")
    for task in tasks:
        status = "✔️" if task[2] else "❌"
        print(f"{task[0]}. {task[1]} [{status}]")
    
    conn.close()

def mark_done(task_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print("Markerad som klar!")

def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print("Uppgift borttagen!")

# 🔁 MENY LOOP
while True:
    print("\n--- TO DO LISTA ---")
    print("1. Visa uppgifter")
    print("2. Lägg till uppgift")
    print("3. Markera som klar")
    print("4. Ta bort uppgift")
    print("5. Avsluta")

    choice = input("Välj: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        title = input("Vad ska göras? ")
        add_task(title)

    elif choice == "3":
        task_id = int(input("ID att markera klar: "))
        mark_done(task_id)

    elif choice == "4":
        task_id = int(input("ID att ta bort: "))
        delete_task(task_id)

    elif choice == "5":
        print("Hej då!")
        break

    else:
        print("Fel val!")