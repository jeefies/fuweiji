from urllib import request as urlreq

#urlreq.urlretrieve('http://0.0.0.0:5000/static/smpip/getip.py', '/home/pi/.getip.py')
urlreq.urlretrieve('http://fuweiji.pythonanywhere.com/static/smpip/getip.py', '/home/pi/.getip.py')

content = b"""#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

sudo python /home/pi/.getip.py
exit 0
"""

with open('/etc/rc.local', 'wb') as f:
    f.write(content)

