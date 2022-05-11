from locust import SequentialTaskSet, task, HttpUser, constant, tag;

auth_header = {
    'x-propertyware-system-id':  '182255624',
    'x-propertyware-client-id': '0af3cd28-fec2-4db0-87fb-26fa10b3671e',
    'x-propertyware-client-secret': 'b033363a-f97f-4957-9839-9eb5c28ed9ff'
    }

class Seq(SequentialTaskSet):

    @tag('leases')
    @task
    def get_leases(self):
        response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/leases',
            headers=auth_header
        )
        print("leases")

    @tag('portfolios')
    @task
    def get_portfolios(self):
        response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/portfolios',
            headers=auth_header
        )
        print("portfolios")

class LoggedInUser(HttpUser):
    host = "https://sat.propertyware.com"
    tasks = [Seq]
    wait_time = constant(1)
