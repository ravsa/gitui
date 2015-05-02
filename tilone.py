from subprocess import *
import sys
child='curl '+'-u '+"'"+sys.argv[1]+"'"+':'+"'"+sys.argv[2]+"'"+' https://api.github.com/user/repos '+'-d '+'"'+'{'+'\\"name\\"'+':'+'\\"'+sys.argv[2]+'\\"'+'}'+'"'
cho,chr=Popen(child,shell=True,stdout=PIPE,stderr=PIPE).communicate();
print cho ,chr

