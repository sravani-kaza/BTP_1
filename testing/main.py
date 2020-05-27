import subprocess
import os
import time

max_processes = 4
files = ['test_'+str(i)+'.py' for i in range(1,max_processes)]
files_1 = ['test_'+str(i)+'1.py' for i in range(1,max_processes)]
files = files + files_1
command = "python3"
processes = set()

for name in files:
    processes.add(subprocess.Popen([command, name]))
    if len(processes) >= 2*max_processes:
        os.wait()
        processes.difference_update([
            p for p in processes if p.poll() is not None])
