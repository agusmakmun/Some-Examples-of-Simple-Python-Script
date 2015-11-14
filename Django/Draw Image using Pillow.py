#http://stackoverflow.com/a/16377244/3445802
>>> from PIL import Image
>>> from PIL import ImageFont
>>> from PIL import ImageDraw 
>>> img = Image.open("sample_in.jpg")
>>> draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
>>> font = ImageFont.truetype("sans-serif.ttf", 16)
# draw.text((x, y),"Sample Text",(r,g,b))
>>> draw.text((0, 0),"Sample Text",(255,255,255),font=font)
>>> img.save('sample-out.jpg')


>>> from PIL import Image
>>> from PIL import ImageFont
>>> from PIL import ImageDraw
>>> img = Image.open("world.jpg")
>>> draw = ImageDraw.Draw(img)
>>> font = ImageFont.truetype("Roboto-Regular-webfont.ttf", 16)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/PIL/ImageFont.py", line 260, in truetype
    return FreeTypeFont(font, size, index, encoding)
  File "/usr/local/lib/python2.7/dist-packages/PIL/ImageFont.py", line 140, in __init__
    self.font = core.getfont(font, size, index, encoding)
IOError: cannot open resource
>>> 
>>> font = ImageFont.truetype("Sawasdee.ttf", 16)
>>> 
>>> draw.text((0,0), "www.qafwah.com", (255,255,255), font=font)
>>> img.save("sample-out-draw.jpg")
>>> img.show("sample-out-draw.jpg")
>>> 

#Checking font if is avalilable on: truetype
agaust@agaust:~/Documents$ locate Sawasdee.ttf
/usr/share/fonts/truetype/tlwg/Sawasdee.ttf
agaust@agaust:~/Documents$ 
agaust@agaust:~/Documents$ ls /usr/share/fonts/truetype/tlwg/
Garuda-BoldOblique.ttf   Norasi-BoldItalic.ttf     TlwgMono-BoldOblique.ttf        TlwgTypo-Oblique.ttf
Garuda-Bold.ttf          Norasi-BoldOblique.ttf    TlwgMono-Bold.ttf               TlwgTypo.ttf
Garuda-Oblique.ttf       Norasi-Bold.ttf           TlwgMono-Oblique.ttf            Umpush-BoldOblique.ttf
Garuda.ttf               Norasi-Italic.ttf         TlwgMono.ttf                    Umpush-Bold.ttf
Kinnari-BoldItalic.ttf   Norasi-Oblique.ttf        TlwgTypewriter-BoldOblique.ttf  Umpush-LightOblique.ttf
Kinnari-BoldOblique.ttf  Norasi.ttf                TlwgTypewriter-Bold.ttf         Umpush-Light.ttf
Kinnari-Bold.ttf         Purisa-BoldOblique.ttf    TlwgTypewriter-Oblique.ttf      Umpush-Oblique.ttf
Kinnari-Italic.ttf       Purisa-Bold.ttf           TlwgTypewriter.ttf              Umpush.ttf
Kinnari-Oblique.ttf      Purisa-Oblique.ttf        TlwgTypist-BoldOblique.ttf      Waree-BoldOblique.ttf
Kinnari.ttf              Purisa.ttf                TlwgTypist-Bold.ttf             Waree-Bold.ttf
Loma-BoldOblique.ttf     Sawasdee-BoldOblique.ttf  TlwgTypist-Oblique.ttf          Waree-Oblique.ttf
Loma-Bold.ttf            Sawasdee-Bold.ttf         TlwgTypist.ttf                  Waree.ttf
Loma-Oblique.ttf         Sawasdee-Oblique.ttf      TlwgTypo-BoldOblique.ttf
Loma.ttf                 Sawasdee.ttf              TlwgTypo-Bold.ttf
agaust@agaust:~/Documents$ 
