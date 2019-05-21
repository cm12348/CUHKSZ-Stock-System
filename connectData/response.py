from connectData import sign
from connectData import preferList
from connectData import requestForData
import time
import base64

def timeHandle(data):
	data1 = data.split(',')
	dataRes = ''
	for i in data1:
		j = i.split(':')
		timeTupleJ = time.localtime(int(j[0]))
		n = 0
		timeStr = ''
		for k in timeTupleJ:
			if n < 6:
				timeStr +=  str(k)+'-'
				n += 1
		j[0] = timeStr[:-1]
		dataRes += j[0]+':'+j[1]+','
	return dataRes[:-1]

def signUp(text):
	#***
    userName = text[0]
    password = text[1]
    sec_password = str(base64.b64encode(password.encode('utf-8')),'utf-8')
    if sign.checkrepeat(userName) == 1:
        return 'Repeated UserName'
    sign.up(userName, sec_password)
	#1!!!add to database(i:user,password o:add to database)
    return 'True'


def signIn(text):
	#***
    userName = text[0]
    password = text[1]
    pw = str(base64.b64encode(password.encode('utf-8')),'utf-8')
    if sign.checkexist(userName) == 0:
        return '[Error:3] invalid user'
    password1 = sign.logIn(userName)
	#2!!!fetch password according to userName"(i:userName o:password)
	#check if password is correct.
    if pw == password1:
		#3!!!switch user status to 1(i:user o:switch user status to 1)
        sign.inState(userName)
        return 'True'
    else:
        return '[Error:2] Wrong password'

def reqData1(text):
	#***
	stockID = text[0]

	data = requestForData.allData(stockID)
	#4!!!fetch all data from database(i:stockID o:allDataSet)
	
	print (data)
	return data

def reqData2(text):
	#***
	timeStart = text[0]
	stockID = text[1]

	# timeTuple = time.strptime(timeStart,"%Y-%m-%d-%H-%M-%S")
	sec = int(timeStart)
	# sec = time.mktime(timeTuple)
	sec += 1
	data = requestForData.periodData(sec,stockID)
	#5!!!fetch data from database in special time(i:timeList o:dataSet)
	if len(data.split(':')) > 1:
		return data.split(':')[1]

def reqPrefer(text):
	#***
	userName = text[0]

	return preferList.req(userName)
	#6!!!prefer list(i:userName o:list)


def addPrefer(text):
	#***
	userName = text[0]
	stockID = text[1]

	preferList.add(userName,stockID)
	#7!!!preferList.append(i:userName,stockID)
	return 'True'

def logOut(text):
	#***
	userName = text[0]
	sign.outState(userName)
	#8!!!switch user status(i:userName o: switch status to 0).
	return 'True'

def reqStatus(text):
	#***
	userName = text[0]

	#9!!! fetch status(i:userName o:status)
	sign.reqStatus(userName)

	return status

def reqStockList(text):
	#***

	#10!!! fetch all stock name(i:None o: stockList)
	return requestForData.stockList()


def delStock(text):
	#***
	userName = text[0]
	stockID = text[1]

	preferList.dele(userName,stockID)
	#11!!! delete stockID from user's preferList(i:userName,stockID o:prefierList)
	
	return 'True'

def switch(head,text):
	if (head == '1'):
		return signUp(text)
	elif (head == '2'):
		return signIn(text)
	elif (head == '3'):
		return reqData1(text)
	elif (head == '4'):
		return reqData2(text)
	elif (head == '6'):
		return reqPrefer(text)
	elif (head == '7'):
		return addPrefer(text)
	elif (head == '8'):
		return logOut(text)
	elif (head == '9'):
		return reqStatus(text)
	elif (head == 'a'):
		return reqStockList(text)
	elif (head =='b'):
		return delStock(text)
	else:
		return
