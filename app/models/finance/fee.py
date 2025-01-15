from app import db

class Fee(db.Model):
    __tablename__ = 'fees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    amount = db.Column(db.Float)

    def __repr__(self):
        return f'<Fee {self.name}>'

class FeeDetails(db.Model):
    __tablename__ = 'fee_details'
    id = db.Column(db.Integer, primary_key=True)
    fee_id = db.Column(db.Integer, db.ForeignKey('fees.id'))
    description = db.Column(db.String(255))
    fee = db.relationship('Fee', backref='details')

    def __repr__(self):
        return f'<FeeDetail {self.description}>'

class FeeInstallment(db.Model):
    __tablename__ = 'fee_installments'
    id = db.Column(db.Integer, primary_key=True)
    fee_id = db.Column(db.Integer, db.ForeignKey('fees.id'))
    installment_amount = db.Column(db.Float)
    due_date = db.Column(db.Date)

    fee = db.relationship('Fee', backref='installments')

    def __repr__(self):
        return f'<FeeInstallment {self.due_date}>'
