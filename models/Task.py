from config import db

class RegularTask(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    label = db.Column(db.String(120), nullable=False)
    task_desc = db.Column(db.String(400), nullable=False)
    time_created = db.Column(db.DateTime(), nullable=False)
    end_time = db.Column(db.DateTime())
    is_done = db.Column(db.Boolean(), nullable=False)

    def save_task(self):
        ses = db.session
        ses.add(self)
        ses.commit()

    @classmethod
    def get_task_by_user(cls, username):
        return list(map(lambda x: x.serialize,cls.query.filter_by(username = username).all()))

    @classmethod
    def get_task_by_user_and_id(cls, username, id):
        return cls.query.filter_by(username = username, id = id).first()

    def mark_as_done(self):
        self.is_done=not self.is_done
        db.session.commit()

    def delete_task(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @property
    def serialize(self):
       return {
           'id': self.id,
           'label':self.label,
           'task_desc': self.task_desc,
           'username': self.username,
           'is_done': self.is_done,
           'time_created': self.time_created.isoformat(),
           'end_time': self.end_time.isoformat()
       }