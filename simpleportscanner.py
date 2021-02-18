# this program is created by ams_programmer

from socket import *
import optparse
from threading import *


def main():
    parser = optparse.OptionParser("Usage of prorgam: " + '-H <target host>  -p <target port> ')
    parser.add_option('-H' ,dest='Thost' , type= 'string' , help = "enter target host here")
    parser.add_option('-p',dest='Tport' , type = 'string' , help = "enter target port here")
    (options , args) = parser.parse_args()
    targethost = options.Thost
    targetport = str(options.Tport).split(',')
    if((targethost == None) | (targetport[0] == None)):
        print(parser.usage)
        exit(0)

    Scanner(targethost,targetport)


def sockscan(targethost,targetport):
    try:
        st = socket(AF_INET , SOCK_STREAM)
        st.connect((targethost,targetport))
        print(f"[+]{targetport} tcp is open :)")
    except:
        print(f"[-]{targetport} tcp is closed !!!")
    finally:
        st.close()


def Scanner(targethost,targetport):
    try:
        targetip = gethostbyname(targethost)
    except:
        print("cant find host with the specify text")
        exit(0)
    try:
        targetname = gethostbyaddr(targetip)
        print("scan results for:" + targetname[0])
    except:
        print("scan result for:" + targetip)
    setdefaulttimeout(1)
    
    for tport in targetport:
        t = Thread(target=sockscan,args=(targethost , int(tport)))
        t.start()

if(__name__ == '__main__'):
    main()
