#!/usr/bin/env python
# coding=utf-8
import optparse
# import socket
from socket import *
# import threading
from threading import *

mutexLock = Semaphore(value=1)
def connScan(host,tgtport):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((host,tgtport))
        connSkt.send('HelloWorld\r\n')
        res = connSkt.recv(1024)
        mutexLock.acquire()
        print "[+] %d/tcp open : %s " % (tgtport,str(res))
    except:
        mutexLock.acquire()
        print "[+] %d/tcp closed" % tgtport
    finally:
        mutexLock.release()
        connSkt.close()

def portScan(host,ports):
    try:
        targetIP = gethostbyname(host)
    except:
        print '[-] Can\'t resolve "%s" : Unknown host' % host
        return
    try:
        targetName = gethostbyaddr(targetIP)
        print '[+] Scan results for : ' + targetName[0]
    except:
        print '[+] Scan results for : ' + targetIP
        setdefaulttimeout(1)
        for tgtport in ports:
            # print '[+] Scanning port : ' + tgtport
            t = Thread(target=connScan,args=(host,int(tgtport)))
            t.start()

def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='target_host', type='string')
    parser.add_option('-p', dest='target_port', type='int')
    (options, args) = parser.parse_args()
    host = options.target_host
    port = options.target_port
    if host == None | port == None:
        print parser.usage
        exit(0)
    portScan(host,port)
