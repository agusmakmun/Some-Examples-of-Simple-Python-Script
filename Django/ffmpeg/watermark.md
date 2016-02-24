Refference: http://stackoverflow.com/a/10920872/3445802

```
ffmpeg -y -i input.mp4 -i logo.png -filter_complex "overlay=10:10" -codec:a copy output.mp4
```

`"overlay=10:10"` -> is left-top position, with 10px x 10px
