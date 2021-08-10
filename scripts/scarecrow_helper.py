#!/usr/bin/python3

import sys
import subprocess

command = sys.argv[1]

with subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True, shell=True) as p:
    for b in p.stdout:
        print(b, end='')

if p.returncode != 0:
    raise CalledProcessError(p.returncode, p.args)