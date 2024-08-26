# main
import traceback
import paramiko #ssh 모듈
from Pack_init.service_list import Service_info_class
from Pack_init.paracall import Shellcontrol
from Pack_init.submain import Mainfunc
from Pack_init.log_info import Log_info_class

run = True #라우터 스위치 반복문
run_ans = True #인터페이스 반복문 1
run_ans2 = True #인터페이스 반복문2
list = []
list_2 = [] # 입력값 검증 리스트
mulist = ""
menu = {}

# ssh connect를 위한 입력값
# connect_ip = "172.16.20.8"
# connect_user = "root"
# connect_passwd = "asd123!@"

connect_ip = input("IP: ")
connect_user = input("Username : ")
connect_passwd = input("PW : ")

net_connect = paramiko.SSHClient()
net_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
net_connect.connect(connect_ip,22 ,username=connect_user, password=connect_passwd)


print(connect_ip + "에 연결되었습니다.")
print("종료를 원할경우 end, 뒤로가기를 원할경우 exit를 입력하세요")

# OS 확인
chos = Shellcontrol(net_connect)
os = chos.check_os()



# 서비스 선택 메뉴 생성
lo = Log_info_class()
menu_1 = lo.service_name()
for i in range(len(menu_1)):
    mulist = mulist + str(i + 1) + "." + menu_1[i] + "\n"
    if i == 0:
        menu = {str(i+1):menu_1[i]}
    else :
        menu[str(i + 1)] = menu_1[i]



while run_ans:      
    # 서비스 질의
    step1 = input(mulist)
    run_ans2 = True

    # 질의한 서비스 확인 리스트
    for i in range(len(menu)):
        list.append(str(i+1))

    # if문 탈출 명령어
    if step1 == "end":
        run_ans = False

    # 질의한 서비스가 존재할경우
    elif step1 in list:
        service = menu.get(step1)
        sl = Service_info_class(service)
        service_name = sl.name2service(os)
        
        mf = Mainfunc(net_connect, os, service_name, service)
        while run_ans2:                
            st2_dic = mf.step2_1()
            step2 = input()
            
            for i in range(len(st2_dic)):
                list_2.append(str(i+1))
        
            if step2 == "end":
                run_ans = False
                run_ans2 = False
                
            elif step2 == "exit":
                run_ans2 = False
                
            elif step2 in list_2:
                print(st2_dic[step2])
                st2_dic[step2]()

            list_2 = []
        list = []
