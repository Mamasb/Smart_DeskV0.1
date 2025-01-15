# app/models/finance.py
from app import db  # Import the db instance

class Fee(db.Model):
    __tablename__ = 'fees'
    
    # Define the columns for the fees table
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)  # Optional description
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Auto set timestamp when created

    # Optionally add more fields as needed
    # e.g., for payments or other attributes related to fees
    # payment_status = db.Column(db.String(50), nullable=False, default='Pending')

    def __repr__(self):
        return f"<Fee {self.id}: {self.amount}>"
