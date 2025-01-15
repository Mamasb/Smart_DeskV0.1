from flask import Blueprint, render_template, request, redirect, url_for
from app.models.finance.fee import Fee, FeeDetails, FeeInstallment
from app.models.misc.textbooks import Textbook  # Import Textbook if needed
from app import db

# Correctly initializing the Blueprint with 'bp' as the attribute
bp = Blueprint('accountant_routes', __name__)

@bp.route('/fees')
def fees():
    fees = Fee.query.all()  # Fetch all Fee records from the database
    return render_template('fees/fees.html', fees=fees)

@bp.route('/fee_details/<int:fee_id>')
def fee_details(fee_id):
    fee_details = FeeDetails.query.filter_by(fee_id=fee_id).all()  # Fetch FeeDetails for the given fee_id
    return render_template('fees/fee_details.html', fee_details=fee_details)

@bp.route('/fee_installments/<int:fee_id>')
def fee_installments(fee_id):
    installments = FeeInstallment.query.filter_by(fee_id=fee_id).all()  # Fetch FeeInstallments for the given fee_id
    return render_template('fees/fee_installments.html', installments=installments)
