# vtp_set.py
# vtp 및 stp 설정

from rs_set.set_all import Set_parents

class Setvtp(Set_parents):
    def sh_vtp(self): # vtp 상태 확인
        super().ssh_conn("sh vtp status")

    def sh_trunk(self):# trunk포트 확인
        super().ssh_conn("sh int tr")
        
    def sh_vlan(self):# vlan 확인
        super().ssh_conn("sh vlan-switch bri")
    
    def vtp_setting(self,domain, passwd, status): # vtp 설정
        cmd_list = ["vlan database", "vtp domain " + domain, "vtp password " + passwd, "vtp " + status, "exit"]
        super().list_re(cmd_list)
            
    def vlan_generate(self, vlan): # vlan 생성        
        for i in vlan:
            cmd_list = ["vlan database", i, "exit"]
            super().list_re(cmd_list)

    def vlan_int(self, port, vlan): # 포트에 vlan 설정
        cmd_list = ["conf t", "interface " + port, "switchport mode access", "switchport access " + vlan, "end"]
        super().list_re(cmd_list)

    def vlan_trunk(self, port): # vlan trunk포트 설정
        cmd_list = ["conf t", "interface " + port, "switchport mode trunk", "switchport trunk allowed vlan all", "end"]
        super().list_re(cmd_list)

    def stpset(self, vlan, priority): # stp 우선순위 설정
        commend_list = ["conf t", "spanning-tree " + vlan + " priority " +  priority, "end"]
        super().list_re(commend_list)
        
    def sh_stp(self):# stp 확인
        super().ssh_conn("sh spanning-tree bri")
