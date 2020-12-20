import os
import yaml
import tkinter.messagebox as msgbox


from tkinter import *
from tkinter import ttk
from src.api_lists import get_token
from src.api_lists import get_user_info
from src.api_lists import scooters
from src.api_lists import custom_reports
from datetime import datetime

with open('info.yaml') as ym:
    conf = yaml.load(ym, Loader=yaml.FullLoader)
with open('personal.yaml') as p:
    doc = yaml.load(p, Loader=yaml.FullLoader)
for i in doc:
    doc[i] = 'null'
with open('personal.yaml', 'w') as p:
    yaml.dump(doc, p)

window = Tk()
window.title("PUMP QMS v1.0.0")
window.resizable(False, False)
window.configure()
window.geometry("680x790")

photo = PhotoImage(file='images/ok.png')


# 스크롤 바 영역
scrollbar = Scrollbar(window, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

# 서버 선택 라디오 버튼 메뉴 생성
server_menu = Menu(window)

select_server = Menu(server_menu, tearoff=0)
select_server.add_radiobutton(label="Staging")
select_server.add_separator()
select_server.add_radiobutton(label="Develop")
select_server.add_separator()
select_server.add_radiobutton(label="Live")

server_menu.add_cascade(label="Select_Server", menu=select_server)

window.configure(menu=server_menu)

# relpath = os.path.relpath("/Users/hyunjunpark/python_gui/src/images")
# print(relpath)

# 유저 ID, PASS 작성하는 Frame 생성
test_image = PhotoImage(file='images/user.png')
user_account_frame = LabelFrame(window, text="테스트 진행자 정보", relief="solid", bd=1, pady=5)
user_account_frame.pack()
user_account_frame.place(x=5, y=5, width=665, height=120)

# 프레임 내부 계정 관련 최초 문구
account_label = Label(user_account_frame, text="씽씽앱 계정")
account_label.pack()
account_label.grid(row=0, column=0, padx=5)

# 씽씽 ID 작성 문구
id_label = Label(user_account_frame, text="ID ")
id_label.grid(row=0, column=3, padx=5)

# 씽씽 ID 작성 텍스트 박스
account_id = StringVar()
user_id_box = Entry(user_account_frame, textvariable=account_id)
user_id_box.grid(row=0, column=4, padx=5)

# 씽싱 PASS 작성 문구
pass_label = Label(user_account_frame, text="PASS ")
pass_label.grid(row=0, column=6)

# 씽싱 PASS 작성 텍스트 박스
account_pass = StringVar()
user_pass_box = Entry(user_account_frame, textvariable=account_pass, width=12)
user_pass_box.grid(row=0, column=7, padx=5)


# 토큰 가져오기 전 텍스트 가져와서 저장하기
def get_user_account_info():
    with open('personal.yaml') as p:
        doc = yaml.load(p, Loader=yaml.FullLoader)
    doc['account_id'] = account_id.get()
    doc['account_pass'] = account_pass.get()

    with open('personal.yaml', 'w') as p:
        yaml.dump(doc, p)

    with open('personal.yaml') as p:
        doc = yaml.load(p, Loader=yaml.FullLoader)
    try:
        user_token = get_token.get_xingxing_user_token(conf['stg_app_token'], conf, conf['stg_api_base_url'], doc)
    except KeyError:
        msgbox.showwarning('흐엉 ㅜㅜ', '아이디나 비번중에 하나가 틀리거나 다 틀렸어요!')

    try:
        if user_token != '':
            with open('personal.yaml') as p:
                doc = yaml.load(p, Loader=yaml.FullLoader)
            doc['user_token'] = user_token

            with open('personal.yaml', 'w') as p:
                yaml.dump(doc, p)

            success_label = Label(user_account_frame, image=photo)
            success_label.grid(row=0, column=9, pady=0)
            time = datetime.now().strftime('%H:%M')
            time_stamp = Label(user_account_frame, text=time)
            time_stamp.grid(row=0, column=10)
        else:
            print('토큰 가져오기 실패...')
    except UnboundLocalError:
        pass

# 토큰 가져오기 버튼
get_token_button = Button(user_account_frame, text="토큰 가져오기", command=get_user_account_info)
get_token_button.grid(row=0, column=8)

# ******** 마스터 영역 *********
# 마스터 프레임 내부 계정 관련 최초 문구
master_account_label = Label(user_account_frame, text="마스터 계정")
master_account_label.grid(row=1, column=0, padx=5)

# 마스터 ID 작성 문구
master_id_label = Label(user_account_frame, text="ID ")
master_id_label.grid(row=1, column=3)

# 마스터 ID 작성 텍스트 박스
master_id_str = StringVar()
master_user_id_box = Entry(user_account_frame, textvariable=master_id_str)
master_user_id_box.grid(row=1, column=4, padx=5)

# 마스터 PASS 작성 문구
master_pass_label = Label(user_account_frame, text="PASS ")
master_pass_label.grid(row=1, column=6)

# 마스터 PASS 작성 텍스트 박스
master_pass_str = StringVar()
master_user_pass_box = Entry(user_account_frame, textvariable=master_pass_str, width=12)
master_user_pass_box.grid(row=1, column=7, padx=5)

# master 토큰 가져오기 버튼
master_get_token_button = Button(user_account_frame, text="토큰 가져오기")
master_get_token_button.grid(row=1, column=8)

# ******** TMS 영역 *********
# TMS 프레임 내부 계정 관련 최초 문구
TMS_account_label = Label(user_account_frame, text="TMS 계정")
TMS_account_label.grid(row=2, column=0, padx=5)

# TMS ID 작성 문구
TMS_id_label = Label(user_account_frame, text="ID ")
TMS_id_label.grid(row=2, column=3)

# TMS ID 작성 텍스트 박스
tms_id = StringVar()
TMS_user_id_box = Entry(user_account_frame, textvariable=tms_id)
TMS_user_id_box.grid(row=2, column=4, padx=5)

# TMS PASS 작성 문구
TMS_pass_label = Label(user_account_frame, text="PASS ")
TMS_pass_label.grid(row=2, column=6)

# TMS PASS 작성 텍스트 박스
tms_pass = StringVar()
TMS_user_pass_box = Entry(user_account_frame, textvariable=tms_pass, width=12)
TMS_user_pass_box.grid(row=2, column=7, padx=5)


def get_tms_account_info():
    with open('personal.yaml') as p:
        doc = yaml.load(p, Loader=yaml.FullLoader)
    doc['tms_id'] = tms_id.get()
    doc['tms_pass'] = tms_pass.get()

    with open('personal.yaml', 'w') as p:
        yaml.dump(doc, p)

    with open('personal.yaml') as p:
        doc = yaml.load(p, Loader=yaml.FullLoader)
    try:
        tms_token = get_token.get_tms_token(conf, conf['stg_api_base_url'], doc)
    except KeyError:
        msgbox.showwarning('흐엉 ㅜㅜ', '아이디나 비번중에 하나가 틀리거나 다 틀렸어요!')

    try:
        if tms_token != '':
            with open('personal.yaml') as p:
                doc = yaml.load(p, Loader=yaml.FullLoader)
            doc['tms_token'] = tms_token

            with open('personal.yaml', 'w') as p:
                yaml.dump(doc, p)

            success_label = Label(user_account_frame, image=photo)
            success_label.grid(row=2, column=9, pady=0)
            time = datetime.now().strftime('%H:%M')
            time_stamp = Label(user_account_frame, text=time)
            time_stamp.grid(row=2, column=10)
        else:
            print('토큰 가져오기 실패...')
    except UnboundLocalError:
        pass

# TMS 토큰 가져오기 버튼
TMS_get_token_button = Button(user_account_frame, text="토큰 가져오기", command=get_tms_account_info)
TMS_get_token_button.grid(row=2, column=8)

# 스쿠터 정보 관련 Frame 생성
scooters_frame = LabelFrame(window, text="Scooters 정보", relief="solid", bd=1)
scooters_frame.pack(side="left")
scooters_frame.place(x=5, y=130, width=330, height=180)

# 스쿠터 시리얼 입력 텍스트 박스
serial_str = StringVar()
serial_text_box = Entry(scooters_frame, textvariable=serial_str, width=10)
serial_text_box.grid(row=0, column=0, padx=5, pady=10)

# 스쿠터 시리얼 가져오기
def get_serial():
    scooter_serial = serial_str.get()
    with open('personal.yaml') as p:
        doc = yaml.load(p, Loader=yaml.FullLoader)
    try:
        scooter_info = scooters.get_scooter_info(doc['tms_token'], conf, conf['stg_api_base_url'], scooter_serial)
        scooter_info = list(scooter_info)
        scooter_info_list = ['_id : ', 'battery : ', 'serialNumber : ', 'useStatus : ', 'enable : ', 'gpsSignal : ']
        for i in range(len(scooter_info)):
            search_result_scooter.insert(END, scooter_info_list[i] + scooter_info[i] + '\n')
        scooter_info_success_label = Label(scooters_frame, image=photo)
        scooter_info_success_label.grid(row=0, column=2, pady=0)
        time = datetime.now().strftime('%H:%M')
        time_stamp = Label(scooters_frame, text=time)
        time_stamp.grid(row=0, column=3)
    # except KeyError:
    #     msgbox.showwarning('스쿠터 조회 오류', '스쿠터 시리얼을 확인해주세요')
    except UnboundLocalError as u:
        msgbox.showwarning('스쿠터 시리얼 오류', u)

# 스쿠터 시리얼 조회 버튼
search_scooter_button = Button(scooters_frame, text="스쿠터 조회", command=get_serial)
search_scooter_button.grid(row=0, column=1, padx=5, pady=10)

# 스쿠터 조회 결과 텍스트 박스
search_result_scooter = Text(scooters_frame, width=40, height=7, relief="solid", borderwidth=1)
search_result_scooter.grid(row=1, column=0, padx=5, pady=5, columnspan=4)

# 유저 정보 관련 Frame 생성
user_frame = LabelFrame(window, text="User 정보", relief="solid", bd=1)
user_frame.pack()
user_frame.place(x=340, y=130, width=330, height=180)

# 유저 아이 입력 텍스트 박스
# user_id_str = StringVar()
# user_id_text_box = Entry(user_frame, textvariable=user_id_str)
# user_id_text_box.grid(row=0, column=0, padx=5, pady=10)


def get_user_info_by_token():
    with open('personal.yaml') as p:
        doc = yaml.load(p, Loader=yaml.FullLoader)
    try:
        user_info_data = get_user_info.get_user_info(doc['user_token'], conf, conf['stg_api_base_url'])
        user_info_data = list(user_info_data)
        doc['user_id'] = user_info_data[0]
        doc['name'] = user_info_data[2]
        doc['phone'] = user_info_data[3]
        doc['invite_code'] = user_info_data[4]
        with open('personal.yaml', 'w') as p:
            yaml.dump(doc, p)

        user_info_list = ['_id : ', 'userId : ', 'name : ', 'phone : ', 'inviteCode : ']
        for i in range(len(user_info_data)):
            search_result_user.insert(END, user_info_list[i] + user_info_data[i] + '\n')

        user_info_success_label = Label(user_frame, image=photo)
        user_info_success_label.grid(row=0, column=1, pady=0)
        time = datetime.now().strftime('%H:%M')
        time_stamp = Label(user_frame, text=time)
        time_stamp.grid(row=0, column=2)
    except KeyError as k:
        msgbox.showwarning('토큰이 확인되지 않아요', k)


# 유저 정보 조회 버튼
search_user_button = Button(user_frame, text="유저 조회", command=get_user_info_by_token)
search_user_button.grid(row=0, column=0, padx=0, pady=10)


def get_card_info_by_token():
    with open('personal.yaml') as p:
        doc = yaml.load(p, Loader=yaml.FullLoader)
    try:
        card_info_data = get_user_info.get_card_info(doc['user_token'], conf, conf['stg_api_base_url'])
        search_result_user.insert(END, card_info_data + '\n')
        user_info_success_label = Label(user_frame, image=photo)
        user_info_success_label.grid(row=0, column=4, padx=0, pady=0)
        time = datetime.now().strftime('%H:%M')
        time_stamp = Label(user_frame, text=time)
        time_stamp.grid(row=0, column=5, padx=0)
    except KeyError as k:
        msgbox.showwarning('토큰이 확인되지 않아요', k)

# 카드 정보 조회 버튼
get_card_id = Button(user_frame, text='카드 조회', command=get_card_info_by_token)
get_card_id.grid(row=0, column=3, padx=0, pady=10)

# 유저 조회 결과 텍스트 박스
search_result_user = Text(user_frame, width=40, height=7, relief="solid", borderwidth=1)
search_result_user.grid(row=1, column=0, padx=5, pady=10, columnspan=6)

# Operation Frame 생성
operation = LabelFrame(window, text="Operation", relief="solid", bd=1)
operation.pack()
operation.place(x=5, y=310, width=665, height=470)

# operation frame 안에 배터리 수치 교체 Frame 생성
change_battery = LabelFrame(operation, text="배터리 수치 교체", relief="solid", bd=1)
change_battery.place(x=5, y=5, width=325, height=80)

# 배터리 수치 텍스트 박스
battery_num = IntVar()
battery_num_test_box = Entry(change_battery, textvariable=battery_num, width=5)
battery_num_test_box.grid(row=0, column=0, padx=5, pady=10)

# 배터리 변경 API
def change_battery_num():
    with open('personal.yaml') as p:
        doc = yaml.load(p, Loader=yaml.FullLoader)
    try:
        scooter_num = scooters.change_scooter_battery(doc['tms_token'], conf, conf['stg_api_base_url'], serial_str.get(), battery_num.get())

        scooter_b_num = Label(change_battery, text=str(scooter_num))
        scooter_b_num.grid(row=0, column=2, pady=5)

        scooter_battery_success_label = Label(change_battery, image=photo)
        scooter_battery_success_label.grid(row=0, column=3, padx=0, pady=0)
        time = datetime.now().strftime('%H:%M')
        time_stamp = Label(change_battery, text=time)
        time_stamp.grid(row=0, column=4, padx=0)
    except KeyError as k:
        msgbox.showwarning('오류가 발생했어요', k)

# 배터리 수치 변경 버튼
change_battery_button = Button(change_battery, text="변경", command=change_battery_num)
change_battery_button.grid(row=0, column=1, padx=5, pady=10)

# operation frame 안에 배터리 수치 교체 Frame 생성
custom_report = LabelFrame(operation, text="1:1 문의 등록", relief="solid", bd=1)
custom_report.place(x=335, y=5, width=325, height=80)

# 1:1문의 일괄등록
def all_create_custom_reports():
    success_num = 0
    get_serial_str = serial_str.get()
    with open('personal.yaml') as p:
        doc = yaml.load(p, Loader=yaml.FullLoader)
    try:
        parking_report_id = custom_reports.create_parking_custom_reports(doc['user_token'], conf,
                                                                         conf['stg_api_base_url'], get_serial_str)
        success_num += 1

        rent_report_id = custom_reports.create_rent_custom_reports(doc['user_token'], conf,
                                                                         conf['stg_api_base_url'], get_serial_str)
        success_num += 1

        scooter_report_id = custom_reports.create_scooter_custom_reports(doc['user_token'], conf,
                                                                         conf['stg_api_base_url'], get_serial_str)
        success_num += 1

        app_report_id = custom_reports.create_app_custom_reports(doc['user_token'], conf,
                                                                 conf['stg_api_base_url'], get_serial_str)
        success_num += 1

        message_report_id = custom_reports.create_message_custom_reports(doc['user_token'], conf,
                                                                         conf['stg_api_base_url'], get_serial_str)
        success_num += 1

        success_num_label = Label(custom_report, text=str(success_num))
        success_num_label.grid(row=0, column=1, pady=1)

        with open('personal.yaml') as p:
            doc = yaml.load(p, Loader=yaml.FullLoader)
        doc['parking_report_id'] = parking_report_id
        doc['rent_report_id'] = rent_report_id
        doc['scooter_report_id'] = scooter_report_id
        doc['app_report_id'] = app_report_id
        doc['message_report_id'] = message_report_id

        with open('personal.yaml', 'w') as p:
            yaml.dump(doc, p)

        all_create_custom_reports_success_label = Label(custom_report, image=photo)
        all_create_custom_reports_success_label.grid(row=0, column=2, padx=0, pady=0)
        time = datetime.now().strftime('%H:%M')
        time_stamp = Label(custom_report, text=time)
        time_stamp.grid(row=0, column=3, padx=0)
    except KeyError as k:
        msgbox.showwarning('오류가 발생했어요', k)
    except UnboundLocalError as u:
        msgbox.showwarning('모두 등록에 실패했어요', u)


# 1:1 문의 일괄 등록 버튼
all_create_custom_reports = Button(custom_report, text="1:1문의 일괄 등록", command=all_create_custom_reports)
all_create_custom_reports.grid(row=0, column=0, padx=5, pady=2)


# 1:1 문의 일괄 삭제
def delete_custom_reports():
    with open('personal.yaml') as p:
        doc = yaml.load(p, Loader=yaml.FullLoader)
    all_reports = [doc['parking_report_id'], doc['rent_report_id'],
                   doc['scooter_report_id'], doc['app_report_id'], doc['message_report_id']]
    delete_num = 0
    for all_report in all_reports:
        delete_status_code = custom_reports.delete_all_custom_reports(doc['tms_token'], conf, conf['stg_api_base_url'], all_report)
        if delete_status_code == 200:
            delete_num += 1

    if delete_num > 0:
        delete_num_label = Label(custom_report, text=str(delete_num))
        delete_num_label.grid(row=1, column=1, pady=0)

        all_delete_custom_reports_success_label = Label(custom_report, image=photo)
        all_delete_custom_reports_success_label.grid(row=1, column=2, padx=0, pady=0)
        time = datetime.now().strftime('%H:%M')
        time_stamp = Label(custom_report, text=time)
        time_stamp.grid(row=1, column=3, padx=0)
    else:
        msgbox.showwarning('삭제에 실패했어요', '하나도 삭제되지 않았어요')


# 1:1 문의 일괄 삭제 버튼
all_delete_custom_reports = Button(custom_report, text='1:1문의 일괄 삭제', command=delete_custom_reports)
all_delete_custom_reports.grid(row=1, column=0, padx=5, pady=2)

# operation frame 안에 배터리 수치 교체 Frame 생성
notice = LabelFrame(operation, text="공지 & 이벤트", relief="solid", bd=1)
notice.place(x=5, y=90, width=325, height=80)

# 공지 일괄등록 버튼
create_notice = Button(notice, text="테스트용 공지 등록")
create_notice.grid(row=0, column=0, padx=5, pady=2)

# 이벤트 일괄등록 버튼
create_event_notice = Button(notice, text="테스트용 이벤트 공지 등록")
create_event_notice.grid(row=1, column=0, padx=5, pady=2)

# operation frame 안에 수리내 Frame 생성
repair_history = LabelFrame(operation, text="수리내역", relief="solid", bd=1)
repair_history.place(x=335, y=90, width=325, height=80)

# 수리 부품별 일괄 수리 내역 남기기 버튼
repair_history_button = Button(repair_history, text="수리 부품별 일괄 수리 내역 등록")
repair_history_button.grid(row=0, column=1, padx=5, pady=10)

# operation frame 안에 회원 가입 & 탈퇴 생성
create_delete_user = LabelFrame(operation, text="회원가입 & 탈퇴", relief="solid", bd=1)
create_delete_user.place(x=5, y=180, width=325, height=80)


def delete_user():
    with open('personal.yaml') as p:
        doc = yaml.load(p, Loader=yaml.FullLoader)
    delete_user_response = get_user_info.delete_user_account(doc['tms_token'], conf, conf['stg_api_base_url'], doc['user_id'])
    try:
        if delete_user_response == 200:
            all_delete_custom_reports_success_label = Label(custom_report, image=photo)
            all_delete_custom_reports_success_label.grid(row=0, column=1, padx=0, pady=0)
            time = datetime.now().strftime('%H:%M')
            time_stamp = Label(custom_report, text=time)
            time_stamp.grid(row=0, column=2, padx=0)
    except KeyError:
        msgbox.showwarning('삭제 실패', '계정 삭제에 실패했어요')


# 회원 탈퇴 버튼
delete_user = Button(create_delete_user, text="회원 탈퇴", command=delete_user)
delete_user.grid(row=0, column=0, padx=5, pady=10)


def recover_user():
    with open('personal.yaml') as p:
        doc = yaml.load(p, Loader=yaml.FullLoader)
    recover_user_response = get_user_info.recover_user_account(doc['tms_token'], conf, conf['stg_api_base_url'], doc['user_id'])
    try:
        if recover_user_response == 200:
            all_delete_custom_reports_success_label = Label(custom_report, image=photo)
            all_delete_custom_reports_success_label.grid(row=1, column=1, padx=0, pady=0)
            time = datetime.now().strftime('%H:%M')
            time_stamp = Label(custom_report, text=time)
            time_stamp.grid(row=1, column=2, padx=0)
    except KeyError:
        msgbox.showwarning('복구 실패', '계정 복구에 실패했어요')

# 탈퇴 복구 버튼
recover_delete_user = Button(create_delete_user, text="탈퇴 복구", command=recover_user)
recover_delete_user.grid(row=0, column=1, padx=5, pady=10)

# operation frame 안에 첫 라이딩 삭제 Frame 생성
delete_first_riding = LabelFrame(operation, text="첫 라이딩 삭제", relief="solid", bd=1)
delete_first_riding.place(x=335, y=180, width=325, height=80)

# 수리 부품별 일괄 수리 내역 남기기 버튼
repair_history_button = Button(delete_first_riding, text="첫 라이딩 삭제")
repair_history_button.grid(row=0, column=1, padx=5, pady=10)

# operation frame 안에 스테이션 일괄 생성 frame 생성
all_create_station = LabelFrame(operation, text="스테이션 일괄 추가", relief="solid", bd=1)
all_create_station.place(x=5, y=270, width=325, height=80)

# 스테이션 일괄 추가 버튼
all_create_station_button = Button(all_create_station, text="스테이션 일괄 추가")
all_create_station_button.grid(row=0, column=0, padx=5, pady=10)

# 시즌패스 Frame 생성
season_pass = LabelFrame(operation, text='시즌 패스 (삭제예정)', relief='solid', bd=1)
season_pass.place(x=335, y=270, width=325, height=170)

# 패스 조회 버튼
get_pass_button = Button(season_pass, text='패스 정보 가져오기')
get_pass_button.grid(row=0, column=0, padx=5, pady=5)

# 현재 패스 결과 라벨
current_pass = Label(season_pass, text='구독중 패스')
current_pass.grid(row=1, column=0, pady=5)

# 패스 조회 결과 Text
pass_result = Text(season_pass, width=28, height=3, relief="solid", borderwidth=1)
pass_result.grid(row=1, column=1, pady=5)

# 다음 패스 결과 라벨
next_pass = Label(season_pass, text='구독 예약')
next_pass.grid(row=2, column=0, pady=5)

# 다음 패스 조회 결과 Text
next_pass_result = Text(season_pass, width=28, height=3, relief="solid", borderwidth=1)
next_pass_result.grid(row=2, column=1, pady=5)

# 패스 구매 Frame
buy_pass_label = LabelFrame(operation, text='패스 구매 (삭제 예정)', relief='solid', bd=1)
buy_pass_label.place(x=5, y=360, width=325, height=80)

pass_values = ['45 패스 x 3', '45 패스', '25패스 x 3', '25 패스', '10 패스']
pass_combo_box = ttk.Combobox(buy_pass_label, height=10, width=10, values=pass_values, state='readonly')
pass_combo_box.grid(row=0, column=0, padx=5, pady=5)

buy_pass_button = Button(buy_pass_label, text='패스 구매')
buy_pass_button.grid(row=0, column=1, padx=5, pady=5)

window.mainloop()
