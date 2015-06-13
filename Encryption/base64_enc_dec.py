"""
Name             : Base 64 Encryption, encoder and decoder
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
Powered          : Python-2.7
"""

import base64

class Encode:
    def _base16_encode(self, encode_string):
        encoder = base64.b16encode(encode_string)
        return encoder

    def _base32_encode(self, encode_string):
        encoder = base64.b32encode(encode_string)
        return encoder
    
    def _base64_encode(self, encode_string):
        encoder = base64.b64encode(encode_string)
        return encoder

    def _base64_encode_string(self, encode_string):
        encoder = base64.encodestring(encode_string)
        return encoder

    def _base64_standard_encode(self, encode_string):
        encoder = base64.standard_b64encode(encode_string)
        return encoder

    def _base64_urlsafe_encode(self, encode_string):
        #sample: 'http://bloggersmart.net'
        encoder = base64.urlsafe_b64encode(encode_string)
        return encoder
    
class Decode:
    def _base16_decode(self, decode_string):
        decoder = base64.b16decode(decode_string, casefol=False)
        return decoder
    
    def _base32_decode(self, decode_string):
        decoder = base64.b32decode(decode_string, casefol=False, map01=None)
        return decoder
    
    def _base64_decode(self, decode_string):
        decoder = base64.b64decode(decode_string)
        return decoder

    def _base64_decode_string(self, decode_string):
        #sample string: 'c3Nz\n'
        decoder = base64.decodestring(decode_string)
        return decoder

    def _base64_standard_decode(self, decode_string):
        #sample string: 'c3Nz'
        decoder = base64.standard_b64decode(decode_string)
        return decoder

    def _base64_urlsafe_decode(self, decode_string):
        #sample string: 'aHR0cDovL2Jsb2dnZXJzbWFydC5uZXQ='
        decoder = base64.urlsafe_b64encode(decode_string)
        return decoder


#mome = Decode()
#mome._base64_urlsafe_decode('aHR0cDovL2Jsb2dnZXJzbWFydC5uZXQ=')
#print mome._base64_decode_string('c3Nz\n')
