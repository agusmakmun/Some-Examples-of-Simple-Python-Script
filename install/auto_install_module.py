# Ref: https://github.com/rafi16jan/kurs-bi/blob/master/kurs_bi/scrap.py

try:
   from bs4 import BeautifulSoup
except ImportError:
   import subprocess
   subprocess.call(['python', __file__.replace('scrap', 'install')])
   from install import main as install_pip #.install.py
   install_pip()
   from bs4 import BeautifulSoup
