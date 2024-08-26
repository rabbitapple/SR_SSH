# call_log.py

from Pack_init.paracall import Shellcontrol
from Pack_init.log_info import *
import Pack_init.service_list as service_list


# 클래스 생성
class Call_log:
    # 생성자. 로그 가공. 
    def __init__(self, conn, service, name):
        self.conn = conn
        self.service = service
        self.name = name
        self.crt = Shellcontrol(conn)
        # 로그 정보파일 리스트화
        loginfo = Log_info_class()
        log_location = loginfo.service_log_location(name) # 서비스 로그 위치
        self.log_key = loginfo.service_log_keyword(name) # 로그 색인 키값

        
        change_commend = "cat " + log_location
        self.log_all = self.crt.request(change_commend)    
        self.log_list = self.log_all.split("\n")

    # 로그 읽기 함수.
    def print_log(self):
        for i in self.log_list:
            print(i)



# 공통로그폴더일경우 오버라이딩.
class Call_log_service(Call_log):
    def print_log(self):  
        for i in self.log_list:
            if self.log_key in i:
                print(i)



class Call_log_main:
    def prilog(self,conn, service, name):
       
        if service == "none":
            a = Call_log(conn, service, name)
        
        else:
            a = Call_log_service(conn, service, name)
        a.print_log()





