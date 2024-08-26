class Service_info_class:
    def __init__(self, service):
        #로그 정보파일 리스트화
        self.service_location = 0
        self.service_info = []
        self.service_info_list = []
    
        with open("./Pack_init/conf3/service.conf3", "r", encoding = "UTF-8") as self.service_info_file:
            self.service_info_all = self.service_info_file.read()

        self.service_info_list = self.service_info_all.split("\n")

        for i in range(1, len(self.service_info_list)):
            self.service_info.append(self.service_info_list[i].split("::"))
        
        for j in range(len(self.service_info_list)-1):
            if service in self.service_info_list[j+1]:
                self.service_location = j
    # 서비스 정보
    def service_info_return(self):
        return self.service_info
        
    #서비스 정보 라인
    def find_service_line(self):
        return self.service_location

    def name2service(self, os):
        if os == "Ubuntu":
            os_code = 2
        else:
            os_code = 1

        service_name = self.service_info[self.service_location][os_code]
        return service_name
