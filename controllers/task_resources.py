from flask_restful import Resource, reqparse, request
from models.Task import RegularTask
import time
from datetime import datetime
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

req = reqparse.RequestParser()
req.add_argument('label', help = 'This field cannot be blank', required = True)
req.add_argument('task_desc', help = 'This field cannot be blank', required = True)
req.add_argument('end_time')

req_mark = reqparse.RequestParser()
req_mark.add_argument('id', help='This filed cannot be blank', required=True)

req2 = reqparse.RequestParser()
req2.add_argument('id', help = 'This field cannot be blank', required = True)
req2.add_argument('label', help = 'This field cannot be blank', required = True)
req2.add_argument('task_desc', help = 'This field cannot be blank', required = True)
req2.add_argument('end_time')

class AddTask(Resource):
    def post(self):
        data = req.parse_args()
        task = RegularTask(username = get_jwt_identity(),
                           label= data['label'],
                           task_desc = data['task_desc'],
                           end_time = datetime.fromtimestamp(123456789),
                           time_created = datetime.now(),
                           is_done=False)
        try:
            task.save_task()
            return {"Msg":"Task created."},200
        except Exception as ex:
            return {'Error': print(ex)}, 500


class GetTask(Resource):
    def get(self, task_id):
        return RegularTask.get_task_by_user_and_id(get_jwt_identity(), task_id).serialize


class GetTasks(Resource):
    def get(self):
        return RegularTask.get_task_by_user("teest2")

class GetTasksLabels(Resource):
    def get(self):
        sets = set()
        tasks = RegularTask.get_task_by_user("teest2")
        for task in tasks:
            sets.add(task['label'])
        return list(sets)

class UpdateTask(Resource):
    def post(self):
        data = req2.parse_args()
        task = RegularTask.get_task_by_user_and_id(data['id'])
        task.task_desc = data['task_desc']
        task.label = data['label']
        task.is_done = data['is_dona']
        task.end_time = datetime.now()
        task.commit()
        
class DeleteTask(Resource):
    def delete(self):
        data = req_mark.parse_args()
        task = RegularTask.get_task_by_user_and_id(get_jwt_identity(),data['id'])
        if task:
            task.delete_task()
            return {'Msg': 'Task deleted'}, 200
        else:
            return {'Msg': 'Task not found'}, 404

class MarkAsDoneTask(Resource):
    def post(self):
        data = req_mark.parse_args()
        task = RegularTask.get_task_by_user_and_id(get_jwt_identity(), data['id'])
        if task:
            task.mark_as_done()
            return {"Msg":"Task has been marked as True"}, 200
        else:
            return {'Msg': 'Task not found'}, 404
