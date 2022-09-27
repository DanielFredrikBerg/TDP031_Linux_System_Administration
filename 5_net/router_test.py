import subprocess
import re



def test_router_ping():
    # -c = nr of packages
    # -W = wait 
    match = '2 packets transmitted, 2 received, 0% packet loss,'
    command = ['ping', '10.0.2.2', '-c', '2', '-W', '2'] 
    ping = subprocess.run(command, capture_output=True, text=True)

    result = re.search(match, ping.stdout).group(0)
    assert match == result


def test_ipforwarding_on():
    match = 'net.ipv4.ip_forward = 1'
    command = ['sysctl', 'net.ipv4.ip_forward']
    # cat /proc/sys/net/ipv4/ip_forward   0 or 1 in terminal
    sysctl = subprocess.run(command, capture_output=True, text=True)
    assert match == sysctl.stdout.rstrip()


def test_masq():
    match = 'MASQUERADE  all  --  anywhere             anywhere'
    command = ['iptables', '--list', '-t', 'nat']
    iptables = subprocess.run(command, capture_output=True, text=True)

    result = re.search(match, iptables.stdout).group(0)
    assert match == result 

def main():
    test_router_ping()

main()
