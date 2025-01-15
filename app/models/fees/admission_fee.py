from app import db

class AdmissionFee(db.Model):
    """
    Represents admission-related fees for new students.
    """
    __tablename__ = 'admission_fees'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"<AdmissionFee(id={self.id}, amount={self.amount})>"
