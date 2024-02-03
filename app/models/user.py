from app.models.db import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    nickname = db.Column(db.String(50))

    # Add any other user-related fields as needed

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, name={self.name}, surname={self.surname}, nickname={self.nickname})>"

    # TODO: For the one implementing the USER Service : Implement CRUD and other stuff.
