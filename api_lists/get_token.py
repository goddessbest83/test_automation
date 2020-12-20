import requests
import json


def get_xingxing_user_token(app_token, conf, a_address, doc):
    # get user token
    header = {'Content-Type': 'application/json', 'Authorization': app_token}
    user_token_endpoint = conf['api_list']['-get_user_token']
    get_user_token_url = a_address + user_token_endpoint
    user_token_data = {'userId': doc['account_id'], 'password': doc['account_pass']}
    user_token_response = requests.post(url=get_user_token_url, headers=header, data=json.dumps(user_token_data))
    user_token_response_json = user_token_response.json()
    user_token = user_token_response_json['accessToken']

    return user_token


def get_tms_token(conf, a_address, doc):
    # get tms token
    header = {'Content-Type': 'application/json'}
    get_tms_token_endpoint = conf['api_list']['-get_tms_token']
    get_tms_token_url = a_address + get_tms_token_endpoint
    tms_token_data = {'userId': doc['tms_id'], 'password': doc['tms_pass']}
    tms_token_response = requests.post(url=get_tms_token_url, headers=header, data=json.dumps(tms_token_data))
    tms_token_response_json = tms_token_response.json()
    tms_token = tms_token_response_json['accessToken']

    return tms_token


def get_woker_token(conf, a_address):
    # # get worker token
    header = {'Content-Type': 'application/json'}
    worker_token_endpoint = conf['api_list']['-get_worker_token']
    worker_by_token_url = a_address + worker_token_endpoint
    worker_by_token_data = {'workerId': conf['worker_id'], 'worker password': conf['worker_pass']}
    worker_by_token_response = requests.get(url=worker_by_token_url, headers=header,
                                            data=json.dumps(worker_by_token_data))
    worker_by_token_response_json = worker_by_token_response.json()
    worker_by_token = worker_by_token_response_json['accessToken']

    return worker_by_token