"""
This script las modified from: 
https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/blob/master/grabbing/grab_modules_python2_v1.py
Modified again for more from: https://hg.python.org/cpython/file/2.7/Lib/
"""

data = ['BaseHTTPServer', 'Bastion', 'CGIHTTPServer', 'ConfigParser', 'Cookie', 'DocXMLRPCServer',
        'HTMLParser', 'MimeWriter', 'Queue', 'SimpleHTTPServer', 'SimpleXMLRPCServer', 'SocketServer',
        'StringIO', 'UserDict', 'UserList', 'UserString', '_LWPCookieJar', '_MozillaCookieJar', '__future__',
        '__phello__.foo', '_abcoll', '_osx_support', '_pyio', '_strptime', '_threading_local', '_weakrefset',
        'abc', 'aifc', 'antigravity', 'anydbm', 'argparse', 'ast', 'asynchat', 'asyncore', 'atexit', 'audiodev',
        'base64', 'bdb', 'binhex', 'bisect', 'cProfile', 'calendar', 'cgi', 'cgitb', 'chunk', 'cmd', 'code',
        'codecs', 'codeop', 'collections', 'colorsys', 'commands', 'compileall', 'contextlib', 'cookielib',
        'copy', 'copy_reg', 'csv', 'dbhash', 'decimal', 'difflib', 'dircache', 'dis', 'doctest', 'dumbdbm',
        'dummy_thread', 'dummy_threading', 'filecmp', 'fileinput', 'fnmatch', 'formatter', 'fpformat',
        'fractions', 'ftplib', 'functools', 'genericpath', 'getopt', 'getpass', 'gettext', 'glob', 'gzip',
        'hashlib', 'heapq', 'hmac', 'htmlentitydefs', 'htmllib', 'httplib', 'ihooks', 'imaplib', 'imghdr',
        'imputil', 'inspect', 'io', 'keyword', 'linecache', 'locale', 'macpath', 'macurl2path', 'mailbox',
        'mailcap', 'markupbase', 'md5', 'mhlib', 'mimetools', 'mimetypes', 'mimify', 'modulefinder', 'multifile',
        'mutex', 'netrc', 'new', 'nntplib', 'ntpath', 'nturl2path', 'numbers', 'opcode', 'optparse', 'os',
        'os2emxpath', 'pdb', 'pickle', 'pickletools', 'pipes', 'pkgutil', 'platform', 'plistlib', 'popen2',
        'poplib', 'posixfile', 'posixpath', 'pprint', 'profile', 'pstats', 'pty', 'py_compile', 'pyclbr',
        'pydoc', 'quopri', 'random', 're', 'repr', 'rexec', 'rfc822', 'rlcompleter', 'robotparser',
        'runpy', 'sched', 'sets', 'sgmllib', 'sha', 'shelve', 'shlex', 'shutil', 'site', 'smtpd',
        'smtplib', 'sndhdr', 'socket', 'sre', 'sre_compile', 'sre_constants', 'sre_parse', 'ssl', 'stat',
        'statvfs', 'string', 'stringold', 'stringprep', 'struct', 'subprocess', 'sunau', 'sunaudio', 'symbol',
        'symtable', 'sysconfig', 'tabnanny', 'tarfile', 'telnetlib', 'tempfile', 'textwrap', 'this', 'threading',
        'timeit', 'toaiff', 'token', 'tokenize', 'trace', 'traceback', 'tty', 'types', 'urllib', 'urllib2',
        'urlparse', 'user', 'uu', 'uuid', 'warnings', 'wave', 'weakref', 'webbrowser', 'whichdb',
        'xdrlib', 'xmllib', 'xmlrpclib', 'zipfile']

import os
while True:
    print "[+] --------------------------------"
    print " 1. View all __builtins__"
    print " 2. View all modules from list data"
    print " 3. View all dir from modules"
    print " 4. View all modules from sys.modules"
    print " 5. View all choice dir modules from sys.modules"
    print "[+] --------------------------------"
    
    inp_user = raw_input("Enter your choice: ")
    os.system("clear")
    if inp_user == '1':
        print dir (__builtins__)
    elif inp_user == '2':
        print data
    elif inp_user == '3':
        inp_module = raw_input("Type your module (ex: zipfile): ")
        import importlib
        try:
            imp = importlib.import_module(inp_module)
            print dir(imp)
            
        except ImportError:
            print "\n[-] Upss... [",inp_module, "] not found at dir from modules.\n"

    elif inp_user == '4':
        import sys
        print sys.modules.keys()

    elif inp_user == '5':
        inp_module = raw_input("Type your module (ex: time): ")
        import importlib
        try:
            imp = importlib.import_module(inp_module)
            print dir(imp)
            
        except ImportError:
            print "\n[-] Upss... [",inp_module, "] not found dir modules from sys.modules\n"
