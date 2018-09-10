import os
import unittest
import tempfile
import run
import json
import sys
import config
class FlaskrTestCase(unittest.TestCase):
    username = 'test1'
    password = 'test1'

    def setUp(self):
        run.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_test.db'
        self.app = run.app.test_client()
        config.db.create_all()
        response = self.app.post('/register', data = {'username': self.username, 'password':self.username})
        self.access_token = json.loads(response.get_data().decode(sys.getdefaultencoding()))['access_token']

    def tearDown(self):
        run.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
        os.remove('app_test.db')

    def test_check_empty_db(self):
        response = self.app.get('/task/get/all', headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/json"})
        data = json.loads(response.get_data().decode(sys.getdefaultencoding()))
        self.assertEqual(data, [])

    def test_adding_new_task(self):
        resp_post = self.app.post('/task/add', data={"label": "siema","task_desc": "elo"}, headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/x-www-form-urlencoded"})
        response = self.app.get('/task/get/all', headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/json"})
        data = json.loads(response.get_data().decode(sys.getdefaultencoding()))
        self.assertEqual(len(data), 1)



if __name__ == '__main__':
    unittest.main()