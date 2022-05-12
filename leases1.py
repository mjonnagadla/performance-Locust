# /leases/{leaseId}/contact
from locust import SequentialTaskSet, task, HttpUser, constant, tag;
import json

expected_code=200
auth_header = {
    'x-propertyware-system-id' : '171048968',
    'x-propertyware-client-id' : '026f8cd1-7017-46bd-8ec1-f5b5488dfa52',
    'x-propertyware-client-secret' : '3d5e2970-f074-4bfd-bfe3-25b23e8b609f'
    }

class LeaseRetrival(SequentialTaskSet):
    
    @tag('Lease Contact')
    @task(4)
    def get_leases(self):
        #file_handle=
        with self.client.get('/pw/api/rest/v1/leases/1783791624/contact', catch_response=True, headers=auth_header, name="/lease/contact") as response:
            if response.status_code == expected_code:
                print(response.text)
                print(response.status_code)
                print(type(response))
                print("Lease found in response and Request is success") 
                #converting the response string to python dictonary
                lease_contact_details=json.loads(response.text)
                #loading and converting the python dic to Json object 
                json_object=json.dumps(lease_contact_details, indent=4)
                print(json_object)

                # if response.status_code == expected_code and '244974235' in response.text and '244974236' in response.text:
                #     print("Contacts attached to the lease are found in response")
                #     if response.status_code == expected_code and '"type":"TENANT"' in response.text:
                #         print('Contact Type is also found in response')
                #         if response.status_code == expected_code and '"city":"Crystal Lake"' in response.text and '"billNumber":20' in response.text:
                #             print("Address city Found in response")
                #             print("Request is success for GET Lease contact")
            else:
                response.failure("Failed Request")
                        
        
class MyLoadTest(HttpUser):
    host = "https://sat.propertyware.com"
    tasks = [LeaseRetrival]
    wait_time = constant(1)
