import os
import re

proxyByEnv = os.getenv('http_proxy')
proxy = None
if proxyByEnv != None and (not not proxyByEnv) :
    pattern = r':'
    proxyList = re.split(pattern, proxyByEnv)
    proxyList[1] = proxyList[1].replace('/', '') 
    proxy=(proxyList[0], proxyList[1], proxyList[2])

print(f'  Proxy settings in environment variables: {proxy}\n')



