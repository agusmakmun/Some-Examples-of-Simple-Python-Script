import uuid, hashlib

>>> uuid.uuid4().hex # generate uuid
>>> uuid.uuid5(uuid.NAMESPACE_DNS, 'other').hex

>>> hashlib.sha224(b"saya").hexdigest()
'e21e189dbc4df1cf36ebf6f926a29e3d893be9e2a99546d49a039d0d'
>>> h = hashlib.sha224(b"saya").hexdigest()
>>> hashlib.sha224(b"saya").hexdigest() == h
True
>>> hashlib.sha224(b"saya").hexdigest()
'e21e189dbc4df1cf36ebf6f926a29e3d893be9e2a99546d49a039d0d'
>>> 
