from flask import Flask
from flask_restful import Api
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api = Api(app)
from controllers import user_resources,task_resources, habits_resources

api.add_resource(user_resources.UserRegister, "/register")
api.add_resource(user_resources.UserLogin, "/login")
api.add_resource(user_resources.SecretTestResource, "/content")
api.add_resource(user_resources.TokenRefresh, "/token/refresh")
api.add_resource(user_resources.UserLogoutAccess, '/logout/access')
api.add_resource(user_resources.UserLogoutRefresh, '/logout/refresh')

api.add_resource(habits_resources.AddHabit, '/habit/add')
api.add_resource(habits_resources.GetAllHabitsToDone, '/habit/get/all')

api.add_resource(task_resources.AddTask, '/task/add')
api.add_resource(task_resources.GetTask, '/task/get/<task_id>')
api.add_resource(task_resources.GetTasks, '/task/get/all')
api.add_resource(task_resources.DeleteTask, '/task/delete/<task_id>')
api.add_resource(task_resources.UpdateTask, '/task/update')
api.add_resource(task_resources.GetTasksLabels, '/task/lables')
api.add_resource(task_resources.MarkAsDoneTask, '/task/mark/oposite/<task_id>')
if __name__ == "__main__":
    app.run()