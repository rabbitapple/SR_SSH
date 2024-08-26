# 기본설정 

from rs_set.set_all import Set_parents

class Setdefault(Set_parents): 
    def setintip(self, port, set_ip, set_sm): # 인터페이스 ip설정
        commend_list = ["conf t", "interface " + port, "ip add " + set_ip + " " + set_sm, "end"]
        super().list_re(commend_list)

    def set_noshut(self, port): # no shutdown입력
        commend_list = ["conf t", "interface " + port, "no shutdown", "end"]
        super().list_re(commend_list)

    def int_ip(self): # 인터페이스 정보
        super().ssh_conn("sh ip int bri")
        
    def set_rout(self, ni, ni_sm, transeport): # 라우팅 테이블 설정
        commend_list = ["conf t", "ip route " + ni + " " + ni_sm + " " + transeport, "end"]
        super().list_re(commend_list)

    def sh_route(self): # 라우팅 테이블 정보확인
        super().ssh_conn("sh ip ro")

    def capsul(self, vlan): # intervlan 캡슐화
        commend_list = ["conf t", "encapsulation dot1Q " + vlan , "end"]
        super().list_re(commend_list)

    def backup(self, name): # 설정 백업
        vlanl = []
        vlant = ""
        content = super().return_res("sh run")
        vlan = super().return_res("sh vlan-switch bri")
        vlans = vlan.split(" ")
        for i in vlans:
            j = 0
            if "VLAN" in i:
                j += 1
                vlanl.append(i.split("\t"))

        for k in range(j):
            vlant = vlant + vlanl + "\n"

        with open("./data/" + name + ".rsup", "w", encoding = "UTF-8") as backup_file:
            backup_file.write(content + "\n+++++ VLAN +++++\n" + vlant)

    

    def upload(self, name):
        with open("./data/" + name + ".rsup", "r", encoding = "UTF-8") as backup_file:
            backup = backup_file.read()
        
        backup_list = backup.split("\n+++++ VLAN +++++\n")
        shrun = backup_list[0].split("\n")
        vlan = backup_list[1].split("\n")


        super().return_res("conf t")
        super().list_re(shrun)
        super().return_res("end")
            
        for j in vlan:
            cmd_list = ["vlan database", vlan + " " + j, "exit"]
            super().list_re(cmd_list)

