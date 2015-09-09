>>> import os
>>> os.listdir('.')
['insetup.exe', 'pumper2.png', 'pumper.py']
>>> import commands
>>> commands.getoutput('ls -l insetup.exe').split(' ')[4]+' KB'
'690256 KB'
>>> 
>>> import os
>>> os.path.getsize('insetup.exe')
690256L
>>> os.stat('insetup.exe').st_size
690256L
>>> 
>>> 
