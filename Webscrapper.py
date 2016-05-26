import requests

alphanumString = "abcdefghijklmnopqrstuvwkyz1234567890"
alphanum = [c for c in alphanumString]

#add website name
website = ""
git = "http://www." + website + ".com/"

start = 0
end = 37000

def compute():

	for i in range(start,end):

		r = git + getChar(i)
		request = requests.get(r)
		if(404==request.status_code):
			print(getChar(i))

#takes a number and returns a alpha numeric number
def getChar(num):
	tempNum = num
	repeat = 1
	length = len(alphanum)
	while(tempNum>length):
		tempNum = tempNum/length
		repeat = repeat+1

	tempString = ""
	tempNum = num
	while(repeat>0):
		tempString = tempString + alphanum[(tempNum%(length+1)-1)]
		tempNum = tempNum/length
		repeat = repeat-1

	return tempString


if __name__ == "__main__":
	compute()
