"""
    A shape to imitate some specific user behaviour.
    First peak of users appear at time_limit/3 and
    second peak appears at 2*time_limit/3
    Settings:
        min_users -- minimum users
        peak_one_users -- users in first peak
        peak_two_users -- users in second peak
        time_limit -- total length of test
"""
import math
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


class DoubleWave(LoadTestShape):

    min_users = 20
    peak_one_users = 100
    peak_two_users = 75
    time_limit = 600

    def tick(self):
        run_time = round(self.get_run_time())

        if run_time < self.time_limit:
            user_count = (
                (self.peak_one_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 5) ** 2)
                + (self.peak_two_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 10) ** 2)
                + self.min_users
            )
            return (round(user_count), round(user_count))
        else:
            return None