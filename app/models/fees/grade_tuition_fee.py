from app import db

class GradeTuitionFee(db.Model):
    """
    Represents tuition fees for various grades.
    """
    __tablename__ = 'grade_tuition_fees'

    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"<GradeTuitionFee(id={self.id}, grade={self.grade}, amount={self.amount})>"
