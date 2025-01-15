from app import db

class TransportMode(db.Model):
    """
    Represents the modes of transport available for students.
    """
    __tablename__ = 'transport_modes'

    id = db.Column(db.Integer, primary_key=True)
    mode_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price_per_term = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<TransportMode(id={self.id}, mode_name={self.mode_name}, price_per_term={self.price_per_term})>"
