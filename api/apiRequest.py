import json


def getRequestData(self, apiCall):
    headerCollection = {    
    'x-propertyware-system-id':  '182255624',
    'x-propertyware-client-id': '0af3cd28-fec2-4db0-87fb-26fa10b3671e',
    'x-propertyware-client-secret': 'b033363a-f97f-4957-9839-9eb5c28ed9ff'
    }
    apiRequest = self.client.get(apiCall, headers=headerCollection)
    print(apiRequest)
    apiData = apiRequest.text
    parse_json = json.loads(apiData)


def postRequestData(self, apiCall, testData, headers):
    apiRequest = self.client.post(apiCall, json=testData, headers=headers)
    apiData = apiRequest.text
    self.cookie = apiRequest.cookies
    parse_json = json.loads(apiData)


def postAPIRequestData(self, apiCall, testData):
    headerCollection = {
        "content-type": "application/json",
        "accept": "application/json",
        "X-XSRF-TOKEN": self.cookie["XSRF-TOKEN"],
        "XSRF-TOKEN": self.cookie["XSRF-TOKEN"]
    }
    apiRequest = self.client.post(
        apiCall, json=testData, headers=headerCollection)
    apiData = apiRequest.text
    parse_json = json.loads(apiData)
