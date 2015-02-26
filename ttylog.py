from subprocess import Popen,PIPE
import re
import sys

pipe = Popen(['strace','-p',sys.argv[1],'-e','read'],shell=False, stdout=PIPE, stderr=PIPE)
tmp_string = ""

while True:
        output = pipe.stderr.readline()
        if (output.find("\\r\\n") >= 0):
                print tmp_string
                tmp_string = ""
        else:
                pattern = r'"([a-z]|[A-Z]|\\r\\n|-| |@|\.)"'
                m = re.search(pattern,output)
                if (m is None):
                        continue
                else:
                        tmp_string = tmp_string + m.group()[-1:][:-1]

