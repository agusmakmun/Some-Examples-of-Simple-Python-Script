>>> import os, time
>>> os.environ['TZ'] = 'Asia/Jakarta'
>>> time.tzset()
>>> time.strftime('%X %x %Z')
'12:26:07 10/15/15 WIB'
>>> print str(datetime.datetime.now()).split()[0]
2015-10-15
>>> 
