$ ./manage.py sqlall name-app

'''
CommandError: App 'name-app' has migrations. 
Only the sqlmigrate and sqlflush commands can be used when an app has migrations.
'''

So there before migrate to see it.

>>> from app.models import Book
>>> print Book.objects.all().query
SELECT "app_book"."id", "app_book"."judul", "app_book"."slug", "app_book"."harga", "app_book"."detail" FROM "app_book"
>>> 
