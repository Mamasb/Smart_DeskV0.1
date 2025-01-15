from app import db

class AssessmentTool(db.Model):
    """
    Represents an assessment tool used in the school system.
    """
    __tablename__ = 'assessment_tools'

    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price_per_use = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<AssessmentTool(id={self.id}, tool_name={self.tool_name}, price_per_use={self.price_per_use})>"
