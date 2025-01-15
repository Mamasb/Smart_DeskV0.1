from flask import Blueprint, render_template, request
from app.models.misc.school_fee import SchoolFee
from app.models.misc.new_student import NewStudent
from app import db


bp = Blueprint('invoice_routes', __name__)

@bp.route('/invoices')
def invoices():
    invoices = SchoolFee.query.all()
    return render_template('invoice/invoices.html', invoices=invoices)

@bp.route('/generate_invoice/<int:student_id>')
def generate_invoice(student_id):
    student_fees = SchoolFee.query.filter_by(student_id=student_id).all()
    return render_template('invoice/generate_invoice.html', student_fees=student_fees)
