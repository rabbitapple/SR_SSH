import paramiko

class Shellcontrol:
    def __init__(self, conn):
        self.conn = conn
    
    # 명령 실행 후 결과 리턴
    def request(self, commend):
        (stdin, stdout, stderr) = self.conn.exec_command(commend)
        outread = stdout.read()
        output = outread.decode("utf-8")
        return output

    # 명령 실행
    def request_noprint(self, commend):
        self.conn.exec_command(commend)

    
    # os 확인 후 리턴.
    def check_os(self):
        keyword_list1 = []
        uname_read = self.request("uname -a")
        
        with open("./Pack_init/conf3/keyword.conf3", "r", encoding = "UTF-8") as keyword_os:
            keyword_all = keyword_os.read()
            keyword_list = keyword_all.split("\n")
            for i in keyword_list:
                keyword_list1.append(i.split(" : "))
        
        for j in range(len(keyword_list)):
            if keyword_list1[j][1] in uname_read:
                self.os_name = keyword_list1[j][0]
                
        return self.os_name


    