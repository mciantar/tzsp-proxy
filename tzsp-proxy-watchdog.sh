#!/bin/bash
/bin/ps aux | /bin/grep "python3 /usr/local/sbin/tzsp-proxy.py" | /bin/grep -v "grep" || /bin/nohup /usr/local/sbin/tzsp-proxy.py >/dev/null 2>&1 &
