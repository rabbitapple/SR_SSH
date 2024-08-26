# main
import traceback
from netmiko import ConnectHandler #ssh 모듈
from rs_set.main_function import Mainfunc
from rs_set.main_function import Mainfunc_ro

run = True #라우터 스위치 반복문
run_ans = True #인터페이스 반복문 1
run_ans2 = True #인터페이스 반복문2
list = []
list_2 = [] # 입력값 검증 리스트

# ssh connect를 위한 입력값
connect_ip = input("IP: ")
connect_user = input("Username : ")
connect_passwd = input("PW : ")

# ssh connect
net_connect = ConnectHandler(device_type = "cisco_ios", ip = connect_ip, username = connect_user, password = connect_passwd)
net_connect.enable()
print(connect_ip + "에 연결되었습니다.")
print("종료를 원할경우 end, 뒤로가기를 원할경우 exit를 입력하세요")

while run:
    equip = input("switch/router/server? \n")
    if  equip == "switch":
        maincode = Mainfunc(net_connect)
        run = False
        
    elif  equip == "router":
        maincode = Mainfunc_ro(net_connect)
        run = False




try:

    while run_ans:
        st1_dic = maincode.step2()
        step1 = input()
        run_ans2 = True

        for i in range(len(st1_dic)):
            list.append(str(i+1))
        
        if step1 == "end":
            run_ans = False
        
        elif step1 in list:
            while run_ans2:                
                st2_dic = st1_dic[step1]()
                step2 = input()
                
                for i in range(len(st2_dic)):
                    list_2.append(str(i+1))
            
                if step2 == "end":
                    run_ans = False
                    run_ans2 = False
                    
                elif step2 == "exit":
                    run_ans2 = False
                    
                elif step2 in list_2:
                    st2_dic[step2]()
                    
                    
                list_2 = []
            list = []

            
except:
    print(traceback.format_exc())

# ssh disconnect
net_connect.disconnect()
print(connect_ip + "로부터의 연결이 끊어졌습니다.")
