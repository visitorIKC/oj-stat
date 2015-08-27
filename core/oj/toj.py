import requests
import json

supportStatus = {"ac","na"}
errorMsg = "Error : toj only supports AC and NA."

def fetch_user(uid,status):
	if not status in supportStatus:
		print (errorMsg)
		return {errorMsg}
	data = requests.post("http://toj.tfcis.org/oj/be/api", data={"reqtype":status.upper(), "acct_id":uid})
	data = json.loads(data.text)
	return data[status.lower()]

def get_url(prob):
	if prob == errorMsg:
		return "http://toj.tfcis.org/oj/"
	return "http://toj.tfcis.org/oj/pro/"+str(prob)+"/"
