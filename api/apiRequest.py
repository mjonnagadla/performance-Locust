import json


def getRequestData(self, apiCall):
    apiRequest = self.client.get(apiCall)
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
