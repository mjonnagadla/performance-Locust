from locust import TaskSet, task, constant, tag, HttpUser;

auth_header = {
    'x-propertyware-system-id':  '182255624',
    'x-propertyware-client-id': '0af3cd28-fec2-4db0-87fb-26fa10b3671e',
    'x-propertyware-client-secret': 'b033363a-f97f-4957-9839-9eb5c28ed9ff'
    }

class Seq(TaskSet):

    def on_start(self):
        self.client.get('/pw/home/home.do', headers=auth_header, name="/homepage")

    @tag('leases')
    @task(3)
    def get_leases(self):
        response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/leases',
            headers=auth_header
        )
        print("leases")

    @tag('portfolios')
    @task(1)
    def get_portfolios(self):
        response = self.client.request(
            method='GET',
            url='/pw/api/rest/v1/portfolios',
            headers=auth_header
        )
        print("portfolios")
    
    def on_stop(self):
        self.client.get('/pw/login.jsp', headers=auth_header, name="/loginpage")

class LoggedInUser(HttpUser):
    host = "https://sat.propertyware.com"
    tasks = [Seq]
    wait_time = constant(1)


