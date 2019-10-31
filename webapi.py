import json
import requests

api_headers = {'identity': 'Group2', 'token': '2c55f846-e723-4564-b93c-35630007dd7a'}


def api_getUserID(username='marytan'):
    api_url = 'http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/customers/' + username
    response = requests.get(api_url, headers=api_headers)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data["customerId"]
    else:
        return None


def api_getCustomerDetails(customerId=2):
    api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/customers/{customerId}/details"
    response = requests.get(api_url, headers=api_headers)
    # {
    #     "customerId": "2",
    #     "gender": "Female",
    #     "firstName": "Hui Shan",
    #     "lastName": "Tan",
    #     "lastLogIn": "2019-01-29T18:00:00.000+0000",
    #     "dateOfBirth": "1992-03-25T00:00:00.000+0000"
    # }
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data
    else:
        return None


def api_getListOfDepositAccounts(customerId=2):
    api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/accounts/deposit/{customerId}"
    response = requests.get(api_url, headers=api_headers)
    # [
    #     {
    #         "accountId": 74,
    #         "type": "SAVINGS",
    #         "displayName": "POSB SAVINGS ACCOUNT",
    #         "accountNumber": "490723483"
    #     }
    # ]
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data
    else:
        return None

def api_getTransactionDetails(accountId=74):
    api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/transactions/{accountId}?from=01-01-2018&to=02-01-2019"
    response = requests.get(api_url, headers=api_headers)
# [
#     {
#         "transactionId": "119973fe-7d7b-494b-86cf-872c34b6780c",
#         "accountId": 74,
#         "type": "DEBIT",
#         "amount": "12.9",
#         "date": "2018-01-01T02:00:00.000+0000",
#         "tag": "TRANSPORT",
#         "referenceNumber": "789010165 FAST-TREK TRANSPORT"
#     }
# ]
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data
    else:
        return None

def  api_getAccountBalance(accountId):
    api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/accounts/deposit/{accountId}/balance?"
    response = requests.get(api_url, headers=api_headers)
    # {
    #     "availableBalance": "27354.91",
    #     "currency": "S$",
    #     "dateOfBalance": "2019-10-31T06:24:59.394+0000",
    #     "displayName": "POSB SAVINGS ACCOUNT",
    #     "accountNumber": "432262070",
    #     "accountType": "SAVINGS"
    # }
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data
    else:
        return None

def  api_getListOfCreditAccounts(customerId):
    api_url = f"http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/accounts/credit/{customerId}"
    response = requests.get(api_url, headers=api_headers)
    # [
    #     {
    #         "accountId": 106,
    #         "displayName": "VISA Platinum",
    #         "cardNumber": "1234-2345-3456-4567"
    #     },
    #     {
    #         "accountId": 206,
    #         "displayName": "DBS Altitude Visa Signature Card",
    #         "cardNumber": "1111-2222-3333-4444"
    #     }
    # ]
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data
    else:
        return None

