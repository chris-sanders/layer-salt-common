from charms.reactive import when, when_not, set_state
import subprocess

@when_not('salt-common.installed')
def install_layer_salt_master():
    #subprocess.call(["wget -O - https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -"],shell=True)
    #with open("/etc/apt/sources.list.d/saltstack.list","w") as file:
    #    file.write("deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial main")
    subprocess.call(['sudo','apt update'],shell=True)
    set_state('salt-common.installed')
