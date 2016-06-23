#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' LogInstaller for Linux bassed on debian (all deb).
    Created by: Summon Agus (agus@python.web.id) at Thu, 23 Jun 2016 : 22:51
    Licensed  : MIT
    
    Config:
      You also can setup this file using crontab, ex:
        $ sudo crontab -e
      
      Setup to daily method ([minute] [hour] [date] [month] [year])
        59 23 * * * ~/path/to/logInstaller.py
'''

import os

homedir      = os.path.expanduser('~')
bash_history = open(homedir+"/.bash_history", 'r')
logFile      = 'logs/logInstaller.txt'

outList = []
with bash_history as f:
    for log in f.readlines():
        log       = log.replace('\n', '')
        log_split = log.split()
        
        if len(log_split) > 1:
            permission = 'user'
            if log_split[0] == 'sudo':
                permission = 'root'

            prefix = all([
                '-r' not in log_split and \
                '--update' not in log_split and \
                '--upgrade' not in log_split
            ])
            if permission == 'root':
                if prefix and \
                   log_split[1] == 'pip' and log_split[2] == 'install' or \
                   log_split[1] == 'apt-get' and log_split[2] == 'install':
                    outList.append('{} : {}\n'.format(permission, log))
            elif permission == 'user':
                if prefix and \
                   log_split[0] == 'pip' and log_split[1] == 'install' or \
                   log_split[0] == 'apt-get' and log_split[1] == 'install':
                    outList.append('{} : {}\n'.format(permission, log))

setNewLog = set(outList)
mode      = 'w'
if os.path.exists(logFile):
    mode = 'rb+'

with open(logFile, mode) as writeLog:
    rep_log   = lambda l: l.replace('\n', '')
    
    if mode == 'rb+':        
        setOldLog = set([ rep_log(log) for log in writeLog.readlines() ])
        for log in setNewLog:
            if rep_log(log) not in setOldLog:
                print "[i] New tool --> {}".format(rep_log(log))
                writeLog.write(log)
            else: pass

    elif mode == 'w':
        for log in setNewLog:
            print "[i] New tool --> {}".format(rep_log(log))
            writeLog.write(log)
