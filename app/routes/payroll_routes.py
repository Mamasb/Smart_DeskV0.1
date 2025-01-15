from flask import Blueprint, render_template, request
from app.models.finance.payroll import Payroll
from app import db


bp = Blueprint('payroll_routes', __name__)

@bp.route('/payroll')
def payroll():
    payrolls = Payroll.query.all()
    return render_template('finance/payroll.html', payrolls=payrolls)

@bp.route('/add_payroll', methods=['GET', 'POST'])
def add_payroll():
    if request.method == 'POST':
        staff_id = request.form['staff_id']
        salary_amount = request.form['salary_amount']
        date_of_payment = request.form['date_of_payment']
        
        new_payroll = Payroll(staff_id=staff_id, salary_amount=salary_amount, date_of_payment=date_of_payment)
        db.session.add(new_payroll)
        db.session.commit()
        return redirect(url_for('payroll_routes.payroll'))
    return render_template('finance/add_payroll.html')
