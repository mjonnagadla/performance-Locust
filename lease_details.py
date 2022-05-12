#Accessing Lease details API with grouping - using name parameter
from locust import TaskSet, task, HttpUser, constant, task;
import csv;

auth_header = {
    'x-propertyware-system-id':  '182255624',
    'x-propertyware-client-id': '0af3cd28-fec2-4db0-87fb-26fa10b3671e',
    'x-propertyware-client-secret': 'b033363a-f97f-4957-9839-9eb5c28ed9ff'
    }

#leaseIDs = [3214737414,3144384512,3144351748,3222503426,3222306816]

file = open("./data/leases.csv")
csvreader = csv.reader(file)
fields =[]
fields = next(csvreader)

class LeaseDetails(TaskSet):
    
    @task
    def get_leases(self):
        for i in fields:
         id = int(i)
         response = self.client.request(
         method='GET',
         url='/pw/api/rest/v1/leases/%i'  % id, name='/leases/leaseID',
         headers=auth_header
         )
         print("leaseID ",id,response)
        

class LoggedInUser(HttpUser):
    host = "https://sat.propertyware.com"
    tasks = [LeaseDetails]
    wait_time = constant(1)

file.close()