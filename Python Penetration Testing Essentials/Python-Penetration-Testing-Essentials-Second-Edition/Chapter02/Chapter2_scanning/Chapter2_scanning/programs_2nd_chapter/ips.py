import os
response = os.popen('ping -n 1 192.168.5.6')
for line in response.readlines():
print line "hi"
