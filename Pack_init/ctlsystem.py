import paramiko
from Pack_init.paracall import Shellcontrol
import Pack_init.service_list as service_list


class Service_status:    
    def __init__(self,conn, os, service):
        self.conn = conn
        self.os_name = os
        
        self.crt = Shellcontrol(conn)
                
        if os == "Ubuntu":
            self.os_code = 2
        else:
            self.os_code = 1
            
        service_info_cl1 = service_list.Service_info_class(service)
        service_info = service_info_cl1.service_info_return()
        service_line = service_info_cl1.find_service_line()
        
        
        self.system = service_info[service_line][self.os_code]   
        
        # commend_status = "systemctl status " + self.system 
        # self.status_read = self.crt.request(commend_status)
        # if self.status_read in "could not be found":
        #     print("해당 서비스가 존재하지 않습니다.")
        # else:            
        #     self.status_line = self.status_read.split("\n")
        #     self.status_line[1] = self.status_line[1].strip("preset: disabled")
        #     self.status_line[1] = self.status_line[1].strip("preset: enabled")
        
    # status 갱신함수
    def re_status(self):
        commend_status = "systemctl status " + self.system
        self.status_read = self.crt.request(commend_status)
        if self.status_read in "could not be found":
            print("해당 서비스가 존재하지 않습니다.")
        else:            
            self.status_line = self.status_read.split("\n")
            self.status_line[1] = self.status_line[1].strip("preset: disabled")
            self.status_line[1] = self.status_line[1].strip("preset: enabled")
        
        
    # 결과값 출력 함수
    def status_print(self):
        self.re_status()
        print(self.status_read)

    # loaded 상태 확인
    def loaded_status(self):
        self.re_status()

        if "enabled" in self.status_line[1]:
            self.loaded = "enabled"
            return self.loaded
        elif "disabled" in self.status_line[1]:
            self.loaded = "disabled"
            return self.loaded
        else:
            print("error")
            
    # active상태 확인      
    def active_status(self):   
        self.re_status()
        if "inactive" in self.status_line[2]:
            self.active_status = "inactive"
            return self.active_status
        elif "running" in self.status_line[2]:
            self.active_status = "active"
            return self.active_status
        else:
            print("error")

    # 서비스 시작
    def system_start(self):
        change_commend = "systemctl start " + self.system
        change_service = self.crt.request(change_commend)
        self.re_status()
        if "running" in self.status_line[2]:
            self.active_status = "active"
            print("active is active")

    # 서비스 종료
    def system_stop(self):
        change_commend = "systemctl stop " + self.system
        change_service = self.crt.request(change_commend)
        self.re_status()
        if "inactive" in self.status_line[2]:
            self.active_status = "inactive"
            print("active is inactive")

    # 서비스 실행 설정
    def system_enable(self):
        change_commend = "systemctl enable " + self.system
        change_service = self.crt.request(change_commend)
        self.re_status()
        if "enabled" in self.status_line[1]:
            self.active_status = "enabled"
            print("loaded is enabled")

    # 서비스 미실행 설정
    def system_disable(self):
        change_commend = "systemctl disable " + self.system
        change_service = self.crt.request(change_commend)
        self.re_status()
        if "disabled" in self.status_line[1]:
            self.active_status = "disabled"
            print("loaded is disabled")



        



