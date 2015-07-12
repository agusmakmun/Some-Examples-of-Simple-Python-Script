"""
Modified again for more from: https://hg.python.org/cpython/file/2.7/Lib/
"""

def buliltins():
    print "------- This __builtsins__ (Built-in Functions) -------"
    return dir (__builtins__)

#print buliltins()
"""
>>> import sys
>>> a = sys.modules
>>> type(a)
<type 'dict'>
>>> a.keys()
['heapq', 'code', 'tkFileDialog', 'functools', 'random', 'subprocess', ---->> more ]
"""


from bs4 import BeautifulSoup
import urllib

url = 'https://hg.python.org/cpython/file/2.7/Lib/'
soup = BeautifulSoup(url)

def get_url(url):
    start = urllib.urlopen(url)
    soup = BeautifulSoup(start)
    for link in soup.findAll('a', href=True):
        href = link['href']
        split = href.split("/")
        try:
            index_akhir = split[5]
            if index_akhir[-3] == '.':
                print index_akhir
            else:
                pass
        except IndexError:
            pass
        
#get_url(url)

data = """
BaseHTTPServer.py
Bastion.py
CGIHTTPServer.py
ConfigParser.py
>>> more
"""

#data = data.split("\n")
#data = data[1:-1]
#print str(data).replace(".py", "")



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



print data
print type(data)
