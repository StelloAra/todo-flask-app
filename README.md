# 📝 To-Do Web App (Python + Flask + SQLite)

En enkel men kraftfull To-Do applikation byggd med **Python, Flask och SQLite**.
Projektet demonstrerar en komplett **CRUD-applikation** med modern UI, inklusive dark mode 🌙

---

## 🚀 Funktioner

- ✅ Lägg till uppgifter
- 📋 Visa alla uppgifter
- ✔️ Markera som klar (checkbox)
- 🗑 Ta bort uppgifter
- 🌙 Dark mode (sparas automatiskt)
- 💾 SQLite-databas
- 🎨 Snygg och responsiv design

---

## 🧱 Tech Stack

- **Backend:** Python + Flask
- **Databas:** SQLite
- **Frontend:** HTML (Jinja2 templates), CSS
- **State:** LocalStorage (för dark mode)

---

## 📁 Projektstruktur

```
todo-app/
│
├── app.py              # Flask backend
├── todo.db            # SQLite databas
│
├── templates/
│   └── index.html     # HTML template
│
├── static/
│   └── style.css      # CSS styling
│
└── .venv/             # Virtuell miljö (ignoreras i Git)
```

---

## ⚙️ Installation

### 1. Klona projektet

```
git clone <repo-url>
cd todo-app
```

### 2. Skapa virtuell miljö

```
python3 -m venv .venv
```

### 3. Aktivera miljön

```
source .venv/bin/activate
```

### 4. Installera dependencies

```
pip install flask
```

---

## ▶️ Kör applikationen

```
python app.py
```

Öppna i din webbläsare:

```
http://127.0.0.1:5000/
```

---

## 🧠 Hur det funkar

### CRUD-logik:

- **Create:** Lägg till uppgift via formulär
- **Read:** Hämta från SQLite och visa i UI
- **Update:** Checkbox togglar `done`
- **Delete:** Ta bort via knapp

### Dark Mode:

- Toggle via knapp
- Sparas i `localStorage`
- Återställs automatiskt vid reload

---

## ✨ Framtida förbättringar

- 📅 Deadlines
- 🔥 Prioritet (Low / Medium / High)
- 🔐 Inloggning (auth)
- ☁️ Deploy (Render / Railway / Vercel)
- 📱 Mobilanpassning

---

## 💡 Lärdomar

Detta projekt visar:

- Hur backend + databas kopplas ihop
- Hur man bygger en riktig CRUD-app
- Hur man separerar frontend/backend
- Grundläggande webbutveckling med Flask

---

## 👨‍💻 Author

Byggt som ett lärandeprojekt i Python + SQL + Webbutveckling 🚀

---

# todo-flask-app

Simple full-stack To-Do web app built with Python, Flask and SQLite. Features full CRUD functionality, clean UI, and dark mode.
