from app import db

class NewStudent(db.Model):
    """
    Represents a new student enrolled in the school.
    """
    __tablename__ = 'new_students'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    registration_date = db.Column(db.Date, nullable=False)
    
    student = db.relationship('Student', backref=db.backref('new_students', lazy=True))

    def __repr__(self):
        return f"<NewStudent(id={self.id}, student_id={self.student_id}, registration_date={self.registration_date})>"
