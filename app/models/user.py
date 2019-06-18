from app import db

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        if user:
            return user
    
    @classmethod
    def find_by_id(cls, _id):
        user = cls.query.filter_by(id=_id).first()
        if user:
            return user

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def json(self):
        return {
            "id": self.id,
            "username": self.username
            }