from locust import TaskSet, task, HttpUser, constant, task;

auth_header = {
    'x-propertyware-system-id':  '182255624',
    'x-propertyware-client-id': '0af3cd28-fec2-4db0-87fb-26fa10b3671e',
    'x-propertyware-client-secret': 'b033363a-f97f-4957-9839-9eb5c28ed9ff'
    }

class Building(TaskSet):
    
    @task(1)
    def get_buildings(self):
        response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/buildings',
            headers=auth_header
        )
        print("Buildings fetched",response)

class LoggedInUser(HttpUser):
    host = "https://sat.propertyware.com"
    tasks = [Building]
    wait_time = constant(1)