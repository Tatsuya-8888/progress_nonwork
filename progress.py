
import hashlib
import random
from time import sleep

per=0.0


while(True):

	per=per+0.01

	d=str(random.random())
	hs=hashlib.md5(d.encode()).hexdigest()

	text="{0:1.2f}%".format(per)
	print(text,end=" : ")


	for i in hs:
		print(i, flush=True, end="")
		sleep(random.random()/5)

	print("//")
	sleep(random.random())

	if per > 99.0 : per=0.0
