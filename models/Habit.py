from config import db
from datetime import datetime
from datetime import timedelta

class Habit(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    habit_desc = db.Column(db.String(400), nullable=False)
    time_created = db.Column(db.DateTime(), nullable=False)
    time_done = db.Column(db.DateTime())
    next_reset_time = db.Column(db.DateTime())
    is_daily_done = db.Column(db.Boolean(), nullable=False)
    reset_24h = db.Column(db.Boolean(), nullable=False)

    def save_habit(self):
        ses = db.session
        ses.add(self)
        ses.commit()

    def mark_as_daily_done(self):
        self.is_daily_done = True
        self.time_done = datetime.now()
        if(self.reset_24h):
            self.next_reset_time = self.time_done + timedelta(days=1)
        else:
            self.next_reset_time = self.time_done.replace(hour=23, minute=59, second=59)
        self.update_habit()

    @classmethod
    def get_habit_by_user(cls, username):
        cls.check_to_reste()
        return list(map(lambda x: x.serialize,cls.query.filter_by(username = username, is_daily_done = False).all()))

    @classmethod
    def get_habit_by_user_and_id(cls, username, id):
        return cls.query.filter_by(username = username, id = id).first()

    def delete_habit(self):
        db.session.delete(self)
        db.session.commit()

    def update_habit(self):
        db.session.commit()

    def check_to_reste(self, username):
        habit_list = list(self.query.filter_by(username=username, is_daily_done=False).all())
        for habit in habit_list:
            if(habit.next_reset_time <= datetime.now()):
                habit.is_daily_done = False
                habit.update_habit()

    @property
    def serialize(self):
       return {
           'id': self.id,
           'habit_desc': self.habit_desc,
           'username': self.username,
           'is_daily_done': self.is_daily_done,
           'time_created': self.time_created.isoformat(),
           'time_done': None if not self.time_done else self.time_done.isoformat(),
           'next_reset_time': None if not self.next_reset_time else self.next_reset_time.isoformat(),
           'reset_24h':self.reset_24h
       }