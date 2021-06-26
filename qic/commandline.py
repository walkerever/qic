import sys
import os
import subprocess

class commandline :
    @staticmethod
    def qx(cmd, merge=False, debug=False, exitonerror=False, hidepwd=False, pwdmark="") :
        if type(cmd) is not list :
            if type(cmd) is str :
                cmd = cmd.split()
            else :
                raise Exception("cmd must be a list or a string.")
        cmdmasked = list()
        if hidepwd :
            i=0
            while i < len(cmd) :
                if cmd[i] in ['-'+c for c in pwdmark] :
                    cmdmasked.append(cmd[i])
                    if i+1 < len(cmd) :
                        cmdmasked.append("******")
                    i+=2
                else :
                    cmdmasked.append(cmd[i])
                    i+=1
        if debug :
            print("# cmd=[{}]".format(" ".join(cmdmasked or cmd)))
        with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.subprocess.STDOUT if merge else subprocess.PIPE) as p :
            out, err = p.communicate()
            out = out and out.decode().rstrip()
            err = err and err.decode().rstrip()
            if debug :
                print("# stdout=[{}]".format(out or ""))
                print("# stderr=[{}]".format(err or ""))
                print("# rtcode=[{}]".format(p.returncode))
            if p.returncode != 0 and exitonerror :
                sys.exit(p.returncode)
            return (p.returncode, out, err)
            
        
#print(commandline.qx("echo hello -p xx yy",debug=True,hidepwd=True,pwdmark="p"))
#print(commandline.qx("ls -p",debug=True,hidepwd=True,pwdmark="p"))
