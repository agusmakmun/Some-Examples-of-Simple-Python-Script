Refference: 
- http://stackoverflow.com/a/10920872/3445802
- http://stackoverflow.com/a/4491369/3445802

```
ffmpeg -y -i input.mp4 -i logo.png -filter_complex "overlay=10:10" -codec:a copy output.mp4
```

- `"overlay=10:10"` -> is left-top position, with 10px x 10px
- `-codec:a copy` -> simply stream copy'ing for audo.


####This method for `force overwrite`, `benchmark`, `720p` and copy'ing audio codec:
```
ffmpeg -y -i input.mp4 -i logo.png -s 720x406 -filter_complex "overlay=10:10" -codec:a copy output.mp4
```
