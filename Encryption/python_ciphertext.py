#Simply how to make a ciphertext only with 1 line.

>>> #hex_encode = 'summonagus'.encode('hex')
>>> hex_encode = '73756d6d6f6e61677573'
>>> chip  = ''.join([ str(int(a)*2) if a.isdigit() and int(a) == 3 else str(int(a)/2) if a.isdigit() and int(a) == 6 else a for a in hex_encode ])
>>> 
>>> hex_encode
'73756d6d6f6e61677573'
>>> chip
'76753d3d3f3e31377576'
>>> 
>>> 
