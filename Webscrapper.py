import requests

alphanumString = "abcdefghijklmnopqrstuvwkyz1234567890a"
alphanum = [c for c in alphanumString]

git = "http://www.github.com/"

start = 99
end = 37000

def compute():
	#request = requests.get('http://www.github.com/')

	for i in range(start,end):

		#print(getChar(i))
		r = git + getChar(i)
		request = requests.get(r)
		#print(request.status_code)
		if(404==request.status_code):
			print(getChar(i))
		#if(getChar(i) == "aa"):
		#	print(getChar(i))
	#print(request.status_code)

def getChar(num):
	tempNum = num
	repeat = 1
	length = len(alphanum)
	while(tempNum>length-1):
		tempNum = tempNum/length
		repeat = repeat+1

	tempString = ""
	tempNum = num
	while(repeat>0):
		tempString = tempString + alphanum[tempNum%length]
		tempNum = tempNum/length
		repeat = repeat-1

	return tempString


if __name__ == "__main__":
	compute()
