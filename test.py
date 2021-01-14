import subprocess
rcmd = "su reboot"
pwd = "nvidia"
p = subprocess.Popen(rcmd, shell=True, stdin='nvidia', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
p.stdin.write(pwd.encode('utf-8'))
# p.stdin.write("\n".encode('utf-8'))
# # p.stdin.write(rcmd.encode('utf-8'))
# out, err = p.communicate(rcmd.encode('utf-8'))