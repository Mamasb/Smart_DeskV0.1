from app import db

class Payroll(db.Model):
    """
    Represents the payroll information for staff and teachers.
    """
    __tablename__ = 'payroll'

    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    salary_amount = db.Column(db.Float, nullable=False)
    date_of_payment = db.Column(db.Date, nullable=False)
    
    staff = db.relationship('Staff', backref=db.backref('payroll', lazy=True))

    def __repr__(self):
        return f"<Payroll(id={self.id}, staff_id={self.staff_id}, salary_amount={self.salary_amount}, date_of_payment={self.date_of_payment})>"
