#NAT
from rs_set.set_all import Set_parents

class Setnat(Set_parents):
    def nat_status(self):
        super().ssh_conn("sh ip nat translation")
    
    def out_set(self, port):
        commend_list = ["conf t", "interface " + port, "ip nat outside", "end"]
        super().list_re(commend_list)

    def in_set(self, port):
        commend_list = ["conf t", "interface " + port, "ip nat inside", "end"]
        super().list_re(commend_list)

    def static_nat(self, in_ip, out_ip):
        commend_list = ["conf t", "ip nat inside source " + in_ip + " " + out_ip, "end"]
        super().list_re(commend_list)

    def part_nat(self, in_ip, wild_mask, out_ip, out_sm, pool_name):
        commend_list = ["conf t", "access-list 1 permit " + in_ip + " " + wild_mask, "ip nat pool " + pool_name + " " + out_ip + " net mask " + out_sm, "ip nat inside source list 1 pool " + pool_name + " overload", "end"]
        super().list_re(commend_list)
        
    def dynamic_nat(self, in_ip, wild_mask, out_ip, out_sm, pool_name, port):
        commend_list = ["conf t", "interface " + port, "ip address " + out_ip + " " + out_sm + " secondnary", "access-list 1 permit " + in_ip + " " + wild_mask, "ip nat pool " + pool_name + " " + out_ip + " " + in_ip + " netmask " + out_sm, "ip nat inside source list 1 pool " + pool_name, "end"]
        super().list_re(commend_list)