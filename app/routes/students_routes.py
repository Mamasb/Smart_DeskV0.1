from flask import Blueprint, render_template, request
from app.models.personnel import Student
from app import db


bp = Blueprint('students_routes ', __name__)

@bp.route('/students')
def students():
    students = Student.query.all()
    return render_template('personnel/students.html', students=students)

@bp.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        student = Student(name=name, grade=grade)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('students_routes.students'))
    return render_template('personnel/add_student.html')
