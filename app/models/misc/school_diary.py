from app import db

class SchoolDiary(db.Model):
    """
    Represents the school diary for a student.
    """
    __tablename__ = 'school_diaries'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    diary_entry = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    student = db.relationship('Student', backref=db.backref('school_diaries', lazy=True))

    def __repr__(self):
        return f"<SchoolDiary(id={self.id}, student_id={self.student_id}, created_at={self.created_at})>"
