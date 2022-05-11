from locust import TaskSet, task, HttpUser, constant, task;
from api import apiRequest

class Leases(TaskSet):
    @task
    def get_leases(self):
        apiRequest.getRequestData(self, '/pw/api/rest/v1/leases')

class LoggedInUser(HttpUser):
    host = "https://sat.propertyware.com"
    tasks = [Leases]
    wait_time = constant(2)
