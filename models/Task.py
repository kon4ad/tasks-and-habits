from config import db

class RegularTask(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    label = db.Column(db.String(120), nullable=False)
    task_desc = db.Column(db.String(400), nullable=False)
    time_created = db.Colmun(db.DateTime(), nullable=False)
    end_time = db.Column(db.DateTime())
    is_done = db.Column(db.Boolean(), nullable=False)

    def save_task(self):
        ses = db.session
        ses.add(self)
        ses.commit()

    @classmethod
    def get_task_by_user(cls, username):
        return cls.query.filter_by(username = username).all()