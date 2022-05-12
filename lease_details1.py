#Accessing Lease details API without grouping
from locust import TaskSet, task, HttpUser, constant, task;

auth_header = {
    'x-propertyware-system-id':  '182255624',
    'x-propertyware-client-id': '0af3cd28-fec2-4db0-87fb-26fa10b3671e',
    'x-propertyware-client-secret': 'b033363a-f97f-4957-9839-9eb5c28ed9ff'
    }

leaseIDs = [3214737414,3144384512,3144351748,3222503426,3222306816]

class LeaseDetails1(TaskSet):
    
    @task
    def get_leases(self):
        for i in leaseIDs:
         response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/leases/%i'  % i,
            headers=auth_header
         )
         print("leaseID ",i,response)
        

class LoggedInUser(HttpUser):
    host = "https://sat.propertyware.com"
    tasks = [LeaseDetails1]
    wait_time = constant(1)