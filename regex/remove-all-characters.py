import re
import string

def replaceIt(file):
    out = ''
    with open(file, 'r') as f:
        for line in f:
            repl = '[' + re.escape(''.join(string.punctuation)) + ']'
            out += re.sub(repl, '', line)
        return out

print (replaceIt('test.txt'))

# output
'''
cobaanu231339 91102
1212086mcmnad0ca
'''

# test.txt
'''
coba*())@*&#anu;,231339 91102-$@!%!
''..,121208***&@6mcmnad0ca
'''
