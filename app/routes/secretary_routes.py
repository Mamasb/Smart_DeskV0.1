from flask import Blueprint, render_template
from app.models.personnel.student import Student

from app.models.personnel.staff import Staff


from app import db


bp = Blueprint('secretary_routes', __name__)

@bp.route('/students')
def students():
    students = Student.query.all()
    return render_template('personnel/students.html', students=students)

@bp.route('/staff')
def staff():
    staff_members = Staff.query.all()
    return render_template('personnel/staff.html', staff_members=staff_members)
