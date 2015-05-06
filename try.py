import pexpect
child=pexpect.spawn('git push -u origin master')
child.expect('Username')
child.sendline('ravsa')
child.expect('Password')
child.sendline('ravsa150')
print "done"
