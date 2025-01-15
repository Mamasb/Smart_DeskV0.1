from app import db

class Textbook(db.Model):
    """
    Represents textbooks for students.
    """
    __tablename__ = 'textbooks'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    book_title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    student = db.relationship('Student', backref=db.backref('textbooks', lazy=True))

    def __repr__(self):
        return f"<Textbook(id={self.id}, student_id={self.student_id}, book_title={self.book_title}, price={self.price})>"
