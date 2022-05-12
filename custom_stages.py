"""
    A simply load test shape class that has different user and spawn_rate at
    different stages.

    Keyword arguments:

        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage
            stop_at_end -- Can be set to stop once all stages have run.
"""
from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape
from api import apiRequest

class UserTasks(TaskSet):
    @task
    def get_leases(self):
     apiRequest.getRequestData(self, '/pw/api/rest/v1/leases')

    @task
    def get_portfolios(self):
     apiRequest.getRequestData(self, '/pw/api/rest/v1/portfolios')

    @task
    def get_buildings(self):
     apiRequest.getRequestData(self, '/pw/api/rest/v1/buildings')

    @task
    def get_vendors(self):
     apiRequest.getRequestData(self, '/pw/api/rest/v1/vendors')

    @task
    def get_bills(self):
     apiRequest.getRequestData(self, '/pw/api/rest/v1/bills')

class WebsiteUser(HttpUser):
    host = "https://sat.propertyware.com"
    wait_time = constant(0.5)
    tasks = [UserTasks]

class StagesShape(LoadTestShape):

    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 10},
        {"duration": 100, "users": 50, "spawn_rate": 10},
        {"duration": 180, "users": 100, "spawn_rate": 10},
        {"duration": 220, "users": 30, "spawn_rate": 10},
        {"duration": 230, "users": 10, "spawn_rate": 10},
        {"duration": 240, "users": 1, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None