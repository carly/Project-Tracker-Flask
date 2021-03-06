from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/")
def add_new_student():
    """Homepage gives form to add a new student"""
    return render_template("student_add.html")

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""
    return render_template("student_search.html")

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    list_of_tuples = hackbright.list_of_project_grades(github)



    html = render_template("student_info.html", first=first, last=last, github=github, \
        list_of_tuples=list_of_tuples)
    return html

@app.route("/project")
def project_details():
    """Show the detailed information about a project"""
    title = request.args.get('project')
    title, description, max_grade = hackbright.get_project_by_title(title)

    html = render_template("/project.html", title=title, description=description, max_grade=max_grade)
    return html

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student"""
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    github = request.form.get('github')
    hackbright.make_new_student(firstname, lastname, github)
    return "The student information has been successfully added!"



if __name__ == "__main__":
    app.run(debug=True)