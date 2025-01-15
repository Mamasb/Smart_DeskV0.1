class AdmissionFee(db.Model):
    __tablename__ = 'admission_fee'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def calculate_expected_amount(new_students):
        return new_students * self.amount

    def serialize(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'description': self.description,
        }
