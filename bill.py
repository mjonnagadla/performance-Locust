from locust import SequentialTaskSet, task, HttpUser, constant, tag;
import json, _json;

expected_code=200
auth_header = {
    'x-propertyware-system-id':  '182255624',
    'x-propertyware-client-id': '0af3cd28-fec2-4db0-87fb-26fa10b3671e',
    'x-propertyware-client-secret': 'b033363a-f97f-4957-9839-9eb5c28ed9ff'
    }

class BillRetrival(SequentialTaskSet):
    
    @tag('Bills')
    @task(1)
    def get_leases(self):
        with self.client.get('/pw/api/rest/v1/bills', catch_response=True, headers=auth_header) as response:
            if response.status_code == expected_code and "id" in response.text and "vendorID" in response.text:
                print(response.text)
                print(response.status_code)
                print("portfolio found in response and Request is success")       
                if response.status_code == expected_code and '228295017' in response.text:
                    print("vendor id is found in response")
                    if response.status_code == expected_code and '"portfolioID":228295017' in response.text:
                        print('Portfolio Id is also found in response')
                        if response.status_code == expected_code and '"billNumber":21' in response.text and '"billNumber":20' in response.text:
                            print("Specific Bill Number Found in response")
                            print("Request is success for GET Bills")
            else:
                response.failure("Failed Request")
                        

    @tag("Bill Payment")
    @task(4)
    def get_portfolios(self):
        with self.client.get('/pw/api/rest/v1/bills/payments', catch_response=True, headers=auth_header) as response:
            if response.status_code == expected_code and "id" in response.text:
                print(response.text)
                print(response.status_code)
                print("Payments found in response and Request is success")       
                if response.status_code == expected_code and '"id":266181991' in response.text:
                    print("vendor id is found in response")
                    if response.status_code == expected_code and '"portfolioID":228295008' in response.text:
                        print('Portfolio Id is also found in response')
                        if response.status_code == expected_code and '"billDate":"2014-01-09"' in response.text and '"billNumber":20' in response.text:
                            print("Specific Bill date Found in response")
                            print("Request is success for GET Bills")
            else:
                response.failure("Failed Request")
        
class MyLoadTest(HttpUser):
    host = "https://sat.propertyware.com"
    tasks = [BillRetrival]
    wait_time = constant(1)
