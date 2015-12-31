#----- Question, wes diacak2.. :V -------
from base64 import *

def enkrip(plain, gembok):
    enc = ''
    cuk = ''
    asu = ''
    for i in plain:
        enc += b64encode(b32encode(i))
        cuk += b32decode(b64decode(enc))

        asu = enc
        enc += b64encode(str(gembok))
        asu = b64decode(str(enc).replace(asu, ''))
        
    print cuk+asu
    print enc
    return enc

enkrip('xxx', '222')

'''
Clue : Pahami fungsinya :D, Angka
Flag ==> plain_gembok
'''


#----------------------- Answered: --------------------
encode = "TVk9PT09PT0=MQ==TlE9PT09PT0=MQ==TUU9PT09PT0=MQ==TTQ9PT09PT0=MQ==UE09PT09PT0=MQ==SU09PT09PT0=MQ==S1E9PT09PT0=MQ==SVk9PT09PT0=MQ==TDQ9PT09PT0=MQ==SVU9PT09PT0=MQ==Tk09PT09PT0=MQ==TUU9PT09PT0=MQ==S009PT09PT0=MQ==UEU9PT09PT0=MQ==TUU9PT09PT0=MQ==TkE9PT09PT0=MQ==TzQ9PT09PT0=MQ==TUU9PT09PT0=MQ==Tlk9PT09PT0=MQ==SlU9PT09PT0=MQ==TVU9PT09PT0=MQ==TlU9PT09PT0=MQ==TUU9PT09PT0=MQ==Tlk9PT09PT0=MQ==TTQ9PT09PT0=MQ==S1E9PT09PT0=MQ==TjQ9PT09PT0=MQ==T0E9PT09PT0=MQ==S1U9PT09PT0=MQ==Tlk9PT09PT0=MQ==T1E9PT09PT0=MQ==T1U9PT09PT0=MQ==Tk09PT09PT0=MQ==SUk9PT09PT0=MQ==TVU9PT09PT0=MQ==TlE9PT09PT0=MQ==TUU9PT09PT0=MQ==Tkk9PT09PT0=MQ==TUU9PT09PT0=MQ==T0k9PT09PT0=MQ==UFU9PT09PT0=MQ=="

def decrypt(encode):
    #b32decode(b64decode("TVk9PT09PT0=MQ=="))
    #>> f
    
    chunks, chunk_size = len(encode), len(encode)/40
    pisah = [ encode[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
    jutul = ''
    for item in pisah:
        jutul += b32decode(b64decode(item))
    print jutul
    #flag{CTF_EkaSyahwanMemangTopUntukBelajar}
    
decrypt(encode)
