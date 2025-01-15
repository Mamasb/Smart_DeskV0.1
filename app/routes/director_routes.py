from flask import Blueprint, render_template, request
from app.models.personnel.manager import Manager
from app.models.personnel.teacher import Teacher
from app.models.personnel.staff import Staff

from app import db

# Create blueprint object 'bp'
bp = Blueprint('director_routes', __name__)

@bp.route('/staff')
def staff():
    staff_members = Staff.query.all()
    return render_template('personnel/staff.html', staff_members=staff_members)

@bp.route('/teachers')
def teachers():
    teachers = Teacher.query.all()
    return render_template('personnel/teachers.html', teachers=teachers)

@bp.route('/managers')
def managers():
    managers = Manager.query.all()
    return render_template('personnel/managers.html', managers=managers)
