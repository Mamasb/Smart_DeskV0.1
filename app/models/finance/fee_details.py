from app import db

class FeeDetails(db.Model):
    """
    Represents the details of a fee breakdown.
    """
    __tablename__ = 'fee_details'
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer, primary_key=True)
    fee_id = db.Column(db.Integer, db.ForeignKey('fees.id'), nullable=False)
    fee_value = db.Column(db.Float, nullable=False)
    fee_description = db.Column(db.String(200), nullable=True)
    
    fee = db.relationship('Fee', backref=db.backref('fee_details', lazy=True))

    def __repr__(self):
        return f"<FeeDetails(id={self.id}, fee_value={self.fee_value}, fee_description={self.fee_description})>"
