#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import time, os
import sys, fileinput
from bs4 import BeautifulSoup


class Grabber(object):
    def use(self):
        print ""
        print "* This just Fucking whatever for grabbing."
        print "* For license just fucking to change this. ^Summon Agus Created."
        print "-------------------------------------------------------------------------------------"
        print "[1] Add Note         : ./notes.py addnote <file_name> <title> <content> <tag1, tag2>"
        print "[2] List Note        : ./notes.py listnote <file_name>"
        print "[3] Delete Note      : ./notes.py delnote <file_name> <numb_line>"
        print "[4] Add Url to Grab  : ./notes.py addurl <file_name> <url>"
        print "-------------------------------------------------------------------------------------"
        print ""
    
    def addnote(self, args):
        self.help = "./notes.py addnote <file_name> <title> <content> <tag1, tag2>"
        
        if len(sys.argv) < 5:
            sys.exit("[-] Fucking Damn!!\n[?] Use similiar this: " + self.help)

        f_note_out  = sys.argv[2]
        title       = sys.argv[3]
        content     = sys.argv[4]
        tags        = sys.argv[5]
        
        print "[+] Your args is: ./notes.py", args, f_note_out, title, content, tags
        time.sleep(1)
        print "[>] Waiting for save your note ..."

        my_note = '"'+title+'": "'+content+'"'+ ' tag: '+ tags

        """ [?] Trying if file was exists, so note will add in new line.
            [?] But, if file is doesn't exists, this program will automatically write file with your first argument.
        """
        try:
            f_note = open(f_note_out, 'a')
            my_note = my_note + '\n'
        except IOError:
            f_note = open(f_note_out, 'w')
            my_note = '\n' + my_note
                    
        f_note.write(my_note)
        f_note.close()
        time.sleep(1)
        print "[>] Your note was saved in <"+ f_note_out +">"

    def listnote(self, args):
        self.help = "./notes.py listnote <file_name>"
        if len(sys.argv) < 2:
            sys.exit("[-] Fucking Damn!!\n[?] Use similiar this: " + self.help)
        
        print "[+] Your args is: ./notes.py", args, sys.argv[2]
        
        try:
            with open(sys.argv[2], "r") as f:
                print " -------------------------------------- "
                for line in f:
                    print line.replace("\n", "")
                    time.sleep(0.3)
                print " -------------------------------------- "
            
        except IOError:
            sys.exit("[-] File Doesn't exists!!"+\
                     "\n[?] This your path now: " +str(os.getcwd())+\
                     "\n[?] This files and folders in your path now: " + str(os.listdir('.')) )

    def delnote(self, args):
        self.help = "./notes.py delnote <file_name> <numb_line>"
        if len(sys.argv) < 3:
            sys.exit("[-] Fucking Damn!!\n[?] Use similiar this: " + self.help)

        f_note_out = str(sys.argv[2])
        try:
            for numb, line in enumerate(fileinput.input(f_note_out, inplace=True)): #start index from 0
                if numb == int(sys.argv[3]):
                    continue
                else:
                    sys.stdout.write(line)
            sys.exit("[+] Success delete line <"+sys.argv[3]+"> in file of <"+ f_note_out +">")
        
        except OSError:
            sys.exit("[-] File Doesn't exists!!"+\
                     "\n[?] This your path now: " +str(os.getcwd())+\
                     "\n[?] This files and folders in your path now: " + str(os.listdir('.')) )
        
    def addurl(self, args):
        self.help = "./notes.py addurl <file_name> <url>"
        if len(sys.argv) < 3:
            sys.exit("[-] Fucking Damn!!\n[?] Use similiar this: " + self.help)

        url = str(sys.argv[3])
        f_note_out = str(sys.argv[2])
        print "[+] Your args is: ./notes.py", args, f_note_out, url
        
        agent   = {'User-Agent':'Mozilla/5.0'}
        request = urllib2.Request(url, headers=agent)
        page    = urllib2.urlopen(request).read()
        soup    = BeautifulSoup(page)

        title    = soup.title.string.encode('utf-8')
        descriptions = soup.findAll(attrs={"name":"description"})[0]['content'].encode('utf-8')
        keywords = soup.findAll(attrs={"name":"keywords"})[0]['content'].encode('utf-8')
        
        print "[>] Waiting for save your note ..."
        time.sleep(1)
        
        my_note = '"'+title+'": "'+descriptions+'"'+ ' tag: '+ keywords
        
        try:
            f_note = open(f_note_out, 'a')
            my_note = my_note + '\n'
        except IOError:
            f_note = open(f_note_out, 'w')
            my_note = '\n' + my_note

        f_note.write(my_note)
        f_note.close()
        time.sleep(1)
        print "[>] Your url note was saved in <"+ f_note_out +">"


if __name__ == "__main__":
    mome = Grabber()
    try:
        args = str(sys.argv[1])
        if args == 'addnote':
            mome.addnote(args)
        elif args == 'listnote':
            mome.listnote(args)
        elif args == 'delnote':
            mome.delnote(args)
        elif args == 'addurl':
            mome.addurl(args)
        else:
            print "Funcking damn!, please checkout your input"
    except IndexError:
        mome.use()

