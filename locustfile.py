from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_posts(self):
        self.client.get("/posts")

    @task
    def get_users(self):
        self.client.get("/users")
