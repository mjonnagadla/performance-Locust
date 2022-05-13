from locust import TaskSet, task, HttpUser, constant, task;

auth_header = {
    'x-propertyware-system-id':  '182255624',
    'x-propertyware-client-id': '0af3cd28-fec2-4db0-87fb-26fa10b3671e',
    'x-propertyware-client-secret': 'b033363a-f97f-4957-9839-9eb5c28ed9ff'
    }

class Sample(TaskSet):
    
    @task(1)
    def get_vendor(self):
        response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/vendors',
            headers=auth_header
        )
        print("vendors")

    @task(4)
    def get_vendorID(self):
        response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/vendors/259031178',
            headers=auth_header
        )
        print("portfolios")

class LoggedInUser(HttpUser):
    host = "https://sat.propertyware.com"
    tasks = [Sample]
    wait_time = constant(1)
