# DHCP
from rs_set.set_all import Set_parents

class Setdhcp(Set_parents):
    def set_dhcp_pool(self, start_ip, end_ip, pool_name, net_range, ip_sm, gateway):
        commend_list = ["conf t", "ip dhcp pool " + pool_name, "network " + net_range + " " + ip_sm, "dns-server 8.8.8.8", "default-router " + gateway, "exit", "ip dhcp excluded-address " + start_ip + " " + end_ip, "end"  ]
        super().list_re(commend_list)

    def sh_pool(self):
        super().ssh_conn("sh ip dhcp pool")

    def sh_binding(self):
        super().ssh_conn("sh ip dhcp binding")