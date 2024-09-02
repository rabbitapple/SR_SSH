SR_SSH Code Review

 

목차
서론	4
1. Switch/Router Setting Tool	5
1.1.	dhcp	7
1.2.	st_routing_config	7
1.3.	stp_12	7
1.4.	nat	8
1.5.	vtp	8
1.6.	vlan_trunk	9
1.7.	mainfunc	9
2. Server Setting Tool	11
2.1. log_info	13
2.1.1 log_info_class	13
2.2.1. call_log	13
2.2.2. call_log_service(Call_log)	14
2.2.2. call_log_main	14
2.3 paracall	15
2.3.1. Shellcontrol	15
2.4 install_service	16
2.4.1. Install_service	16
2.5. setting	17
2.5.1. Set_service	17
2.5.1. Set_service	18
2.6 service_info	18
2.6.1. Service_info_class	18
2.7. submain	19
2.7.1. Mainfunc	19

 
서론
 
개요
사용자는 계정 정보를 입력하여 SSH에 접속합니다. 이후에 Router/Switch/Server를 질의합니다. 이후 기능/서비스에 대하여 질의하여 상세 기능을 실행합니다. 
질의 중간에 exit를 통해 상위노드로 이동 가능하며 end를 통해 노드를 탈출하여 종료하게 됩니다. 




 
1. Switch/Router Setting Tool
 

개요
Switch 및 Router의 설정 및 제어를 위한 도구입니다.
외부 라이브러리로 cisco의 네트워크 장비에 SSH로 접근을 하는 paramiko를 사용하였습니다. 
DHCP, NAT, VTP, VLAN, STP, 기타 설정과 같이 기능에 따라 모듈들이 구성되어 있으며 추가적으로 mainfunc 모듈에서는 main코드의 가독성을 위한 함수들이 구성되어 있습니다. 
기능구현의 경우 대부분 paramiko로 생성한 세션으로 통신을 하기에 main에서 인스턴스를 생성하여 세션을 연결하고, 이 인스턴스를 함수들이 매개변수로 받아 사용하는 구조로 이루어져 있습니다.


 

Package	Module	Discription
Pack_init	dhcp	DHCP 설정 함수가 포함된 모듈.
	st_routing_config	Router 및 Switch 설정값 확인 함수들이 포함된 모듈.
	stp_12	STP 설정값 및 Priority 설정 함수가 포함된 모듈.
	nat	NAT 설정 확인 함수 및 NAT 설정 방법별 설정 함수가 포함된 모듈.
	vtp	VTP 설정 및 VTP 설정값 확인 함수가 포함된 모듈.
	vlan_trunk	VLAN, Trunk 인터페이스 설정값 확인 및 설정 함수들이 포함된 모듈.
	mainfunc	명령 수동 입력 및 기타 설정 함수, 메인코드에 사용될 함수가 포함된 모듈.
main	메인 코드.

 
1.1.	dhcp
개요
DHCP 관련 함수들이 포함된 모듈입니다.
DHCP Pool 설정 및 DHCP Pool 확인을 하는 함수가 포함되어 있습니다. 
Function
Discription	Parameter	Return
dhcp_set(net_connect)	DHCP 설정 함수. 	SSH Session Instence	x
dhcp_sh(net_connect)	DHCP Pool 확인 함수.	SSH Session Instence	x



1.2.	st_routing_config
개요
라우팅 테이블 설정 함수가 포함된 모듈입니다. 
Function
Discription	Parameter	Retrurn
st_ro(net_connect, 
d_ip, sm, n_ip)	라우팅 테이블 추가 함수. 	SSH Session Instence
목적지 ip
서브넷마스크
next hop ip 	x



1.3.	stp_12
개요
STP 관련 함수가 포함된 모듈입니다. 
STP Priority 설정 확인 함수 및 STP 테이블 확인 함수가 포함되어 있습니다. 

Function
Discription	Parameter	return
stp_ro(conn, vlan, pri)	STP Priority 설정 함수. 	SSH Session Instence
VLAN 영역
Priority	x
stp_sh(conn)	STP 테이블 확인 함수.	SSH Session Instence	x

1.4.	nat
개요
NAT 관련 함수가 포함된 모듈입니다. 
NAT 설정 방법에 따라 정적 NAT, 동적 NAT, PAT 설정 함수가 포함되어 있습니다. 

Function
Discription	Parameter	Return
static_nat_(net_con)	정적 nat 설정 함수.	SSH Session Instence	x
dynamic_nat_(net_con)	동적 nat 설정 함수.	SSH Session Instence	x
pat_(net_con)	동적 pat 설정 함수.	SSH Session Instence	x



1.5.	vtp
개요
VTP 관련 함수가 포함된 모듈입니다. 
Trunk포트 설정 함수 및 VTP 상태 확인 함수가 포함되어 있습니다. 

Function
Discription	Parameter	Retrun
trunk_cr(conn)	trunk 포트 설정 함수.	SSH Session Instence	x
vtp_sta(conn)	vtp상태 확인 함수.	SSH Session Instence	x

 
1.6.	vlan_trunk
개요
VLAN 및 Trunk 인터페이스 관련 함수가 포함된 모듈입니다.
VLAN 확인 및 생성, 포트 할당, 

Function
Discription	Parameter	Return
vlan_show(conn)	vlan 확인 함수.	SSH Session Instence	x
vlan_cr(conn)	vlan 생성 함수.	SSH Session Instence	x
vlan_acc(conn)	vlan 포트 할당 함수.	SSH Session Instence	x
trunk_show(conn)	trunk interface확인 함수.	SSH Session Instence	x
trunk_cr(conn)	trunk 생성 함수.	SSH Session Instence	x



1.7.	mainfunc
개요
기타 설정 및 메인 코드 관련 함수가 포함된 모듈입니다.
기타 설정 함수는 SSH를 통한 명령 전달 함수, 인터페이스 정보, IP 할당, no shutdown 함수, 설정값 백업 함수, 라우팅 테이블 정보 확인 함수, Intervlan 캡슐화 함수가 포함되어 있습니다.
메인코드 관련 함수는 메뉴판 출력 및 메뉴판 dictionary 반환 함수 및 기능 구현 함수로 이루어져 있습니다.
Function
Discription	Parameter	Return
return_res(conn, commend)	SSH를 통한 명령 전달 결과를 반환 함수. 	SSH Session Instence
SSH 명령어	명령 전달
결과값
print_res(conn, commend)	SSH를 통한 명령 전달 결과를 출력 함수. 	SSH Session Instence
SSH 명령어	X
list_res(conn, commend_list)	SSH를 통한 명령 전달 결과를 출력 함수. 	SSH Session Instence
SSH 명령어 리스트	X
int_ip(conn)	인터페이스 정보 확인 함수.	SSH Session Instence	X
setintip(conn, port,
set_ip, set_sm)	인터페이스 ip설정 함수.	SSH Session Instence
Interface, IP, SM	X
set_noshut(conn, port)	no shutdown입력 함수. 	SSH Session Instence
Interface	X
backup(conn, name)	설정 백업 함수.	SSH Session Instence
서비스명	X
set_rout(conn, ni
ni_sm, transeport)	라우팅 테이블 설정 함수.	SSH Session Instence, 
NI, SM, Transeport	X
sh_route(conn)	라우팅 테이블 정보확인 함수.	SSH Session Instence	X
capsul(conn, vlan)	intervlan 캡슐화 함수. vlan 값을 매개변수로 받는다.	SSH Session Instence
VLAN	X
step3_1_1(conn)	명령어 입력 함수.	SSH Session Instence	X
step3_1_2(conn)	인터페이스 정보 함수.	SSH Session Instence	X
step3_1_3(conn)	인터페이스 ip설정 함수.	SSH Session Instence	X
step3_1_4(conn)	no shutdown 설정할 인터페이스 입력 함수.	SSH Session Instence	X
step3_1_5(conn)	설정 백업 파일명 입력 함수.	SSH Session Instence	X
step3_1_6(conn)	라우팅 테이블 설정 함수.	SSH Session Instence	X
step3_1_7(conn)	라우팅 테이블 정보 확인 함수.	SSH Session Instence	X
step3_1_8(conn)	vlan 캡슐화 함수.	SSH Session Instence	X
step3_2_1(conn)	vtp상태 확인 함수.	SSH Session Instence	X
step3_2_2(conn)	trunk interface확인 함수.	SSH Session Instence	X
step3_2_3(conn)	vlan 확인 함수.	SSH Session Instence	X
step3_2_4(conn)	vlan 생성 함수.	SSH Session Instence	X
step3_2_5(conn)	인터페이스에 vlan 설정 함수.	SSH Session Instence	X
step3_2_6(conn)	trunk포트 설정 함수.	SSH Session Instence	X
step3_2_7(conn)	vtp 설정 함수.	SSH Session Instence	X
step3_3_1(conn)	stp 정보 확인 함수.	SSH Session Instence	X
step3_3_2(conn)	stp 우선순위 설정 함수.	SSH Session Instence	X
step3_4_1(conn)	DHCP Pool 확인 함수.	SSH Session Instence	X
step3_4_2(conn)	DHCP 설정 함수.	SSH Session Instence	X
step3_5_1(conn)	nat 정보 확인 함수.	SSH Session Instence	X
step3_5_2(conn)	Static NAT 설정 함수.	SSH Session Instence	X
step3_5_3(conn)	Daynamic NAT 설정 함수.	SSH Session Instence	X
step3_5_4(conn)	PAT 설정 함수.	SSH Session Instence	X
step3_1_dic()	default 설정 dic 반환 함수.	X	menu
dictionary
step3_2_dic()	vtp 설정 dic 반환 함수.	X	menu
dictionary
step3_3_dic()	stp 설정 dic 반환 함수.	X	menu
dictionary
step2()	스위치 초기 메뉴 및 dic 반환 함수.	X	menu
dictionary
step3_1_dic_ro()	default 라우팅 설정 dic 반환 함수.	X	menu
dictionary
step3_2_dic_ro()	vtp 설정 dic 반환 함수.	X	menu
dictionary
step3_3_dic_ro()	stp 설정 dic 반환 함수.	X	menu
dictionary
step2_ro()	라우터 초기 메뉴 및 dic 반환 함수	x	menu
dictionary


 
2. Server Setting Tool
 

개요
Server의 Service 설정 및 제어를 위한 도구입니다.
내부 라이브러리의 모듈인 paramiko를 사용하여 SSH를 제어하였습니다.   
서비스의 서비스 명 및 Log파일 위치 등 정보가 담긴 설정파일을 제어하는 메서드를 Log_info_class, Service_info_class를 통해 구현하였습니다.
이외에 Log 확인 class, Service Setting class, Service Install class, Service Status확인 class를 구현하였으며 이를 Submain class에서 사용하여 main code의 가독성을 높이기 위한 메서드를 구현하였습니다. 

추가적으로 conf3설정파일의 설정값을 추가할경우 별도의 코드 수정 없이 설정을 제외한 기본적인 기능의 사용이 가능합니다.
 

Package	Module	Discription
Pack_init	call_log	로그 정보를 확인하는 함수가 포함된 모듈
	ctlsystem	서비스 시작, 종료 및 상태 확인 함수가 포함된 모듈.
	install_service	Samba 설치 함수가 포함된 모듈.
	log_info	로그 정보 확인 함수가 포함된 모듈.
	mainfunc	메인 메뉴 함수가 포함된 모듈.
	paracall	장비 접속 후 os 확인 및 명령 실행 함수가 포함된 모듈.
	service	서비스 정보 리턴 함수가 포함된 모듈.
	setting	서비스 설정 함수가 포함된 모듈.
	submain	서비스 설정 함수가 포함된 모듈.
main	메인 코드.

 
2.1. log_info
개요
Log 정보 및 OS정보 관련 모듈입니다.

2.1.1 log_info_class
개요
Log 정보 및 OS정보 관련 클래스 입니다. 
Log 정보가 포함된 파일에서 Log 정보를 불러오는 메서드 및 정보의 좌표값을 불러오는 메서드와 OS 정보가 포함된 파일에서 OS정보를 불러오는 메서드가 포함되어 있습니다.
Method
Discription	Parameter	Return
__init__()	로그 정보파일을 읽고 가공하여
인스턴스 변수에 선언 및 초기화	X	X
log_info_return()	로그 정보 리턴(log_info)  메서드.	X	X
find_log_location
(service)	설정파일에서 로그파일의 Path값
 좌표 리턴 메서드. service 값을
매개변수로 받는다.	X	X
service_name()	서비스 이름 리턴 메서드.	X	X

2.2 call_log
개요
Paramiko를 통해 Log파일을 읽고 분석하는 모듈입니다.

2.2.1. call_log
개요
Log 관련 클래스입니다.
로그의 출력 및 서비스별 분석을 하는 메서드가 포함된 클래스 입니다. 
Method
Discription	Parameter	return
__init__(conn, service, name)	로그 정보를 리스트화하여 인스턴스 변수에 할당 및 초기화	SSH Session Instence
상세 서비스명
서비스명	X
print_log()	Debian 계열 로그 읽기 메서드.	X	X
ssh_pro()	SSH 로그 분석 메서드	X	X
dhcp_pro()	DHCP로그 분석 메서드	X	X
smb_pro()	SMB 로그분석 메서드	X	X
ftp_pro()	FTP 로그분석 메서드	X	X

2.2.2. call_log_service(Call_log)
개요
Debian 계열 OS의 Log 관련 클래스입니다.
Call_log 클래스의 자식 클래스 입니다.
로그 출력 메서드를 오버라이딩 하며, 필요시 추후 로그 분석 메서드 또한 오버라이딩 할 예정입니다.

Method
Discription	Parameter	Return
print_log()	Ubuntu 계열 로그 출력
메서드. 오버라이딩.	X	X

2.2.2. call_log_main
개요
OS에 따라서 로그를 출력 및 분석하는 메서드가 포함된 클래스 입니다.

Method
Discription	Parameter	Return
prilog(conn, service, name)	OS에 따른 로그를 출력하는 메서드	SSH Session Instence
상세 서비스명
서비스명	X

 
2.3 paracall
개요
OS확인 및 Paramiko를 사용한 명령 전달 관련 모듈입니다.
다른 클래스 및 모듈에서 전반적으로 사용되는 모듈입니다.


2.3.1. Shellcontrol
개요
OS확인 및 Paramiko를 사용한 명령 전달 관련 클래스입니다.
SSH서버의 OS를 리턴하는 메서드와 Paramiko를 통한 명령 전달 후 결과를 출력/리턴하는 메서드가 포함되어 있습니다. 
다른 클래스 및 모듈에서 전반적으로 사용되는 클래스입니다. 

Method
Discription	Parameter	Return
__init__(conn)	SSH 세션 인스턴스를 매개변수로
받아 인스턴스 변수로 선언 및
초기화	SSH Session Instence	X
check_os(commend)	SSH 서버 OS 리턴 메서드.	명령문	OS
request_noprint
(commend)	Paramiko를 통한 명령 전달후 결과 
리턴 메서드	명령문	명령 결과
request(commend)	Paramiko를 통한 명령 전달후 결과 
출력 메서드	명령문	X

 

2.4 install_service
개요
서비스 설치 관련 모듈입니다.


2.4.1. Install_service
개요
서비스 설치 관련 클래스입니다.
서비스를 설치하는 메서드가 포함되어 있습니다.

Method
Discription	Parameter	Return
__init__(conn,
os, service)	인스턴스 변수로 선언 및 초기화.	SSH Session Instence
OS, 
서비스명	X
Install()	서비스 설치 메서드	X	X

 
2.5. setting
개요
서비스 설정 관련 모듈입니다.


2.5.1. Set_service
개요
서비스 설정 관련 클래스입니다.
SSH, Samba, DHCP, DNS Server 서비스 설정 메서드 및 SMB Mount 메서드가
포함되어있습니다.

Method
Discription	Parameter	Return
__init__(conn)	인스턴스 변수로 선언 및
초기화	SSH Session Instence	X
sshset()		SSH PermitRootLogin 설정 메서드.	X	X
dhcpset()	DHCP Pool 설정 메서드.	X	X
dhcp_static()	DHCP IP static 할당 설정 메서드 	X	X
dnsset_master()	DNS Master설정 메서드.	X	X
dnsset_slave()	DNS slave설정 메서드.	X	X
dns_zone()	DNS에 Hostname 추가 메서드	X	X
ftpset()	FTP설정 메서드.	X	X
smbset()	Samba 서버 설정 메서드.	X	X
mount()	SMB 마운트 메서드.	X	X


 
2.8 ctlsystem
개요
systemctl명령어 관련 모듈입니다.


2.8.1. Service_status
개요
Systemctl 명령어 관련 클래스입니다.
서비스 상태 출력 및 서비스 상태 변경 메서드가 포함되어 있습니다. 

Method
Discription	Parameter	Return
status_print()	상태 출력메서드.	X	X
system_start()	서비스 시작 메서드.	X	X
system_stop()	서비스 종료 메서드.	X	X
system_enable()	서비스 실행 설정 메서드.	X	X
system_disable()	서비스 미실행 설정 메서드.	X	X



2.6 service_info
개요
conf3 파일을 통해 서비스 정보를 가공하는 모듈입니다.


2.6.1. Service_info_class
개요
conf3 파일을 통해 서비스 정보를 가공하는 클래스입니다.

Method
Discription	Parameter	Return
service_info_return()	서비스 정보를 리스트화하여 
리턴하는 메서드	X	Service Info
name2service(os)	서비스 이름 리턴 메서드.	X	상세 서비스 명

 

2.7. submain
개요
메인 코드 가독성을 위한 모듈입니다.


2.7.1. Mainfunc
개요
메인 코드 가독성을 위한 클래스입니다.
메인코드에서 사용되는 메뉴판 출력 및 함수 dictionary 리턴메서드 및 기능 구현에 필요한 input값을 받는 메서드가 포함되어 있습니다.
Method
Discription	Parameter	Return
__init__(conn, os
, service, name)	받은 매개변수들을 인스턴스 변수로 선언 및 초기화 이후 import된 
Class들의 인스턴스를 생성	SSH Session Instence	X
dhcp()	DHCP설정 input값을 받는 메서드.	X	X
dns()	DNS설정 input값을 받는 메서드.	X	X
samba()	Samba 서버 설정 input값을 받는 메서드.	X	X
setting()	설치 메뉴 선택 메서드.	X	X
step3()	로그 출력 메서드	X	X
step2_1()	메뉴판 출력 및 dic 리턴 메서드	X	Menu dictionary

 
3. Main Code
 

제어흐름도
메인 코드가 실행이 될 경우 기기명을 물어본 뒤 기기 종류에 맞춰 모듈을 import합니다.
이후 SSH 모듈을 Import한 뒤 첫번째 제어문으로 들어갑니다. 첫번째 제어문에서 메뉴판을 출력을 하고 입력값에 따라 인스턴스 주소가 값인 dictionary 값을 가져와 호출하게 됩니다. 
호출된 인스턴스는 다시 인스턴스 주소가 값인 dictionary를 리턴시키고 이 dictionary로 다시 인스턴스 주소 키값을 구한 뒤 인스턴스를 호출하여 기능을 실행시키게 됩니다. 입력노드에서 올바르지 않은 값을 입력시 제어노드에서 다시 입력노드로 돌아가게 되고 step입력노드의 경우 올바른 값일경우 인스턴스를 호출하며 end를 입력할경우 disconnect노드로, exit를 입력할경우 상위 입력노드로 이동하게 된다.  










           

