from rs_set.default_set import Setdefault
from rs_set.dhcp_set import Setdhcp
from rs_set.nat_set import Setnat
from rs_set.vtp_set import Setvtp



class Mainfunc:
    def __init__(self, conn):
        self.default = Setdefault(conn)
        self.dhcp = Setdhcp(conn)
        self.nat = Setnat(conn)
        self.vtp = Setvtp(conn)

# 1.임의값 입력 \n2.인터페이스 정보 \n3.인터페이스 ip설정 \n4.no shutdown \n5.설정 백업

    def step3_1_1(self): #임의값 입력
        run = True
        print("명령어를 입력하세요.")
        print("escape를 입력시 종료됩니다.")
        while run:
            commend = input()
            if commend == "escape":
                run = False
                com = ["conf t", "end"]
                self.default.list_re(com)
            else:
                self.default.ssh_conn(commend)

    def step3_1_2(self): #인터페이스 정보
        self.default.int_ip()

    def step3_1_3(self): # 인터페이스 ip설정
        port = input("인터페이스 : ")
        set_ip = input("IP : ")
        set_sm = input("SM : ")
        self.default.setintip(port, set_ip, set_sm)

    def step3_1_4(self): # no shutdown
        port = input("인터페이스 : ")
        self.default.set_noshut(port)

    def step3_1_5(self): # 설정 백업
        print(".rsup 확장자로 저장욉니다.")
        file = input("백업 파일명 :")
        self.default.backup(file)


# 1.vtp 정보\n2.trunk 정보\n3.vlan 정보\n4.vlan 생성\n5.vlan 설정\n6.trunk포트 설정\7.vtp설정
    def step3_2_1(self): # vtp 정보
        self.vtp.sh_vtp()

    def step3_2_2(self):# trunk 정보
        self.vtp.sh_trunk()

    def step3_2_3(self):# vlan 정보
        self.vtp.sh_vlan()

    def step3_2_4(self):# vlan 생성
        run = True
        vlan = []
        print("escape입력시 중지")
        while run:
            inv = input("VLAN : ")
            if inv == "escape":
                run = False
            else:
                vlan.append(inv)

        self.vtp.vlan_generate(vlan)

    def step3_2_5(self):# 인터페이스에 vlan 설정
        run = True
        run2 = True
        while run:
            port = input("Port : ")
            vlan = input("VLAN : ")
            self.vtp.vlan_int(port, vlan)
            while run2:
                ans = input("계속 설정하시겠습니까? y/n")
                if ans == "y":
                    run2 = False
                elif ans == "n":
                    run = False
                    run2 = False
            

    def step3_2_6(self):# trunk포트 설정
        run = True
        run2 = True
        while run:
            port = input("Port : ")
            self.vtp.vlan_trunk(port)
            while run2:
                ans = input("계속 설정하시겠습니까? y/n")
                if ans == "y":
                    run2 = False
                elif ans == "n":
                    run = False
                    run2 = False

    def step3_2_7(self):# vtp 설정
        domain = input("Domain : ")
        passwd = input("Passwd : ")
        status = input("server/transparent/client? ")
        self.vtp.vtp_setting(domain, passwd, status)

# 1.stp 정보\n2.stp 우선순위 설정

    def step3_3_1(self):# stp 정보
        self.vtp.sh_stp()

    def step3_3_2(self):# stp 우선순위 설정
        run = True
        run2 = True
        while run:
            vlan = input("VLAN : ")
            pri = input("Priority : ")
            self.vtp.stpset(vlan, pri)
            while run2:
                ans = input("계속 설정하시겠습니까? y/n")
                if ans == "y":
                    run2 = False
                elif ans == "n":
                    run = False
                    run2 = False

    
        
    def step3_1_dic(self): # default 설정 dic
        print("1.임의값 입력 \n2.인터페이스 정보 \n3.인터페이스 ip설정 \n4.no shutdown \n5.설정 백업\n")
        dic = {"1":self.step3_1_1, "2":self.step3_1_2, "3":self.step3_1_3, "4":self.step3_1_4, "5":self.step3_1_5}
        return dic


    def step3_2_dic(self): # vtp 설정 dic
        print("1.VTP 정보\n2.Trunk 정보\n3.VLAN 정보\n4.VLAN 생성\n5.인터페이스에 VLAN 설정\n6.Trunk 포트 설정\n7.VTP 설정\n")
        dic = {"1":self.step3_2_1, "2":self.step3_2_2, "3":self.step3_2_3, "4":self.step3_2_4, "5":self.step3_2_5, "6":self.step3_2_6, "7":self.step3_2_7}
        return dic
        
    def step3_3_dic(self): # stp 설정 dic
        print("1.STP 정보\n2.STP 우선순위 설정\n")
        dic = {"1":self.step3_3_1, "2":self.step3_3_2}
        return dic

    def step2(self): # 초기 메뉴
        print("1.Default\n2.VLAN 및 VTP\n3.STP")
        dic = {"1":self.step3_1_dic, "2":self.step3_2_dic, "3":self.step3_3_dic}
        return dic



#******************************************************************************************************************

class Mainfunc_ro(Mainfunc):

# \n6.라우팅 테이블 설정 \n7.라우팅 테이블 정보\n8.vlan 캡슐화 
    def step3_1_6(self): # 라우팅 테이블 설정
        run = True
        run2 = True
        while run:
            ni = input("NI : ")
            ni_sm = input("SubnetMask : ")
            transeport = input("Next Port IP : ")
            self.default.set_rout(ni, ni_sm, transeport)
            while run2:
                ans = input("계속 설정하시겠습니까? y/n")
                if ans == "y":
                    run2 = False
                elif ans == "n":
                    run = False
                    run2 = False
                    
    def step3_1_7(self): #라우팅 테이블 정보
        self.default.sh_route()

    def step3_1_8(self): #vlan 캡슐화 
        run = True
        run2 = True
        while run:
            vlan = input("VLAN : ")
            self.default.capsul(vlan)
            while run2:
                ans = input("계속 설정하시겠습니까? y/n")
                if ans == "y":
                    run2 = False
                elif ans == "n":
                    run = False
                    run2 = False


    def step3_1_9(self): #설정 업로드
        run = True
        while run:
            name = input("설정을 업로드할 파일명(확장자 x)을 입력하세요 : ")
            self.default.upload(name)

#1.pool 정보 확인\n2.binding 정보 확인\3.dhcp서버 설정\n
    def step3_2_1(self):
        self.dhcp.sh_pool()

    def step3_2_2(self):
        self.dhcp.sh_binding()

    def step3_2_3(self):
        start_ip = input("시작 IP : ")
        end_ip = input("끝 IP : ")
        pool_name = input("Pool 이름 : ")
        net_range = input("NI : ")
        ip_sm = input("NI의 Subnet Mask : ")
        gateway = input("Gateway IP : ")        
        self.dhcp.set_dhcp_pool(start_ip, end_ip, pool_name, net_range, ip_sm, gateway)


# 1.nat 정보 확인 \n2.Outside 설정 \n3.Inside 설정 \n4.Static NAT 설정 \n5.Daynamic NAT 설정 \n6.PAT 설정 \n

    def step3_3_1(self):
        self.nat.nat_status()

    def step3_3_2(self):
        run = True
        run2 = True
        while run:
            port = input("Interface : ")
            self.nat.out_set(port)
            while run2:
                ans = input("계속 설정하시겠습니까? y/n")
                if ans == "y":
                    run2 = False
                elif ans == "n":
                    run = False
                    run2 = False
        
        

    def step3_3_3(self):
        run = True
        run2 = True
        while run:
            port = input("Interface : ")
            self.nat.in_set(port)
            while run2:
                ans = input("계속 설정하시겠습니까? y/n")
                if ans == "y":
                    run2 = False
                elif ans == "n":
                    run = False
                    run2 = False

    def step3_3_4(self):
        run = True
        run2 = True
        while run:
            in_ip = input("Inside Interface IP : ")
            out_ip = input("Outside Interface IP : ")
            self.nat.static_nat(in_ip, out_ip)
            while run2:
                ans = input("계속 설정하시겠습니까? y/n")
                if ans == "y":
                    run2 = False
                elif ans == "n":
                    run = False
                    run2 = False

    def step3_3_5(self):
        run = True
        run2 = True
        while run:
            in_ip = input("Inside Interface IP : ")
            wild_mask = input("Inside IP Wild Mask : ")
            out_ip = input("Outside Interface IP : ")
            out_sm = input("Outside Subnet Mask : ")
            pool_name = input("Pool 이름 : ")
            port = input("Interface : ")
            self.nat.dynamic_nat(in_ip, wild_mask, out_ip, out_sm, pool_name, port)
            while run2:
                ans = input("계속 설정하시겠습니까? y/n")
                if ans == "y":
                    run2 = False
                elif ans == "n":
                    run = False
                    run2 = False

    def step3_3_6(self):
        run = True
        run2 = True
        while run:
            in_ip = input("Inside Interface IP : ")
            wild_mask = input("Inside IP Wild Mask : ")
            out_ip = input("Outside Interface IP : ")
            out_sm = input("Outside Subnet Mask : ")
            pool_name = input("Pool 이름 : ")
            self.nat.part_nat(in_ip, wild_mask, out_ip, out_sm, pool_name)
            while run2:
                ans = input("계속 설정하시겠습니까? y/n")
                if ans == "y":
                    run2 = False
                elif ans == "n":
                    run = False
                    run2 = False







    

    def step3_1_dic(self): # default 설정 dic
        print("1.임의값 입력 \n2.인터페이스 정보 \n3.인터페이스 ip설정 \n4.no shutdown \n5.설정 백업 \n6.라우팅 테이블 설정 \n7.라우팅 테이블 정보\n8.Vlan 캡슐화 \n9.설정 업로드\n")
        dic = {"1":super().step3_1_1, "2":super().step3_1_2, "3":super().step3_1_3, "4":super().step3_1_4, "5":super().step3_1_5, "6":self.step3_1_6, "7":self.step3_1_7, "8":self.step3_1_8, "9":self.step3_1_9}
        return dic


        
    def step3_2_dic(self): # vtp 설정 dic
        print("1.Pool 정보 확인\n2.Binding 정보 확인\3.DHCP서버 설정\n")
        dic = {"1":self.step3_2_1, "2":self.step3_2_2, "3":self.step3_2_3}
        return dic

    def step3_3_dic(self): # stp 설정 dic
        print("1.nat 정보 확인 \n2.Outside 설정 \n3.Inside 설정 \n4.Static NAT 설정 \n5.Daynamic NAT 설정 \n6.PAT 설정 \n")
        dic = {"1":self.step3_3_1, "2":self.step3_3_2, "3":self.step3_3_3, "4":self.step3_3_4, "5":self.step3_3_5, "6":self.step3_3_6}
        return dic

    def step2(self): # 초기 메뉴
        print("1.Default \n2.DHCP \n3.NAT")
        dic = {"1":self.step3_1_dic, "2":self.step3_2_dic, "3":self.step3_3_dic}
        return dic

        
















        
            