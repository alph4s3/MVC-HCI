from flask import Flask, render_template, request, redirect, flash
import models

app = Flask(__name__)
app.secret_key = "12345"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
models.init_db()

@app.route("/")
def index():
    search = request.args.get("search")
    category = request.args.get("category")
    notes = models.get_all_notes(search, category)
    return render_template("index.html", notes=notes, search=search, category=category)

@app.route("/create", methods=["GET", "POST"])
def create():
    categories = ["Work", "Personal", "Ideas", "Other"]
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        category = request.form.get("category")
        if not title or not content:
            flash("Both title and content are required!", "error")
            return redirect("/create")
        models.create_note(title, content, category)
        flash("Note created successfully!", "success")
        return redirect("/")
    return render_template("create.html", categories=categories)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    note = models.get_note(id)
    categories = ["Work", "Personal", "Ideas", "Other"]
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        category = request.form.get("category")
        if not title or not content:
            flash("Both fields are required!", "error")
            return redirect(f"/edit/{id}")
        models.update_note(id, title, content, category)
        flash("Note updated successfully!", "success")
        return redirect("/")
    return render_template("edit.html", note=note, categories=categories)

@app.route("/delete/<int:id>")
def delete(id):
    models.delete_note(id)
    flash("Note deleted!", "success")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
