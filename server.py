import socket
import threading
import sys
BUF_SIZ
reply_dic = {'black':'white', 'yin':'yang', 'sun':'earth', 'batman': 'joker' }

def handle_client(cli_s):
	st ='first'
	while st:
		st = cli_s.recv(BUF_SIZ)
		st = st.decode()
		print(cli_s.laddr, " requested for ", st)
		if not st:
			print("connection broken with ", cli_s.laddr)
			return 1
		if st not in reply_dic:
			rep_st = "stupid request"
		else:
			rep_st = reply_dic[st]
		print("\t\t\t sending reply to %s : %s  "%(cli_s.laddr, rep_st))
		rep_st = rep_st.encode()
		cli_s.send(rep_st)
	cli_s.close()
	return 0

request_id = 1
serv_s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
print("socket successfully created")
port = 2020
serv_s.bind((socket.gethostname(),port))

serv_s.listen(5)
thread_lis = []
while True:
	cli_s, addr = serv_s.accept()
	print("\t\t\tGot connection from ", addr)
	thr = threading.Thread(target = handle_client, args = (cli_s))
	thr.start()
	thread_lis.append(thr)

serv_s.close()
