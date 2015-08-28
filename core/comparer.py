import sys
from core.oj import oj

def _fetch(judge_user):
	judge,user = judge_user.split(":",1)
	return oj.fetch_user(judge,user)
	
def _process(expression):
	# by visitorIKC
	Infinity_Number=2147483647
	#print(expression)
	add = expression.rfind('+')
	sub = expression.rfind('-')
	ins = expression.rfind('&')
	brc = expression.rfind(')')
	if max(add,sub,ins,brc) == -1:
		return _fetch(expression)
	if add == max(add,sub,ins,brc):
		return _process(expression[:add]) | _process(expression[add+1:])
	if sub == max(add,sub,ins,brc):
		return _process(expression[:sub]) - _process(expression[sub+1:])
	if ins == max(add,sub,ins,brc):
		return _process(expression[:ins]) & _process(expression[ins+1:])
	brcin = 1  # The pointer is now in how many pairs of ()
	nowindex = brc - 1
	while brcin != 0:
		if expression[nowindex] == ')':
			brcin += 1
		elif expression[nowindex] == '(':
			brcin -= 1
		nowindex -= 1
	if nowindex == -1:
		return _process(expression[1:len(expression)-1])
	add = expression.rfind('+',0,nowindex+1)
	sub = expression.rfind('-',0,nowindex+1)
	ins = expression.rfind('&',0,nowindex+1)
	if add == max(add,sub,ins):
		return _process(expression[:add]) | _process(expression[add+1:])
	if sub == max(add,sub,ins):
		return _process(expression[:sub]) - _process(expression[sub+1:])
	if ins == max(add,sub,ins):
		return _process(expression[:ins]) & _process(expression[ins+1:])
	
def compare(expression):
	expression = expression.replace(" ","")
	#print(expression)
	return _process(expression)
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Error: miss expression")
		print("See README.md for help")
		sys.exit()
	expression = sys.argv[1]
	result = list(compare(expression))
	result.sort()
	print("%d problems in total\n"%len(result))
	for prob in result:
		print(prob[0] + " " + str(prob[1]), end="\t")
	print()
	
