# pytest filename --argument_name argument

import subprocess
import re


def test_ping_router():
    # -c = nr of packages
    # -W = wait
    match = '2 packets transmitted, 2 received, 0% packet loss,'
    command = ['ping', '10.0.0.69', '-c', '2', '-W', '2']

    ping = subprocess.run(command, capture_output=True, text=True)
    result = re.search(match, ping.stdout).group(0)
    assert match == result

def test_hostname():
    match = '^' + 'client2' + '$'
    command = ['hostname']

    found_name = subprocess.run(command, capture_output=True, text=True)
    result = re.search(match, found_name.stdout).group(0)
    assert "client2" == result 



def test_correct_ip():
    correct_address = "address 10.0.0.2"
    correct_netmask = "netmask 255.255.255.0" 
    correct_gw = "gateway 10.0.0.69"
    command = ['cat', '/etc/network/interfaces']

    network_info = subprocess.run(command, capture_output=True, text=True)
    found_ip = re.search(correct_address, network_info.stdout).group(0)
    found_netmask = re.search(correct_netmask, network_info.stdout).group(0)
    found_gw = re.search(correct_gw, network_info.stdout).group(0)
    assert found_ip == correct_address
    assert found_netmask == correct_netmask
    assert found_gw == correct_gw


