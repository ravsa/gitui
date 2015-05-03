from subprocess import *
import sys
child='curl '+'-u '+"'"+sys.argv[1]+"'"+':'+"'"+sys.argv[2]+"'"+' https://api.github.com/user/repos '+'-d '+'"'+'{'+'\\"name\\"'+':'+'\\"'+sys.argv[3]+'\\"'+'}'+'"'
cho=call(child,shell=True,stderr=PIPE)
if cho:
	print "Error in communication"

