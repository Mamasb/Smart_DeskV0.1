from flask import Blueprint, render_template, request
from app.models.fees import TuitionFee, AdmissionFee, FoodFee
from app import db


bp = Blueprint('fees_routes', __name__)

@bp.route('/tuition_fees')
def tuition_fees():
    tuition_fees = TuitionFee.query.all()
    return render_template('fees/tuition_fees.html', tuition_fees=tuition_fees)

@bp.route('/admission_fees')
def admission_fees():
    admission_fees = AdmissionFee.query.all()
    return render_template('fees/admission_fees.html', admission_fees=admission_fees)

@bp.route('/food_fees')
def food_fees():
    food_fees = FoodFee.query.all()
    return render_template('fees/food_fees.html', food_fees=food_fees)
