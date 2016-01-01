#!/usr/bin/python
# -*- coding: utf-8 -*-
import string, sys

"""
Docs: https://python.web.id/blog/untranslate-tools-for-cryptography/

[1] Stack Problem:
>>> import string
>>> make_trans = string.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                  'CDEFGHIJKLMNOPQRSTUVWXYZABcdefghijklmnopqrstuvwxyzab')
>>> trans = string.translate("Summon Agus", make_trans)
>>> trans
'Uwooqp Ciwu'
>>> 

[2] Test it:
agaust@agaust:~/Python-Code/Translate$ python un_translate.py right 3 "Uwooqp Ciwu"
Vxpprq Djxv
Wyqqsr Ekyw
Xzrrts Flzx
agaust@agaust:~/Python-Code/Translate$ python un_translate.py left 4 "Uwooqp Ciwu"
Tvnnpo Bhvt
Summon Agus
Rtllnm zftr
Qskkml yesq

[3] Find Solved:
'Uwooqp Ciwu' is 'Summon Agus'
"""

def _help():
    print "<----------------------------------------------------------------------------------------------->"
    print "[>] Untranslate Tools for Cryptography                                                          |"
    print "[>] Build by Summon Agus, blog: https://python.web.id                                           |"
    print "[>] Made for string was translate with `string.translate` from python modules.                  |"
    print "[+] --------------------------------------------------------------------------------------------|"
    print "[?] Untranslate left :   ./un_translate.py left [<number> or -f <for full>] <string_translate>  |"
    print "[?] Untranslate right:   ./un_translate.py right [<number> or -f <for full>] <string_translate> |"
    print "<----------------------------------------------------------------------------------------------->"

"""Thanks to: `Iron Fist` for this `shift` function.
Answered: http://stackoverflow.com/a/34555735/3445802"""
def shift(s, step, side='right'):
    step %= len(s) #Will generate correct steps even step > len(s)
    if side == 'right':
        return s[-step:]+s[:-step]
    elif side == 'left':
        return s[step:]+s[:step]
    else:
        print '[-] Please, Specify either Right or Left shift!'
        return sys.exit()

""" `_untranslate()` is function of translator"""
def _untranslate(command, length, en_translate):
    command         = sys.argv[1]
    length          = sys.argv[2]
    en_translate    = sys.argv[3]
    
    chrs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    #for complete chars, use this:
    #chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')

    """This `_full_length()` function use if param of `length` is `-f`.
    So, there will returning `untranslate` with full length of param:`chrs`."""
    def _full_length():
        no = 0
        for numb in range(len(chrs)):
            no += 1
            make_trans = string.maketrans( shift(chrs, no, command), chrs)
            print string.translate(en_translate, make_trans )

    """This `_specific_length()` function use if param of `length` use specific number"""
    def _specific_length():
        no = 0
        for numb in range(int(length)):
            no += 1
            make_trans = string.maketrans( shift(chrs, no, command), chrs)
            print string.translate(en_translate, make_trans )

    """Define if `command` is `left or `right`, if not they, it will return to _help() function."""
    if command == 'left' or command == 'right':
        try:
            if length == '-f':
                _full_length()
            else:
                _specific_length()
        except ValueError:
            pass
    else:
        return _help()

if __name__ == "__main__":
    try:
        command         = sys.argv[1]
        length          = sys.argv[2]
        en_translate    = sys.argv[3]
        _untranslate(command, length, en_translate)
    except IndexError:
        _help()
