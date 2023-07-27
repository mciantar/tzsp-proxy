#!/usr/bin/env python3
# Author: Matthew Ciantar
#
# Listens for TZSP on port 37008, extract the encapsulated packet
# and send it to the local interface
#
# Version 1.1
# 2021-04-02
#

import _thread
import fcntl
import socket
import struct

from scapy.all import *

# load tzsp library
load_contrib("tzsp")

def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', bytes(ifname, 'utf-8')[:15]))
    return ':'.join('%02x' % b for b in info[18:24])

mac_str = str(getHwAddr("bond0"))

# extract each packet received and resend it to the local interface
# the original destination mac will be lost
def processPacketCapture ( tzspCapture ):
        try:
             tzspRawPacket = tzspCapture[0]
             tzspPacket = TZSP(tzspRawPacket[UDP].load)
             rawPacket = tzspPacket[2]
             try:
                 rawPacket[Ether].dst = mac_str
                 sendp(rawPacket, iface="bond0", verbose=False)
             except:
                 print("Exception!")
                 print(repr(tzspRawPacket))
        except:
             print("Exception!")

# start sniffing indefinitely
sniff(prn=processPacketCapture, iface="eth0", filter = "udp port 37008", store=0)
