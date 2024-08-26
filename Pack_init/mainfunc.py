# mainfunk.py
import traceback
from netmiko import ConnectHandler #ssh 모듈
from rs_set.main_function import Mainfunc
from rs_set.main_function import Mainfunc_ro
from Pack_init.paracall import Shellcontrol
from Pack_init.log_info import Log_info_class


class Mainfunk(self):
    def serveros(self, conn):
        self.chos = Shellcontrol(conn)
        self.os = self.chos.check_os()

    def makemenu(self):
        mulist = ""
        self.menu = {}
        lo = Log_info_class()
        menu = lo.service_name()
        for i in range(len(menu)):
            mulist = mulist + str(i + 1) + "." + menu[i] + "\n"
            self.menu + {str(i + 1):menu[i]}
        return mulist

    def choicemenu(self):
        run = True
        while run:
            menu = self.makemenu()
            self.service = input(menu)
            if self.service in range(1, len(self.menu)+1):
                run = False


        
    def conn(self, connect_ip, connect_user, connect_passwd):
        run = True
        while run:
            equip = input("switch/router/server? \n")
            if equip == "switch":
                net_connect = ConnectHandler(device_type = "cisco_ios", ip = connect_ip, username = connect_user, password = connect_passwd)
                net_connect.enable()
                self.maincode = Mainfunc(net_connect)
                self.maincode2  = None
                run = False

                
            elif equip == "router":
                net_connect = ConnectHandler(device_type = "cisco_ios", ip = connect_ip, username = connect_user, password = connect_passwd)
                net_connect.enable()
                maincode = Mainfunc_ro(net_connect)
                run = False
                self.maincode = Mainfunc(net_connect)
                self.maincode2  = None

            
            elif equip == "server": 
                self.choicemenu() #self.service
                net_connect = paramiko.SSHClient()
                net_connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                net_connect.connect(connect_ip,22 ,username = connect_user, password = connect_passwd)
                self.serveros() # self.os
                


                
                run = False
                












