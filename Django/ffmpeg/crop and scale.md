http://www.oodlestechnologies.com/blogs/Crop-and-scale-image-using-ffmpeg

####Scale
```
    ffmpeg - i input.png -vf scale=w:h output.png  
//where  -i is input parameter,  w is width of image in pixels ,  h  is height of image in pixels and output.png output file name
eg .ffmpeg - i input.png -vf scale=310:240 output.png
```

####Crop
```
ffmpeg -i input.png -vf  "crop=w:h:x:y" input_crop.png
```
 
where -vf  video filter
w : width , h height , x and y are the left top coordinates of image


