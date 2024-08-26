# submain.py
from Pack_init.call_log import *
from Pack_init.install_service import Install_service
from Pack_init.ctlsystem import Service_status
from Pack_init.setting import Set_service



class Mainfunc:
    def __init__(self, conn, os, service, name):
        self.conn = conn
        self.service = service
        self.name = name
        self.ctl = Service_status(conn, os, service)
        self.ins = Install_service(conn, os, service)
        self.set = Set_service(conn)


    def dhcp(self):
        run = True
        while run:
            sel = input("1.Pool 설정\n2.Static 설정\n")
            if sel == "exit":
                run = False
                
            # Pool Setting
            elif sel in "1": 
                ni = input("DHCP Pool NI : ")
                ni_sub = input("DHCP Pool Subnet : ")
                gateway = input("Gateway : ") 
                gw_sub = input("Gateway's Subnet : ")
                start_ip = input("Start IP : ")
                end_ip = input("End IP : ")
                
                self.set.dhcpset(ni, ni_sub, gateway, gw_sub, start_ip, end_ip)
                
            #Static Setting
            elif sel in "2":
                host = input("Host Name : ")
                mac_add = input("Host's Mac address : ")
                ip = input("Setting IP: ")
                               
                self.set.dhcp_static(host, mac_add, ip)

    def dns(self):
        run = True
        while run:
            sel = input("1.Master 설정\n2.Slave 설정\n3.Domain 추가\n")
            if sel == "exit":
                run = False
                
            # Pool Setting
            elif sel in "1": 
                dns = input("Domain Name.Top Level Doamin Name: ")
                update = input("Update Allow IP : ")
                ns = input("DNS Server Host Name : ")
                ns_ip = input("DNS Server IP : ")
                
                self.set.dnsset_master(dns, update, ns, ns_ip)
                
            #Static Setting
            elif sel in "2":
                dns = input("Domain Name.Top Level Doamin Name : ")
                update = input("DNS Master Server IP : ")
                                               
                self.set.dnsset_slave(dns, update)

            # Domain 추가
            elif sel in "3":
                dns = input("Domain Name.Top Level Doamin Name : ")
                dn = input("Host Name : ")
                ip = input("Host IP : ")
                
                self.set.dnszone(dns, dn, ip)

    def samba(self):
        run = True
        while run:
            sel = input("1.Samba Setting\n2.SMB Mount\n")
            if sel == "exit":
                run = False
                
            # Samba Setting
            elif sel in "1": 
                user = input("Server User : ")
                smb_user = input("SMB User : ")
                comment = input("SMB Comment : ")
                allow_ip = input("Allow IP/Prifix : ")
                path = input("Share File Path : ")
                
                self.set.smbset(user, smb_user, comment, allow_ip, path)
            
            # SMB Mount
            elif sel in "2":
                ip= input("SMB Server IP : ")
                file_name= input("SMB File Path : ")
                path= input("Mount File Path : ")
                smb_user= input("SMB User Name : ")
                pw= input("SMB User Password : ")
                
                self.set.mount(ip, file_name, path, smb_user, pw)


    def setting(self):
        if self.name == "DHCP":
            self.dhcp()
    
        elif self.name == "DNS":
            self.dns()
            
        elif self.name == "SMB":
            self.samba()
            


    def step3(self):
        self.cmain = Call_log_main()
        self.cmain.prilog(self.conn, self.service, self.name)




# 1.상태 출력 2.start 3.stop 4.enable 5.disable 6.install
    def step2_1(self):
        print("1.상태 출력 \n2.start \n3.stop \n4.enable \n5.disable\n6.install\n7.로그확인\n8.설정\n")
        dic = {"1":self.ctl.status_print, "2":self.ctl.system_start, "3":self.ctl.system_stop, "4":self.ctl.system_enable, "5":self.ctl.system_disable, "6":self.ins.install, "7":self.step3, "8":self.setting}
        return dic




        