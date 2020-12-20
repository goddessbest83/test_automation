import requests


# get user by token
def get_user_info(user_token, conf, a_address):
    header = {'Content-Type': 'application/json', 'Authorization': user_token}
    user_by_token_endpoint = conf['api_list']['-get_user_by_token']
    user_by_token_url = a_address + user_by_token_endpoint
    user_by_token_response = requests.get(url=user_by_token_url, headers=header)
    user_by_token_response_json = user_by_token_response.json()
    user_id = user_by_token_response_json['_id']
    user_email_id = user_by_token_response_json['userId']
    user_name = user_by_token_response_json['name']
    user_phone = user_by_token_response_json['phone']
    user_invitecode = user_by_token_response_json['inviteCode']

    return user_id, user_email_id, user_name, user_phone, user_invitecode


def get_card_info(user_token, conf, a_address):
    header = {'Content-Type': 'application/json', 'Authorization': user_token}
    card_info_endpoint = conf['api_list']['-get_card_info']
    card_info_endpoint_url = a_address + card_info_endpoint
    card_info_response = requests.get(url=card_info_endpoint_url, headers=header)
    card_info_response_json = card_info_response.json()
    card_id = 'card_id : ' + card_info_response_json[0]['_id']

    return card_id


def delete_user_account(tms_token, conf, a_address, user_id):
    header = {'Authorization': tms_token}
    delete_user_endpoint = conf['api_list']['delete_user_account']
    delete_user_endpoint = delete_user_endpoint.replace(':user_id', user_id)
    delete_user_endpoint_url = a_address + delete_user_endpoint
    delete_user_response = requests.get(url=delete_user_endpoint_url, headers=header)
    delete_user_response_json = delete_user_response.status_code

    return delete_user_response_json


def recover_user_account(tms_token, conf, a_address, user_id):
    header = {'Authorization': tms_token}
    recover_user_endpoint = conf['api_list']['recover_user_account']
    recover_user_endpoint = recover_user_endpoint.replace(':user_id', user_id)
    recover_user_endpoint_url = a_address + recover_user_endpoint
    recover_user_response = requests.get(url=recover_user_endpoint_url, headers=header)
    recover_user_response_json = recover_user_response.status_code

    return recover_user_response_json