#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

f=cgi.FieldStorage()
cmd=f.getvalue("x")

if "run" in cmd and "pod" in cmd:
	s=cmd.split(" ")
	name=s[2]
	image=s[4]
	op=subprocess.getoutput("sudo kubectl run "+name+" --image="+image)

elif "run" in cmd and "deployment" in cmd:
	s=cmd.split(" ")
	name=s[2]
	image=s[4] 
	op=subprocess.getoutput("sudo kubectl create deployment "+name+" --image="+image)

elif "expose" in cmd and "deployment" in cmd and "port" in cmd:
	s=cmd.split(" ")
	name=s[2]
	port=s[5]
	op=subprocess.getoutput("sudo kubectl expose deployment "+name+" --port="+port+" --type=NodePort")

elif "scale" in cmd and "deployment"  in cmd:
	s=cmd.split(" ")
	name=s[2]
	no=s[4]
	op=subprocess.getoutput("sudo kubectl scale deployment "+name+" --replica="+no)

elif "delete" in cmd and "entire" in cmd:
	op=subprocess.getoutput("sudo kubectl delete all -all")

elif "delete" in cmd:
	if "pod" in cmd:
		s=cmd.split(" ")
		name=s[1]
		op=subprocess.getoutput("sudo kubectl delete pod "+name)
	elif  "deployment" in cmd:
		s=cmd.split(" ")
		name=s[1]
		op=subprocess.getoutput("sudo kubectl delete deployment "+name)

else
	op="please check your input"

print("<pre>")
print(output)
print("</pre>")



