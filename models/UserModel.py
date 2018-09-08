from data_base_config import db
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        print('user saved')

    @classmethod
    def find_by_username(self, username):
        return self.query.filter_by(username = username).first()
