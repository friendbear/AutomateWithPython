#! python3

import subprocess, sys
import logging as log

#subprocess.Popen(['/bin/sh', 'echo', 'Hello Python!'])

subprocess.Popen(['start', 'hello.txt'], shell=True)

# run other python script
subprocess.Popen([sys.executable, 'print("hello")'])


with subprocess.Popen(["ifconfig"]) as proc:
    log.write(proc.stdout.read())
