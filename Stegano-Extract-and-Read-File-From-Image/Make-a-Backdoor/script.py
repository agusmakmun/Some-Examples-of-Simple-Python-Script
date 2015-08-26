"""
Name             : Stegano, Make a Backdoor in file Image
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
"""

import os
import time, zipfile

class scureImage(object):
     def _secure(self, image, zipfile, new_image):
          return os.system("cat "+image+" "+zipfile+" > "+new_image)
     
     def _openScure(self, new_image):
          return os.system("unzip "+new_image)
     
     def _stegano(self, zipFile):
          archive = zipfile.ZipFile(zipFile, 'r')
          list_name = archive.namelist()
          print "[+] This list of files in the image."
          print "+---------------------------------------+"
          print " ", list_name
          print "+---------------------------------------+"
          print "[1] Read file."
          print "[2] Execute file on image."
          choice_op = raw_input("[+] Enter your choice: ")
          if choice_op == "1":
               file_open = raw_input("[+] Type file want to read.\n[+] >>> ")
               try:
                    print "[+] This content of { "+file_open+" }"
                    print "+---------------------------------------+"
                    print archive.read(file_open)
                    print "+---------------------------------------+\n"
                    
               except KeyError:
                    print "[-] Uppss, {", file_open, "} is not found at this file."
                    print "[-] Please check again!"
                    
          elif choice_op == "2":
               return os.system("python "+zipFile)

     def main(self):
          print "\n\tWelcome to Python Scure Image { STEGANO METHOD }"
          print "[+] Please choice this options:"
          print " 1. Saved files in image."
          print " 2. Extract files from image."
          print " 3. Stegano read file from image.\n"
          
          mome = scureImage()
          choice = raw_input("[+] >>> ")
          if choice == "1":
               print os.listdir(".")
               img = raw_input("[+] Type Image file that will save your archive.\n[+] >>> ")
               zip = raw_input("[+] Type your Zip file: ")
               new_img = raw_input("[+] Type New Image saved your zip: ")
               mome._secure(img, zip, new_img)
               print os.listdir(".")
               
          elif choice == "2":
               print os.listdir(".")
               new_img = raw_input("[+] Type Image that will going to Extract all files.\n[+] >>> ")
               mome._openScure(new_img)
               time.sleep(2)
               print os.listdir(".")

          elif choice == "3":
               print os.listdir(".")
               zipName = raw_input("[+] Type Image where your file was saved.\n[+] >>> ")
               try:
                    mome._stegano(zipName)
               except IOError:
                    print "[-] Uppss, {", zipName, "} is not image or not found at this directory."
                    print "[-] Please check again!"
               
if __name__ == "__main__":
     mome = scureImage()
     mome.main()
