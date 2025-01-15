# app/routes/school_fee_routes.py

from flask import Blueprint, render_template, request, redirect, url_for
from app.models.misc.school_fee import SchoolFee
from app import db


bp = Blueprint('school_fee_routes', __name__)

@bp.route('/school_fees')
def school_fees():
    from app.models.misc import SchoolFee  # Import inside the route function
    school_fees = SchoolFee.query.all()
    return render_template('misc/school_fees.html', school_fees=school_fees)


@bp.route('/add_school_fee', methods=['GET', 'POST'])
def add_school_fee():
    if request.method == 'POST':
        student_id = request.form['student_id']
        fee_id = request.form['fee_id']
        fee_value = request.form['fee_value']
        
        new_school_fee = SchoolFee(student_id=student_id, fee_id=fee_id, fee_value=fee_value)
        db.session.add(new_school_fee)
        db.session.commit()
        return redirect(url_for('school_fee_routes.school_fees'))
    return render_template('misc/add_school_fee.html')
