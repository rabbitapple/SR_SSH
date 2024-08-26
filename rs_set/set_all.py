#set_all.py
from netmiko import ConnectHandler #ssh 모듈

class Set_parents:
    def __init__(self, conn):
        self.conn = conn
        
    def ssh_conn(self, commend):
        cmd = self.conn.send_command(commend, expect_string="#")
        print(cmd)

    def list_re(self, commend_list):
        for i in commend_list:
            self.ssh_conn(i)

    def return_res(self, commend):
        cmd = self.conn.send_command(commend, expect_string="#")
        return cmd