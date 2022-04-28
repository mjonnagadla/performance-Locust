from locust import TaskSet, task, HttpUser, constant, task;

auth_header = {
    'x-propertyware-system-id':  '182255624',
    'x-propertyware-client-id': '0af3cd28-fec2-4db0-87fb-26fa10b3671e',
    'x-propertyware-client-secret': 'b033363a-f97f-4957-9839-9eb5c28ed9ff'
    }

class Leases(TaskSet):
    @task
    def get_leases(self):
        response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/leases',
            headers=auth_header
        )
        print(response)

class LoggedInUser(HttpUser):
    host = "https://sat.propertyware.com"
    tasks = [Leases]
    wait_time = constant(2)
