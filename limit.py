#Accessing API with limit
from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape

auth_header = {
    'x-propertyware-system-id':  '182255624',
    'x-propertyware-client-id': '0af3cd28-fec2-4db0-87fb-26fa10b3671e',
    'x-propertyware-client-secret': 'b033363a-f97f-4957-9839-9eb5c28ed9ff'
    }

limits = [50,75,100]

class UserTasks(TaskSet):
    
    @task
    def get_leases(self):
        for i in limits:
         response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/leases?limit=%i'  % i,
            headers=auth_header
         )
         print(response)

    @task
    def get_portfolios(self):
        for i in limits:
         response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/portfolios?limit=%i'  % i,
            headers=auth_header
         )
         print(response)    

    @task
    def get_vendors(self):
        for i in limits:
         response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/vendors?limit=%i'  % i,
            headers=auth_header
         )
         print(response)  

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