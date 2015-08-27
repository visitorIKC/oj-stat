import requests
import re

supportStatus = {"ac","na"}
errorMsg = "Error : tioj fetcher only supports AC and NA."

def fetch_user(uname,status):
	if not status in supportStatus:
		print (errorMsg)
		yield errorMsg
		return
	html = requests.get("http://tioj.ck.tp.edu.tw/users/"+uname).text

	html = html.split("<tbody>",1)[1].split("</tbody>")[0]
	html = html.replace("<tr>","").replace("</tr>","")
	html = html.replace("<td>","").replace("</td>","")
	html = re.sub(r" {2,}","",html)
	html = re.sub(r"\n{2,}","\n",html)

	for line in html.split("\n"):
		if line == "": continue
		pid = int(re.search(r"problems\/(\d+)\/submissions",line).group(1))
		if status == "ac" and line.find("text-success") != -1:
			yield pid
		elif status == "na" and line.find("text-warning") != -1:
			yield pid

def get_url(prob):
	if prob == errorMsg:
		return "http://tioj.ck.tp.edu.tw/";
	return "http://tioj.ck.tp.edu.tw/problems/"+str(prob)
