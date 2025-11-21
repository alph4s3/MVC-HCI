# Notes App (MVC)  
A simple CRUD application built using **Flask + SQLite**, demonstrating the **Model-View-Controller (MVC)** architecture for our Interactive System Development (HCI) project.

**Repository:** https://github.com/alph4s3/MVC-HCI.git

---

## 🔧 Built With  
- [Flask] – Python web framework  
- SQLite3 – Relational db
- HTML / CSS / Jinja2  – For the view  

---

## 🏗 Architecture Overview

### **Model** (`models.py`)  
Responsible for everything data-related: connecting to the database, creating tables, and providing functions such as:  
- `create_note(title, content, category)`  
- `get_all_notes(search, category)`  
- `get_note(id)`  
- `update_note(id, title, content, category)`  
- `delete_note(id)`  
Each note includes: title, content, category, created timestamp, and updated timestamp.

### **View** (`templates/` + `static/styles.css`)  
Handles how things look and feel.  
- `base.html` — layout with navigation bar and flash message area  
- `index.html` — lists all notes with category and timestamps  
- `create.html` — form to add a new note  
- `edit.html` — form to edit an existing note  
Styling in `static/styles.css` gives a clean, user-friendly interface with cards, hover effects, and responsive layout.

### **Controller** (`app.py`)  
Handles user interactions and coordinates Model & View:  
- Routes: `/`, `/create`, `/edit/<id>`, `/delete/<id>`  
- Validates user inputs (title and content must not be blank)  
- Uses flash messages for feedback (success or error)  
- Passes data to templates and triggers model functions  

---

## 👤 How Users Interact With the App  
1. Open the homepage and view all notes displayed in card form.  
2. Click “Create Note” to enter a title, content, and select a category.  
3. Submit the form — if any required fields are missing, an error message appears.  
4. Upon success, the new note appears, and a success message is shown.  
5. Each note shows category, created date, updated date, and offers “Edit” or “Delete”.  
6. Editing or deleting updates the interface immediate, maintaining clear feedback and usability.

---

## ▶️ How to Run Locally  
1. Install dependencies:  
   ```bash
   pip install flask
   
2. Run
   ```bash
   python app.py or python3 app.py
3. Open in browser
   ```cpp
   http://127.0.0.1:5000/
   
   If you get an error like OperationalError: table notes has no column named category, delete the existing notes.db file and rerun the app — the database will rebuild

🎥 Demo Video

https://drive.google.com/file/d/1W6UTZl64B3lpReIl7u0lhQeKWVK1giZZ/view?usp=sharing

