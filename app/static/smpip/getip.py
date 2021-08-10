import os
import re
import requests as req

os.system('ifconfig > /tmp/iplog.log')

with open('/tmp/iplog.log') as f:
    c = f.read()
    data = ' '.join(re.findall('inet (192\.168\.\d+\.\d+)', c))
    #req.post('http://localhost:5000/smpip', {'ip': data})
    req.post('http://fuweiji.pythonanywhere.com/smpip', {'ip': data})
