import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy,ProxyType
from selenium.webdriver.firefox.options import Options


# Define the command to start Tor. This will depend on your operating system and configuration
command = '<<path_to_Tor>>/tor.exe'

#Start the tor process
tor_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

#Wait for tor to start up!!
time.sleep(10)

#Set up proxy setting for the Firefox browser driver
proxy_settings = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': 'localhost:9050',
    'proxy.socks_proxy':'localhost:9050',
    'proxy.ssl_proxy':'localhost:9050',
    'socksVerion': 5

})


options = Options()
options.proxy = proxy_settings

driver  = webdriver.Firefox(options=options)
driver.get('https://check.torprojec.org')
#Check if were using tor

#When youre done, Dont forget to terminate tor
tor_process.terminate()