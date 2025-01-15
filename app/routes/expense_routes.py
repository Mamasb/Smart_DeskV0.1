from flask import Blueprint, render_template, request, redirect, url_for
from app.models.misc.expense import Expense
from app import db

bp = Blueprint('expense_routes', __name__)

@bp.route('/expenses')
def expenses():
    expenses = Expense.query.all()
    return render_template('misc/expenses.html', expenses=expenses)

@bp.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        expense_type = request.form['expense_type']
        
        # Basic validation
        if not description or not amount or not expense_type:
            return render_template('misc/add_expense.html', error="All fields are required.")
        
        try:
            amount = float(amount)  # Convert amount to float
        except ValueError:
            return render_template('misc/add_expense.html', error="Invalid amount entered.")
        
        # Create and save the expense
        new_expense = Expense(description=description, amount=amount, expense_type=expense_type)
        db.session.add(new_expense)
        db.session.commit()
        
        # Redirect to the expenses page after successful addition
        return redirect(url_for('expense_routes.expenses'))
    
    return render_template('misc/add_expense.html')
