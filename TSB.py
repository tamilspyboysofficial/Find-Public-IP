
import urllib


print "   ___________      "
print "   \__    ___/      "
print "     |    |         "
print "     |    |         "
print "     |____|         "
print "  TAMIL SPYBOY  \n"

a=urllib.urlopen('https://ipecho.net/plain\n')
ip=a.read()
print "Your Public IP is-->",ip

