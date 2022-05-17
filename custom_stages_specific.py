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