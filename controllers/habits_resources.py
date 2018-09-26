from flask_restful import Resource, reqparse
from models.Habit import Habit
from datetime import datetime
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

req = reqparse.RequestParser()
req.add_argument('habit_desc', help = 'This field cannot be blank', required = True)
req.add_argument('reset_24h', help = 'This field cannot be blank', required = True)


class AddHabit(Resource):
    @jwt_required
    def post(self):
        data = req.parse_args()
        habit = Habit(habit_desc = data['habit_desc'],
                      username = get_jwt_identity(),
                      time_created = datetime.now(),
                      is_daily_done = False,
                      reset_24h = bool(data['reset_24h'])
                      )
        try:
            habit.save_habit()
            return {"Msg":"habit created."},200
        except Exception as ex:
            return {'Error': print(ex)}, 500

class GetAllHabitsToDone(Resource):
    @jwt_required
    def get(self):
       return Habit.get_habit_by_user(get_jwt_identity())