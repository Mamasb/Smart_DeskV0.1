from app import db

class SchoolExerciseBooks(db.Model):
    """
    Represents exercise books for a student.
    """
    __tablename__ = 'school_exercise_books'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    book_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    student = db.relationship('Student', backref=db.backref('school_exercise_books', lazy=True))

    def __repr__(self):
        return f"<SchoolExerciseBooks(id={self.id}, student_id={self.student_id}, book_name={self.book_name}, price={self.price})>"
