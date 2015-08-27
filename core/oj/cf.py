import requests
import json

supportStatus = {"ac","na"}
errorMsg = "Error : cf fetcher only supports AC and NA"

def fetch_user(uname,status):

	#Wrong-status-error handler
	if not status in supportStatus:
		print (errorMsg)
		yield errorMsg
		return
		
	html = requests.get("https://codeforces.com/api/user.status?from=1&handle="+uname).text
	data = json.loads(html)
	if status == "ac":
		for i in data["result"]:
			if i["verdict"] == "OK" :
				yield cf_prob((i["problem"]["contestId"], i["problem"]["index"]))
	else:
		res = set()
		for i in data["result"]:
			if i["verdict"] != "OK" :
				res.add(cf_prob((i["problem"]["contestId"], i["problem"]["index"])))
		for i in data["result"]:
			if i["verdict"] == "OK" :
				res.discard(cf_prob((i["problem"]["contestId"], i["problem"]["index"])))
		print(len(res));
		for i in res:
			yield i

class cf_prob(tuple):
	def __repr__(self):
		if self[0] >= 100000:
			return "gym"+str(self[0])+self[1]
		else:
			return str(self[0])+self[1]
	
def get_url(prob):
	if prob == errorMsg:
		return "http://codeforces.com/"
	cid, pid = prob
	if cid < 100000:
		return "http://codeforces.com/problemset/problem/"+str(cid)+"/"+pid
	else:
		return "http://codeforces.com/gym/"+str(cid)+"/problem/"+pid
