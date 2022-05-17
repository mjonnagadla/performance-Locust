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

auth_header = {
    'x-propertyware-system-id':  '182255624',
    'x-propertyware-client-id': '0af3cd28-fec2-4db0-87fb-26fa10b3671e',
    'x-propertyware-client-secret': 'b033363a-f97f-4957-9839-9eb5c28ed9ff'
    }

leaseIDs = [3214737414,3144384512,3144351748,3222503426,3222306816]
portfolioIDs = [2583363584,2580283392,1702363139,1773043713,1301839878]
buildingIDs = [2804908036,2419228677,2805006336,2801827840,1405255685]
vendorIDs = [231637780,2161606665,2559574031,2084896783,2764668935]
workorderIDs = [4015882241,4012015635,3998777344,3904799101,4014899204]

class UserTasks(TaskSet):

    @task
    def get_lease_details(self):
        for i in leaseIDs:
         response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/leases/%i'  % i, name='/leases/leaseID',
            headers=auth_header
         )
         print("leaseID ",i,response)

    @task
    def get_portfolio_details(self):
        for i in portfolioIDs:
         response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/portfolios/%i'  % i, name='/portfolios/portfolioID',
            headers=auth_header
         )
         print("portfolioID ",i,response)

    @task
    def get_building_details(self):
        for i in buildingIDs:
         response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/buildings/%i'  % i, name='/buildings/buildingID',
            headers=auth_header
         )
         print("buildingID ",i,response)

    @task
    def get_vendor_details(self):
        for i in vendorIDs:
         response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/vendors/%i'  % i, name='/vendors/vendorID',
            headers=auth_header
         )
         print("vendorID ",i,response)

    @task
    def get_workorder_details(self):
        for i in workorderIDs:
         response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/workorders/%i'  % i, name='/workorders/workorderID',
            headers=auth_header
         )
         print("workorderID ",i,response)


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