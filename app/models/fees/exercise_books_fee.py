from app import db

class ExerciseBooksFee(db.Model):
    """
    Represents fees for exercise books.
    """
    __tablename__ = 'exercise_books_fees'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"<ExerciseBooksFee(id={self.id}, amount={self.amount})>"
