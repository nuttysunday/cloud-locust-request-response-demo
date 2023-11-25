from locust import HttpUser, task, between
import time

class MyUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def my_task(self):
        self.client.get("/your-endpoint")