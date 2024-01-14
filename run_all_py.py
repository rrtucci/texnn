import os
from subprocess import Popen, PIPE, call

''' 

This script tries to run all files, in all white-listed folders, that end in 
.py and have a main() after an 'if __name__ == "__main__":'

'''

dir_whitelist = [
    "./",
    "silly_bnet",
    "asia",
    "expert_archer",
    "rock_layers",
    "vanilla_transformer"
]
file_blacklist = [
    'run_all_py.py',
    'globals.py'
]
for dir_name in dir_whitelist:
    for fname in os.listdir(dir_name):
        if fname[-3:] == '.py' and fname not in file_blacklist:
            path = dir_name + '/' + fname
            print('--------------------', path)
            pro = Popen(['python', fname], cwd=dir_name,
                        stdout=PIPE, stderr=PIPE)
            stdout, stderr = pro.communicate()
            print(str(stderr))