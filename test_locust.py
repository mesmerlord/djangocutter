import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

    @task
    def excercise(self):
        self.client.get("/excercises/")

    @task
    def sets(self):
        self.client.get("/sets/")
    
    @task
    def workout(self):
        self.client.get("/workouts/")