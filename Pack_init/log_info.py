# log_info.py

class Log_info_class:
    def __init__(self):
        #로그 정보파일 리스트화
        self.log_location = 0
        self.log_info = []
        self.log_info_list = []
    
        with open("./Pack_init/conf3/log.conf3", "r", encoding = "UTF-8") as self.log_info_file:
            self.log_info_all = self.log_info_file.read()
        # self.log_info_file = open("./log.txt", "r", encoding #= "UTF-8")
        # self.log_info_all = self.log_info_file.read()
        # self.log_info_file.close()
        self.log_info_list = self.log_info_all.split("\n")

        for i in range(1, len(self.log_info_list)):
            self.log_info.append(self.log_info_list[i].split("::"))
            

                   
        
        

    def log_info_return(self):
        return self.log_info

    def find_log_location(self, service):
        for j in range(len(self.log_info_list)-1):
            if service in self.log_info_list[j+1]:
                self.log_location = j
        return self.log_location

    def service_name(self):
        service = []
        
        for i in range(len(self.log_info_list)-1):
            service.append(self.log_info[i][0])
        return service

    def service_log_location(self, service):
        self.find_log_location(service)
        return self.log_info[self.log_location][1]

    def service_log_keyword(self, service):
        self.find_log_location(service)
        return self.log_info[self.log_location][2]
        