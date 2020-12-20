import requests
import json


def create_parking_custom_reports(user_token, conf, a_address, scooter_serial):

    header = {'Content-Type': 'application/json', 'Authorization': user_token}

    parking_custom_reports_endpoint = conf['api_list']['-post_custom_report']

    parking_custom_reports_url = a_address + parking_custom_reports_endpoint

    parking_custom_reports_data = {
        "serialNumber": scooter_serial,
        "latitude": 37.501282801564244,
        "longitude": 126.98641777038573,
        "address": "서울 강남구 역삼동 689-3",
        "pictures": [],
        "title": "주차신고 Test 용 제목",
        "desc": "Test 용 내용으로 주차신고 1건은 필요하여 해당 건은 남겨놓고 나머지는 삭제됩니다. 참고 부탁드립니다.",
        "problemType": "MESSAGE",
        "detailProblemTypes": ["PARKING"]
    }
    parking_custom_reports_response = requests.post(url=parking_custom_reports_url, headers=header,
                                                    data=json.dumps(parking_custom_reports_data))
    parking_custom_reports_response_json = parking_custom_reports_response.json()
    parking_custom_reports_id = parking_custom_reports_response_json['_id']

    return parking_custom_reports_id


def create_rent_custom_reports(user_token, conf, a_address, scooter_serial):

    header = {'Content-Type': 'application/json', 'Authorization': user_token}

    rent_custom_reports_endpoint = conf['api_list']['-post_custom_report']

    rent_custom_reports_url = a_address + rent_custom_reports_endpoint

    rent_custom_reports_data = {
        "serialNumber": scooter_serial,
        "latitude": 37.501282801564244,
        "longitude": 126.98641777038573,
        "address": "서울 강남구 역삼동 689-3",
        "pictures": [],
        "title": "주차신고 Test 용 제목",
        "desc": "Test 용 내용으로 주차신고 1건은 필요하여 해당 건은 남겨놓고 나머지는 삭제됩니다. 참고 부탁드립니다.",
        "problemType": "MESSAGE",
        "detailProblemTypes": ["RENTAL_RETURN"]
    }
    rent_custom_reports_response = requests.post(url=rent_custom_reports_url, headers=header,
                                                 data=json.dumps(rent_custom_reports_data))
    rent_custom_reports_response_json = rent_custom_reports_response.json()
    rent_custom_reports_id = rent_custom_reports_response_json['_id']

    return rent_custom_reports_id


def create_scooter_custom_reports(user_token, conf, a_address, scooter_serial):

    header = {'Content-Type': 'application/json', 'Authorization': user_token}

    scooter_custom_reports_endpoint = conf['api_list']['-post_custom_report']

    scooter_custom_reports_url = a_address + scooter_custom_reports_endpoint

    scooter_custom_reports_data = {
        "serialNumber": scooter_serial,
        "latitude": 37.501282801564244,
        "longitude": 126.98641777038573,
        "address": "서울 강남구 역삼동 689-3",
        "pictures": [],
        "title": "주차신고 Test 용 제목",
        "desc": "Test 용 내용으로 주차신고 1건은 필요하여 해당 건은 남겨놓고 나머지는 삭제됩니다. 참고 부탁드립니다.",
        "problemType": "MESSAGE",
        "detailProblemTypes": ["SCOOTER_PART"]
    }
    scooter_custom_reports_response = requests.post(url=scooter_custom_reports_url, headers=header,
                                                    data=json.dumps(scooter_custom_reports_data))
    scooter_custom_reports_response_json = scooter_custom_reports_response.json()
    scooter_custom_reports_id = scooter_custom_reports_response_json['_id']

    return scooter_custom_reports_id


def create_app_custom_reports(user_token, conf, a_address, scooter_serial):

    header = {'Content-Type': 'application/json', 'Authorization': user_token}

    app_custom_reports_endpoint = conf['api_list']['-post_custom_report']

    app_custom_reports_url = a_address + app_custom_reports_endpoint

    app_custom_reports_data = {
        "serialNumber": scooter_serial,
        "latitude": 37.501282801564244,
        "longitude": 126.98641777038573,
        "address": "서울 강남구 역삼동 689-3",
        "pictures": [],
        "title": "주차신고 Test 용 제목",
        "desc": "Test 용 내용으로 주차신고 1건은 필요하여 해당 건은 남겨놓고 나머지는 삭제됩니다. 참고 부탁드립니다.",
        "problemType": "MESSAGE",
        "detailProblemTypes": ["APP"]
    }
    app_custom_reports_response = requests.post(url=app_custom_reports_url, headers=header,
                                                    data=json.dumps(app_custom_reports_data))
    app_custom_reports_response_json = app_custom_reports_response.json()
    app_custom_reports_id = app_custom_reports_response_json['_id']

    return app_custom_reports_id


def create_message_custom_reports(user_token, conf, a_address, scooter_serial):

    header = {'Content-Type': 'application/json', 'Authorization': user_token}

    message_custom_reports_endpoint = conf['api_list']['-post_custom_report']

    message_custom_reports_url = a_address + message_custom_reports_endpoint

    message_custom_reports_data = {
        "serialNumber": scooter_serial,
        "latitude": 37.501282801564244,
        "longitude": 126.98641777038573,
        "address": "서울 강남구 역삼동 689-3",
        "pictures": [],
        "title": "주차신고 Test 용 제목",
        "desc": "Test 용 내용으로 주차신고 1건은 필요하여 해당 건은 남겨놓고 나머지는 삭제됩니다. 참고 부탁드립니다.",
        "problemType": "MESSAGE",
        "detailProblemTypes": ["MESSAGE"]
    }
    message_custom_reports_response = requests.post(url=message_custom_reports_url, headers=header,
                                                    data=json.dumps(message_custom_reports_data))
    message_custom_reports_response_json = message_custom_reports_response.json()
    message_custom_reports_id = message_custom_reports_response_json['_id']

    return message_custom_reports_id


def delete_all_custom_reports(tms_token, conf, a_address, report_id):

    header = {'Authorization': tms_token}

    delete_custom_reports_endpoint = conf['api_list']['-delete_custom_report']

    delete_custom_reports_url = a_address + delete_custom_reports_endpoint + report_id

    delete_custom_reports_response = requests.delete(url=delete_custom_reports_url, headers=header)
    delete_custom_reports_response_status = delete_custom_reports_response.status_code

    return delete_custom_reports_response_status
