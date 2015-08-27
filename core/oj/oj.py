from importlib import import_module

ojlist = {"tioj","toj","hoj","cf"}

oj_class = {}
for i in ojlist:
	oj_class[i] = import_module("core.oj."+i)

def oj(ojname):
	return oj_class[ojname.lower()]

def fetch_user(judge,user,status):
	if status == "all":
		st = list()
		for sta in oj(judge).supportStatus:
			st += oj(judge).fetch_user(user,sta)
		st = map(lambda pid:(judge,pid),st)
	else:
#		print(1)
		st = oj(judge).fetch_user(user,status)
#		print(type(st))
		st = map(lambda pid:(judge,pid),st)
	return set(st)

def get_url(prob):
	judge, pid = prob
	if hasattr(oj_class[judge], "get_url"):
		return oj_class[judge].get_url(pid)
	else:
		return None
