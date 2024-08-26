import paramiko
from Pack_init.ctlsystem import Service_status
from Pack_init.paracall import Shellcontrol
import Pack_init.service_list as service_list


class Install_service:
    def __init__(self, conn, os, service):
        self.conn = conn
        self.os_name = os
        self.crt = Shellcontrol(conn)
        if os == "CentOS7":
            self.repo = "yum"
        elif os == "Ubuntu":
            self.repo = "apt"
        else:
            self.repo = "dnf"
        
        
        if os == "Ubuntu":
            self.os_code = 2
        else:
            self.os_code = 1
            
        service_info_cl1 = service_list.Service_info_class(service)
        service_info = service_info_cl1.service_info_return()
        service_line = service_info_cl1.find_service_line()
        
        
        self.system = service_info[service_line][self.os_code]

    def install(self):
        system = self.system
        if self.system == "smb":
            if self.os_name == "Ubuntu":
                system = "samba sambaclient"
            else :
                system = "samba samba-client"

        if "dhcp" in self.system:
            if self.os_name == "Ubuntu":
                system = "isc-dhcp-server"
            elif self.os_name != "Rocky9" :
                system = "dhcp-server"

        if "name" in self.system:
            if self.os_name == "Ubuntu":
                system = "bind9 bind9-utils"
            elif "CentOS" in self.os_name:
                system = "bind bind-chroot bind-utils"            
            else :
                system = "bind bind-utils"

        
        change_commend = self.repo + " -y install " + system
        change_service = self.crt.request(change_commend)
        print(change_service)