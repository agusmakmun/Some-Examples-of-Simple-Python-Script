Discussion: https://www.facebook.com/photo.php?fbid=961895403901754

Mohon maaf mau tanya.ketika saya ketik `"gunicorn_django --bind 0.0.0.0:8001"` yg keluar malah `"Reason: Worker failed to boot"`
itu masalahnya kenapa ya?

Solved: `gunicorn --bind mydomainOrIp:8001 myproject.wsgi:application`
