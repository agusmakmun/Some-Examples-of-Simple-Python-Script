<img src="https://raw.githubusercontent.com/agusmakmun/Some-Examples-of-Simple-Python-Script/master/irc/irssi-nicklist/irssi-with-nicklist-right-side.png">

###Instalations
```
sudo apt-get install screen
sudo apt-get install irssi
```

### DOCS: 
* https://irssi.org
* https://irssi-import.github.io/themes/
* http://www.ircbeginner.com/ircinfo/ircc-commands.html
* https://pthree.org/2010/02/02/irssis-channel-network-server-and-connect-what-it-means/

### CONNECT
/connect irc.freenode.net
/nick summonagus
/join #ubuntu-indonesia
/window 2
/leave

### THEME
1. Download heme: https://irssi-import.github.io/themes/ or https://github.com/ronilaukkarinen/weed
2. Copy ex: murf.theme ke: ~/.irssi/murf.theme
```
/set theme murf.theme
/set theme themes/dot.theme
```

###LOAD SCRIPT
* http://wouter.coekaerts.be/irssi/nicklist
* https://github.com/irssi/scripts.irssi.org
```
/script load nicklist.pl
/reload
```

###ENABLE NICKLIST
* https://dev.adiirc.com/projects/adiirc/wiki/Nicklist

`/nicklist [-bN|-dflor] [#channel]`

Enables/disables Nicklist.

**Switches:**
* -bN - Hides Nicklist buttons if N is 0, shows Nicklist buttons if N is 1.
* -f - Reset default Nicklist settings.
* -d - Reset Nicklist to default settings.
* -l - Show Nicklist in left side.
* -r - Show Nicklist in right side.
* -o - Hide Nicklist .

**Parameters**

[#channel] - Channel to modify Nicklist.

**Example:**
```
/nicklist -r #ubuntu-indonesia
```
