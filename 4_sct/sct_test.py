#//docs.python-guide.org/writing/tests/
# https://docs.pytest.org/en/latest/
# pip install --user pytest
# ~/.local/bin/pytest <fil>


import subprocess

def test_root_exists():
    command = subprocess.Popen(['getent', 'passwd', 'root'], stdout=subprocess.PIPE)
    stdout = command.stdout.read().decode().rstrip().split(":")[0]
    assert stdout == 'root'

def test_games_noshell():
    command = subprocess.Popen(['getent', 'passwd', 'games'], stdout=subprocess.PIPE)
    output = command.stdout.read().decode().rstrip().split(":")
    username = output[0] 
    shell = output[-1] 
    assert username == 'games'
    assert shell == '/usr/sbin/nologin'
