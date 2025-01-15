from app import db

class SchoolDiaryFee(db.Model):
    """
    Represents fees for school diaries.
    """
    __tablename__ = 'school_diary_fees'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"<SchoolDiaryFee(id={self.id}, amount={self.amount})>"
