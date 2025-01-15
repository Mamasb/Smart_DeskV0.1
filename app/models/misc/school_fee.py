from app import db



class SchoolFee(db.Model):
    __tablename__ = 'school_fees'
    __table_args__ = {'extend_existing': True}  # Add this line to allow redefining

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    fee_id = db.Column(db.Integer, db.ForeignKey('fees.id'), nullable=False)
    fee_value = db.Column(db.Float, nullable=False)

    student = db.relationship('Student', backref=db.backref('school_fees', lazy=True))
    fee = db.relationship('Fee', backref=db.backref('school_fees', lazy=True))

    def __repr__(self):
        return f"<SchoolFee(id={self.id}, student_id={self.student_id}, fee_value={self.fee_value})>"
