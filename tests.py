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
        resp_post = self.app.post('/task/add', data={"label": "siema","task_desc": "elo", "end_time":"190039433"}, headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/x-www-form-urlencoded"})
        response = self.app.get('/task/get/all', headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/json"})
        data = json.loads(response.get_data().decode(sys.getdefaultencoding()))
        self.assertEqual(len(data), 1)

    def test_getting_labels(self):
        resp_post = self.app.post('/task/add', data={"label": "siema","task_desc": "elo",  "end_time":"190039433"}, headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/x-www-form-urlencoded"})
        response = self.app.get('/task/lables', headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/json"})
        data = json.loads(response.get_data().decode(sys.getdefaultencoding()))
        self.assertEqual(data[0], 'siema')

    def test_mark_as_done(self):
        resp_post = self.app.post('/task/add', data={"label": "siema","task_desc": "elo", "end_time":"1904039433"}, headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/x-www-form-urlencoded"})
        respom = self.app.get('/task/mark/oposite/1', headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/json"})
        response = self.app.get('/task/get/all', headers={"Authorization": "Bearer {}".format(self.access_token),                                                   "Content-Type": "application/json"})
        data = json.loads(response.get_data().decode(sys.getdefaultencoding()))
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(True, data[0]['is_done'])

    def test_delete(self):
        resp_post = self.app.post('/task/add', data={"label": "siema","task_desc": "elo",  "end_time":"190039433"}, headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/x-www-form-urlencoded"})
        responses = self.app.delete('/task/delete/1', headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/json"})
        response = self.app.get('/task/get/all', headers={"Authorization": "Bearer {}".format(self.access_token),"Content-Type": "application/json"})
        data = json.loads(response.get_data().decode(sys.getdefaultencoding()))
        self.assertEqual(data, [])

    def test_update(self):
        resp_post = self.app.post('/task/add', data={"label": "siema","task_desc": "elo",  "end_time":"190039433"}, headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/x-www-form-urlencoded"})
        update_rsp = self.app.post('/task/update', data={"id":"1", "label": "sieghmera","task_desc": "eerfghlo", "is_done":"False",  "end_time":"190039433"}, headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/x-www-form-urlencoded"})
        response = self.app.get('/task/get/all', headers={"Authorization": "Bearer {}".format(self.access_token),"Content-Type": "application/json"})
        data = json.loads(response.get_data().decode(sys.getdefaultencoding()))
        self.assertEqual(data[0]['label'], "sieghmera")

    def test_habit_adding(self):
        resp_post = self.app.post('/habit/add', data={"habit_desc": "elo",  'reset_24h':"True"}, headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/x-www-form-urlencoded"})
        response = self.app.get('/habit/get/all', headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/json"})
        data = json.loads(response.get_data().decode(sys.getdefaultencoding()))
        self.assertEqual(len(data), 1)

    def test_habit_mark(self):
        resp_post = self.app.post('/habit/add', data={"habit_desc": "elo",  'reset_24h':"True"}, headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/x-www-form-urlencoded"})
        response = self.app.get('/habit/get/all', headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/json"})
        respom = self.app.get('/habit/mark/1', headers={"Authorization": "Bearer {}".format(self.access_token),"Content-Type": "application/json"})
        response = self.app.get('/habit/get/all', headers = {"Authorization":"Bearer {}".format(self.access_token), "Content-Type":"application/json"})
        data = json.loads(response.get_data().decode(sys.getdefaultencoding()))
        self.assertEqual(len(data), 0)

if __name__ == '__main__':
    unittest.main()