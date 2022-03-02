import argparse
from pydoc import describe 
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd():
        return 
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)

    return output.decode() 

if __name__ == '__main__':
    parser  = argparse.ArgumentParser(
        description = 'BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwarp.dedent('''Example:
            netcat.py -t 192.168.1.108 -p 5555 -1 -c # command shell
            netcat.py -t 192.168.1.108 -p 5555 -1 -u=mytest.txt # upload to file
            netcat.py -t 192.168.1.108 -p 5555 -1 -e=\"cat /etc/passwd\" # execute command
            echo 'ABC' | ./netcat.py -t 198.168.1.108 -p 135 # echo text to port 135
            netcat.py -t 192.168.1.108 -p 5555 # connect to server
        ''')
    ) 
parser.add_argument('-c','--command', action='store_true', help='command shell')
