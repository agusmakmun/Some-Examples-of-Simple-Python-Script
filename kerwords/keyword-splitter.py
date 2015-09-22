#usr/bin/python2.7

tmp = ''
with open('keywords.txt') as f:
    for i in f:
        tmp += i.replace('\n', ', ').replace('\r', '')
    print (tmp)
    saved = open('saved.txt', 'w')
    saved.write(tmp)
    saved.close()
