from locust import HttpUser, between, task
import random


class UserBehavior(HttpUser):
    wait_time = between(5, 9)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scooters_serial = ['{{serialnumber_1}}', '{{serialnumber_2}}', '{{serialnumber_3}}']

    def on_start(self):
        print('Now Shooting API')

    @task(1)
    def index(self):
        self.usertoken = 'Bearer {{token}}'
        self.headers = {'Authorization': self.usertoken}
        self.url = '{{end point}}' + random.choice(self.scooters_serial)
        self.client.get(url=self.url, headers=self.headers)