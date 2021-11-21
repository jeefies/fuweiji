from urllib import request as urlreq
from subprocess import call

#urlreq.urlretrieve('http://0.0.0.0:5000/static/smpip/getip.py', '/home/pi/.getip.py')
urlreq.urlretrieve('http://fuweiji.pythonanywhere.com/static/smpip/getip.py', '/home/pi/.getip.py')

content = b"""[Unit]
Description=Smp Ip send

[Service]
ExecStart=/usr/bin/python3 /home/pi/.getip.py

[Install]
WantedBy=multi-user.target
"""

with open("/etc/systemd/system/smpip.service", "wb") as f:
    f.write(content)

call("sudo systemctl enable smpip.service")
