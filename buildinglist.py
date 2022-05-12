from locust import TaskSet, task, HttpUser, constant, task;

auth_header = {
    'x-propertyware-system-id':  '182255624',
    'x-propertyware-client-id': '0af3cd28-fec2-4db0-87fb-26fa10b3671e',
    'x-propertyware-client-secret': 'b033363a-f97f-4957-9839-9eb5c28ed9ff'
    }
#passing building ID's using list
list=[2805006336,2804908036,2419228677]

class Building(TaskSet):
    
    @task(1)
    def get_buildingId(self):
        for i in list:
            response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/buildings/%i' %i,
            headers=auth_header
        )
        print("Buildingid",response,i)

class LoggedInUser(HttpUser):
    host = "https://sat.propertyware.com"
    tasks = [Building]
    wait_time = constant(2)