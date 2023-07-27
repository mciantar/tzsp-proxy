#### TZSP Proxy

### Problem
There are situation where it is not possible to have sensor (TAP) connected to a SPAN port, but there is the ability to capture traffic using a third party device, like MikroTik, that support TZSP. With a few simple rules, it is possible to capture the desired traffic, and forward it to a sensor. The problem is that most sensor do not understand TZSP encapsulation natively! This scripts resolves the problem but acting as a listener for TZSP, decapsulates them, and forwards them to the listening promiscious interface.

This script is provided as is without warranty. In some cases, the script can crash and I have not investigated this further, so I have a watchdog script to monitor and restart it accordingly.
