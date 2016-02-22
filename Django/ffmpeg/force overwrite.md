Force overwrite with parameter `-y`, egg: `ffmpeg -y ...`

####Make a Image Output
```
os.system('ffmpeg -y -i input.mp4 -ss 00:05 -vframes 1 output.jpg')
```
###Make a Scale
```
os.system('ffmpeg -y -i output.jpg -vf scale=350:168 output_350_168_thumbnail.jpg')
```
