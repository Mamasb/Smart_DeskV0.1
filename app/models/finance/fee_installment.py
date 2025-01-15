from app import db

class FeeInstallment(db.Model):
    """
    Represents an installment for a fee payment.
    """
    __tablename__ = 'fee_installments'
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer, primary_key=True)
    fee_id = db.Column(db.Integer, db.ForeignKey('fees.id'), nullable=False)
    installment_amount = db.Column(db.Float, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    
    fee = db.relationship('Fee', backref=db.backref('fee_installments', lazy=True))

    def __repr__(self):
        return f"<FeeInstallment(id={self.id}, installment_amount={self.installment_amount}, due_date={self.due_date})>"
