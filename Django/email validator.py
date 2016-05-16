#!/usr/bin/env python
# Email validator, {summonagus}

import re

input_email = raw_input("Masukkan email: ")

if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", input_email):
    print "Email `{}` tidak valid!".format(input_email)
else:
    print "Email `{}` valid!".format(input_email)
