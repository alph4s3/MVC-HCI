📘 Flask MVC Notes App

A simple but enhanced CRUD Notes Application built using Flask + SQLite, demonstrating the Model-View-Controller (MVC) architecture for our Interactive System Development (HCI) activity.

🔗 Repository: https://github.com/alph4s3/MVC-HCI.git

🚀 Framework Used

Flask (Python) — a lightweight web framework that naturally supports MVC using:

Controllers → Python route functions

Models → Python database logic

Views → Jinja2 templates

Database: SQLite3 (portable, simple, and perfect for small projects)

🧩 MVC Structure Overview
🟦 Model (models.py)

Handles all database logic:

Connects to SQLite

Creates the notes table

Provides CRUD operations:

create_note()

get_notes()

get_note()

update_note()

delete_note()

Each note has:

Title

Content

Category

Created_at

Updated_at

🟩 View (templates/ + static/)

User interface built using HTML + Jinja:

Templates

base.html → shared layout

index.html → list of notes

create.html → add new note

edit.html → edit existing note

CSS

Located in static/styles.css

Modern colors, spacing, hover effects, rounded cards

Flash messages for validation feedback

🟥 Controller (app.py)

Manages:

Request handling

Routing

Input validation

Flash messages

Calling model functions

Passing data to templates

Routes:

GET  /
GET/POST  /create
GET/POST  /edit/<id>
POST      /delete/<id>

🧑‍💻 User Workflow

User opens the homepage and sees all notes displayed as colorful cards.

Clicks Create Note → fills in Title, Content, Category.

Form validates input (empty fields blocked).

Note appears with timestamps + category tag.

User can Edit or Delete notes easily.

Flash messages show success or errors throughout the process.

🎥 Video Demo

📌 Insert your Google Drive / YouTube link here

🛠️ How to Run the App
1. Install dependencies
pip install flask

2. Run the server
python app.py

3. Open in browser
http://127.0.0.1:5000/

❗ If you get:

sqlite3.OperationalError: table notes has no column named category

👉 Delete notes.db
👉 Rerun the app (it will recreate the database)
