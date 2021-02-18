# this program is created by ams_programmer

from socket import *
import optparse
from threading import *

def conscan(tgtHost,tgtPorts):
    try:
        sock = socket(AF_INET , SOCK_STREAM)
        sock.connect((tgtHost,tgtPorts))
        print(f"[+]{tgtPorts} tcp is open :)")
    except:
        print(f"[-]{tgtPorts} tcp is closed !!!")
    finally:
        sock.close()

def PortScanner(tgtHost,tgtPorts):
    try:
        targetip = gethostbyname(tgtHost)
    except:
        print("Unknown Host !!!")

    try:
        targetname = gethostbyaddr(targetip)
        print("scan results for:" + targetname[0])
    except:
        print("scan result for:" + targetip)
    setdefaulttimeout(1)
    
    for tgtport in tgtPorts:
        t = Thread(target=conscan,args=(tgtHost , int(tgtport)))
        t.start()


def main():
    parser = optparse.OptionParser("Usage of prorgam: " + '-H <target host>  -p <target port> ')
    parser.add_option('-H' ,dest='tgthost' , type= 'string' , help = "specify target host")
    parser.add_option('-p',dest='tgtports' , type = 'string' , help = "specify target ports seperated by comma")
    (options , args) = parser.parse_args()
    tgtHost = options.tgthost
    tgtPorts = str(options.tgtports).split(',')
    if((tgtHost == None) | (tgtPorts[0] == None)):
        print(parser.usage)
        exit(0)

    PortScanner(tgtHost,tgtPorts)
if(__name__ == '__main__'):
    main()
