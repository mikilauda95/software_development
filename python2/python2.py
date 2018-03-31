import string
import pickle
import socket
import sys
import re
import datetime
import calendar

# Define function for reading a line (until "\n")
def recvline(sock):
	line=""
	while True:
		a=sock.recv(1)
		line+=a
		if a=='\n':
			break
	#print line
	return line
def findw(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

#Open the connection
sock = socket.socket()
sock.connect(("127.0.0.1", 9999))
recvline(sock)

message="mikilauda"
message+='\n'
sock.send(message)

recvline(sock)

#Hardcode the secret message
message="e170f0ca3304f370139a297c0138afb8"
message+='\n'

sock.send(message)

recvline(sock)
recvline(sock)

# Start from this value and then do the binary search
start=(2**20)/2 #first guess
a=0
num=start
bigger="bigger"
smaller="smaller"
while True:
	a+=1
	sock.send(str(num)+'\n')
	line=recvline(sock)
	if smaller in line.split( ):
		num-=start/(2**a)
	elif bigger in line.split( ):
		num+=start/(2**a)
	else:
		break

# Guess the the numbers drawn with asterisks
numbers=[]
num1=""
num2=""
num3=""
modnum3=""
lnum1=[]
lnum2=[]
lnum3=[]
for i in range(1,8):
	num1+=sock.recv(7)
	num1+='\n'
	sock.recv(9)
	num2+=sock.recv(7)
	num2+='\n'
	sock.recv(9)
	num3+=recvline(sock)

a=0
for line in num3.split('\n'):
	a+=1
	if a==8:
		break
	line+=' '*(7-len(line))
	line+='\n'
	modnum3+=line

five='#######\n#      \n#      \n ##### \n      #\n#     #\n ##### \n'
onee='   #   \n  ##   \n # #   \n   #   \n   #   \n   #   \n ##### \n'
nine=' ##### \n#     #\n#     #\n ######\n      #\n#     #\n ##### \n'
eigh=' ##### \n#     #\n#     #\n ##### \n#     #\n#     #\n ##### \n'
thre=' ##### \n#     #\n      #\n ##### \n      #\n#     #\n ##### \n'
zero='  ###  \n #   # \n# #   #\n#  #  #\n#   # #\n #   # \n  ###  \n'
sixx=' ##### \n#     #\n#      \n###### \n#     #\n#     #\n ##### \n'
four='#      \n#    # \n#    # \n#######\n     # \n     # \n     # \n'
twoo=' ##### \n#     #\n      #\n ##### \n#      \n#      \n#######\n'
seve='#######\n#    # \n    #  \n   #   \n  #    \n  #    \n  #    \n'

numbers=[zero,onee,twoo,thre,four,five,sixx,seve,eigh,nine]

toguess=[num1,num2,modnum3]
guessed=""
for num in toguess:
	for orig in numbers:
		if num==str(orig):
			#print("found")
			guessed+=str(numbers.index(num))
			break

guessed+='\n'
#print guessed


recvline(sock)
recvline(sock)
sock.send(guessed)
recvline(sock)
recvline(sock)
line=""
for i in range(0,8):
	line+=recvline(sock)

recvline(sock)
recvline(sock)
result=pickle.loads(line)
micros=str(result.microsecond)
micros+='\n'
sock.send(micros)
recvline(sock)
line=recvline(sock)
lline=[word.strip(string.punctuation) for word in line.split()]
date=lline[5:8]

# Build a dictionary for the months and weekdays.
# Can be done using the formatting of datetime
# Dictionary chosen for exercise
d={}
d["Jan"] = "1"
d["Feb"] = "2"
d["Mar"] = "3"
d["Apr"] = "4"
d["May"] = "5"
d["Jun"] = "6"
d["Jul"] = "7"
d["Aug"] = "8"
d["Sep"] = "9"
d["Oct"] = "10"
d["Nov"] = "11"
d["Dec"] = "12"
date[1]=d[date[1]]
#print date[1]
year = int("20"+date[2])
date_obj = datetime.datetime(year, int(date[1]), int(date[0]))
d_days={}
d_days["0"] = "Monday"
d_days["1"] = "Tuesday"
d_days["2"] = "Wednesday"
d_days["3"] = "Thursday"
d_days["4"] = "Friday"
d_days["5"] = "Saturday"
d_days["6"] = "Sunday"

day=d_days[str(date_obj.weekday())]+'\n'

sock.send(day)
recvline(sock)
recvline(sock)
secret=recvline(sock)
secret=secret[:-1]
lsecret=[secret]
print(lsecret)
print(secret)
