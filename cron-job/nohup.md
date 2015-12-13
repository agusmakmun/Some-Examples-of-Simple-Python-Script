Simply how to make a `cron job` in Linux using `nohup`<br />
Refference:
- http://www.cyberciti.biz/tips/nohup-execute-commands-after-you-exit-from-a-shell-prompt.html
- http://www.cyberciti.biz/faq/howto-display-process-pid-under-linux-unix/

<pre>
summonagus: ~ $ ls
Applications  Backup  Documents  ENV  README.md  Web  boot-irc.py  log-irc
summonagus: ~ $ chmod +x boot-irc.py 
summonagus: ~ $ nohup python boot-irc.py &
[1] 1343
summonagus: ~ $ nohup: ignoring input and appending output to 'nohup.out'
 
summonagus: ~ $ ps aux | grep boot-irc.py 
summona+  1343  1.1  0.7  39900  7776 pts/2    S    13:07   0:00 python boot-irc.py                               
summona+  1348  0.0  0.0   8860   648 pts/2    S+   13:07   0:00 grep --color=auto boot-irc.py                    
summonagus: ~ $ #diatas sudah otomatis menjadi cron job dengan command utama: python boot-irc.py 
summonagus: ~ $ #sekarang untuk menghentikan kita check proses yang berjalan dengan -->
summonagus: ~ $ # ps aux | grep boot-irc.py, seperti diatas.
summonagus: ~ $ #saatnya kill prosess:
summonagus: ~ $ 
summonagus: ~ $ # dengan command: kill <pid>
summonagus: ~ $ kill 1343
[1]+  Terminated              nohup python boot-irc.py
summonagus: ~ $ ps aux | grep boot-irc.py                                                                         
summona+  1432  0.0  0.0   8860   648 pts/2    S+   13:11   0:00 grep --color=auto boot-irc.py                    
summonagus: ~ $ #selesai
summonagus: ~ $ #by: Summon Agus, thanks suhu: Adhitya Putra
summonagus: ~ $  
</pre>
