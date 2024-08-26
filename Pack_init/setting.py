# setting 
from Pack_init.paracall import Shellcontrol

class Set_service:
    def __init__(self, conn):
        self.call = Shellcontrol(conn)

    def sshset(self): # SSH PermitRootLogin 설정.
        file = "/etc/ssh/sshd_config"
        
        cmd = "cat /etc/ssh/sshd_config"
        conf = self.call.request(cmd)
        
        
        if conf in "PermitRootLogin no":
            cmd = "sed -i 's/PermitRootLogin no/PermitRootLogin yes/' " + file
            ans = self.call.request(cmd)
            print(ans)
            print("설정이 변경되었습니다.")

        else:
            cmd = "echo 'PermitRootLogin yes' >> " + file
            ans = self.call.request(cmd)
            print(ans)
            print("설정이 변경되었습니다.")


    def dnsset_master(self, dns, update, ns, ns_ip): # DNS설정
        #conf 설정
        conf_file = "/etc/named.conf"
        cmd = "sed -i 's/listen-on port 53 .*/listen-on port 53 { any; };/g' " + conf_file
        self.call.request(cmd)
        print("53번 포트 접근설정을 any로 설정하였습니다.")

        cmd = "sed -i 's/allow-query.*/listen-on port 53 { any; };/g' " + conf_file
        self.call.request(cmd)
        
        # rfc설정
        zone_file = "/etc/named.rfc1912.zones"
        cmd = "echo 'zone \"" + dns +"\" IN{\n\ttype master;\n\tfile \"" + dns + ".zone\";\n\tallow-update { " + update + "; };\n};' >> " + zone_file
        self.call.request(cmd)
        print("rfc파일 설정을 완료하였습니다.")
        
        # zone 파일 설정
        
        zone_create = "/var/named/" + dns + ".zone"        
        cmd = "cp -p /var/named/named.localhost " + zone_create       
        self.call.request(cmd)

        cmd = "sed -i 's/IN SOA.*/IN SOA\t" + ns + "." + dns + ".\tex.ex.com (/g' "+ zone_create       
        self.call.request(cmd)

        cmd = "sed -i 's/NS\t*/NS\t" + ns + "." + dns + "/g'" + zone_create       
        self.call.request(cmd)

        cmd = "echo '" + ns + "\tIN\tA\t" + ns_ip + "' >> " + zone_create
        self.call.request(cmd)

        # 재시작
        cmd = "systemctl restart named" 
        self.call.request(cmd)

        

    # DNS slave서버 설정
    def dnsset_slave(self, dns, update):
        # conf 설정
        print("53번 포트 접근설정을 any로 설정")
        conf_file = "/etc/named.conf"
        cmd = "sed -i 's/listen-on port 53 .*/listen-on port 53 { any; };/g' " + conf_file
        self.call.request(cmd)

        cmd = "sed -i 's/allow-query.*/listen-on port 53 { any; };/g' " + conf_file
        self.call.request(cmd)
        

        # rfc 설정
        print("rfc파일 설정")
        zone_file = "/etc/named.rfc1912.zones"
        cmd = "echo 'zone \"" + dns +"\" IN{\n\ttype slave;\n\tfile \"" + dns + ".zone\";\n\tmasters { " + update + "; };\n};' >> " + zone_file
        self.call.request(cmd)
        

        # 재시작
        print("서비스 재시작")
        cmd = "systemctl restart named" 
        self.call.request(cmd)

    
    # Domain 추가
    def dnszone(self, dns, dn, ip):
        # zone 파일 설정        
        zone_create = "/var/named/" + dns + ".zone"        

        cmd = "echo '" + dn + "\tIN\tA\t" + ip + "' >> " + zone_create
        self.call.request(cmd)

        # 재시작
        cmd = "systemctl restart named" 
        self.call.request(cmd)
        


    
    # DHCP Pool 설정
    def dhcpset(self, ni, ni_sub, gateway, gw_sub, start_ip, end_ip): # DHCP 설정.
        #conf 설정
        print("DHCP pool 설정")
        file = "/etc/dhcp/dhcpd.conf"
        cmd = "cat " + file
        reading = self.call.request(cmd) 
        if reading not in "ddns-update-style interim;":
            cmd = "echo 'ddns-update-style interim;' >> " + file
            self.call.request(cmd)
            
        cmd = "echo 'subnet "+ ni + " netmask " + ni_sub + " {\n\toption routers " + gateway + ";\n\toption subnet-mask " + gw_sub +";\n\trange dynamic-bootp " + start_ip + " " + end_ip +";\n\toption domain-name-servers 8.8.8.8;\n\tdefault-lease-time 10000;\n\tmax-lease-time 5000;\n}' >> " + file
        self.call.request(cmd)

        # 재시작
        cmd = "systemctl restart dhcpd" 
        self.call.request(cmd)

    # DHCP static 설정
    def dhcp_static(self, host, mac_add, ip):
        #conf 설정
        file = "/etc/dhcp/dhcpd.conf"
        cmd = "cat " + file
        reading = self.call.request(cmd) 
        if reading not in "ddns-update-style interim;":
            cmd = "echo 'ddns-update-style interim;' >> " + file
            self.call.request(cmd)
        
        cmd = "echo 'host " + host + " {\n\thardware ethernet " + mac_add + ";\n\tfixed-address " + ip + ";\n}' >>" + file
        self.call.request(cmd)

        # 재시작
        cmd = "systemctl restart dhcpd" 
        self.call.request(cmd)

    # Samba 서버 설정
    def smbset(self, user, smb_user, comment, allow_ip, path):
        file = "/etc/samba/smb.conf"    
        que = input("사용자를 새로 생성하시겠습니까? [y]/n ")
        if que != "n":
            cmd = "useradd -s /sbin/nologin " + user
            self.call.request(cmd)
        que = input("SMB 사용자를 새로 생성하시겠습니까? [y]/n ")
        if que != "n":
            cmd = "smbpasswd -a " + smb_user
            self.call.request(cmd)
        cmd = "echo '[smb]\ncomment = " + comment + "\nhosts allow = " + allow_ip + "\npath = " + path + "\nread only = no\nvalid users = " + user + "@" + smb_user + "\nwrite list = " + user + "@" + smb_user +" ' >> " + file
        self.call.request(cmd)

        # 재시작
        cmd = "systemctl restart smb nmb" 
        self.call.request(cmd)

    # SMB 마운트
    def mount(self, ip, file_name, path, smb_user, pw):
        cmd = "mount -t cifs //" + ip + file_name + " " + path + " -o username='" + smb_user + "',password='" + pw + "'"
        ans = self.call.request(cmd)
        print(ans)
