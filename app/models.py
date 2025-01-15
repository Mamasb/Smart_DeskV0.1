from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db  # Import the SQLAlchemy instance from __init__.py

# Association Tables for optional fees
student_food = db.Table('student_food',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('foodfee_id', db.Integer, db.ForeignKey('food_fees.id'), primary_key=True)
)

student_transport = db.Table('student_transport',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('transportfee_id', db.Integer, db.ForeignKey('transport_fees.id'), primary_key=True)
)


# Invoice Model: Represents invoices for students
class Invoice(db.Model):
    __tablename__ = "invoices"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    amount_due = db.Column(db.Float, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    paid_date = db.Column(db.Date, nullable=True)

    student = db.relationship('Student', back_populates='invoices')

    def __repr__(self):
        return f"<Invoice {self.id} for {self.student.first_name} {self.student.family_name}>"


# Payment Model: Represents a payment made by a student
class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    amount_paid = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    payment_method = db.Column(db.String(50), nullable=True)

    student = db.relationship('Student', back_populates='payments')

    def __repr__(self):
        return f"<Payment {self.id} for {self.student.first_name} {self.student.family_name}>"


# Function to generate the next admission number
def generate_admission_number():
    latest_student = db.session.query(Student).order_by(Student.admission_number.desc()).first()

    if latest_student:
        last_number = int(latest_student.admission_number[3:])
        next_number = last_number + 1
        new_admission_number = f"AJA{next_number}"
    else:
        new_admission_number = "AJA1"
    
    return new_admission_number


# FeeStructure Model: Stores fee structure based on grade
class FeeStructure(db.Model):
    __tablename__ = 'fee_structures'
    
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(50), nullable=False)
    tuition_fee = db.Column(db.Float, nullable=False)
    text_books_fee = db.Column(db.Float, nullable=True)
    exercise_books_fee = db.Column(db.Float, nullable=True)
    assesment_tool_fee = db.Column(db.Float, nullable=True)
    school_diary = db.Column(db.Float, nullable=False)
    activity_fees = db.Column(db.Float, nullable=True)

    students = db.relationship('Student', back_populates='fee_structure')

    def __repr__(self):
        return f'<FeeStructure {self.grade}>'


# FoodFee Model
class FoodFee(db.Model):
    __tablename__ = 'food_fees'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    fee = db.Column(db.Float, nullable=False)

    # Relationship with Student through the association table
    students = db.relationship('Student', secondary=student_food, 
                               primaryjoin="FoodFee.id==student_food.c.foodfee_id", 
                               secondaryjoin="student_food.c.student_id==Student.id", 
                               back_populates='food_fees')

    def __repr__(self):
        return f'<FoodFee {self.item}>'




# TransportFee Model (Assuming you have it)
class TransportFee(db.Model):
    __tablename__ = 'transport_fees'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    fee = db.Column(db.Float, nullable=False)

    # Relationship with Student through the association table
    students = db.relationship('Student', secondary=student_transport, 
                               primaryjoin="TransportFee.id==student_transport.c.transportfee_id", 
                               secondaryjoin="student_transport.c.student_id==Student.id", 
                               back_populates='transport_fees')

    def __repr__(self):
        return f'<TransportFee {self.item}>'

class Food(db.Model):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    fee = db.Column(db.Float, nullable=False)

    # Define the relationship with the students table via the association table
    students = db.relationship('Student', secondary='student_food', 
                               back_populates='food_fees')

    def __repr__(self):
        return f'<Food {self.name}>'


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    admission_number = db.Column(db.String(50), unique=True, nullable=False, default=generate_admission_number)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=True)
    family_name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(50), nullable=False)

    # Optional Fees
    food = db.Column(db.Boolean, default=False, nullable=False)
    transport_mode = db.Column(db.String(50), nullable=True)

    # Foreign Key Relationships for optional fees
    food_id = db.Column(db.Integer, db.ForeignKey('food_fees.id'), nullable=True)
    transport_fee_id = db.Column(db.Integer, db.ForeignKey('transport_fees.id'), nullable=True)

    # Compulsory Fees
    tuition_fee = db.Column(db.Float, default=0, nullable=False)
    text_books_fee = db.Column(db.Float, default=0, nullable=False)
    exercise_books_fee = db.Column(db.Float, default=0, nullable=False)
    assessment_tool_fee = db.Column(db.Float, default=0, nullable=False)
    activity_fees = db.Column(db.Float, default=0, nullable=False)
    school_diary = db.Column(db.Float, default=0, nullable=False)

    # Financial Fields
    total_fee = db.Column(db.Float, default=0, nullable=False)
    fees_paid = db.Column(db.Float, default=0, nullable=False)
    balance = db.Column(db.Float, default=0, nullable=False)

    is_active = db.Column(db.Boolean, default=True, nullable=False)

    # Foreign Key Relationships for fee structure
    fee_structure_id = db.Column(db.Integer, db.ForeignKey('fee_structures.id'), nullable=True)

    # Relationships
    invoices = db.relationship('Invoice', back_populates='student')
    fee_structure = db.relationship('FeeStructure', back_populates='students')

    # Relationship to food fees through the association table
    food_fees = db.relationship('Food', secondary='student_food', 
                                back_populates='students')

    # Relationship to transport fees through the association table
    transport_fees = db.relationship('TransportFee', secondary='student_transport', 
                                     back_populates='students')

    # Add the payments relationship to Student
    payments = db.relationship('Payment', back_populates='student')

    def __repr__(self):
        return f"<Student {self.first_name} {self.family_name}, Grade: {self.grade}>"

    def calculate_total_fee(self):
        """Calculates the total fee for the student based on grade and optional fees."""
        if not self.fee_structure:
            return 0

        total_fee = self.fee_structure.tuition_fee + self.fee_structure.text_books_fee + \
                    self.fee_structure.exercise_books_fee + self.fee_structure.assessment_tool_fee + \
                    self.fee_structure.activity_fees + self.fee_structure.school_diary

        if self.food and self.food_fees:
            total_fee += sum(fee.fee for fee in self.food_fees)
        if self.transport_mode and self.transport_fees:
            total_fee += sum(fee.fee for fee in self.transport_fees)

        return total_fee

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(6), nullable=False)  # 'Debit' or 'Credit'
    transaction_date = db.Column(db.DateTime, default=datetime.utcnow)

def create_tables():
    db.create_all()
