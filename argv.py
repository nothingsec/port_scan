#!/usr/bin/env python
# coding=utf-8

import sys
import os
import socket
import IPy # 处理ip的库

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        # print str(ip),port
        s.connect((str(ip), port))
        print '[+] Discover ' + str(ip) + ' : ' + str(port)
        try:
            banner = s.recv(1024)
            s.close()
            return banner,True
        except:
            print "No banner"
            return "No banner",True
    except Exception, e:
        return "No banner",False

def checkVuln(port,banner):
    f = open("port_banner.txt", 'r')
    # f.write(banner+"\n")
    for line in f.readlines():
        info = line.split(' ')[0]

        if info.split(','):
            info = info.split(',')
        try:
            if info[0].split('#'):
                # print info[0]
                info2 = []
                for i in range(int(info[0].split('#')[0]),int(info[0].split('#')[1])+1):
                    info2.append(i)
                info = info2
        except:
            pass
        else:
            info = list(info)
        if port in info:
            print '[+] Port ' + str(port) + ' in this file is ' + line.strip('\n')
            try:
                print '[+] Server is vulnerable: ' + banner.strip('\n')
            except:
                pass
def main():
    if len(sys.argv) == 2:
        # filename = sys.argv[1]
        # if not os.path.isfile(filename):
        #     print "[-] " + filename + ' does not exist.'
        #     exit(0)
        # if not os.access(filename, os.R_OK):
        #     print '[-] ' + filename + ' access denied.'
        #     exit(0)
        portList = [21,22,23,80,81,82,83,84,85,86,87,89,161,389,443,445,512,513,514,873,1025,111,1433,1521,2082,2083,2222,2601,2604,3128,3306,3312,3311,3389,4440,5432,5900,5984,6082,6379,7001,7002,7778,8080,8080,8089,9090,8083,8649,8888,9200,9300,10000,11211,27017,27018,28017,50000,50070,50030]
        ip = sys.argv[1]
        try:
            ip = IPy.IP(ip)
        except Exception, e:
            print '[-]Error IP ：' + str(e)
            return
        for port in portList:
            # if
            banner,status = retBanner(ip,port)
            if status:
                checkVuln(port, banner)

    else:
        print '[-] Usage: ' + str(sys.argv[0]) + ' <ip or ip/24>'
        exit(0)


        print "[+] Reading Vuln From " + filename

if __name__ == '__main__':
    main()