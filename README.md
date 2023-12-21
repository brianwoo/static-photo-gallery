# Static Photo Gallery
### This project provides a simple way to generate a static photo gallery

## Features
- A quick and simple way to generate a static photo gallery
- Photo gallery is responsive, desktop and mobile friendly
- File resized will perserve last modification time
- Photos will be shown in chronological order in gallery
- Lazy loading support in displaying photos

## Requirements:
- Python 3.x
- Jinja2
- ImageMagick (optional, only to resize photos for a gallery)

## ImageResize

```bash
./imageResize.sh 
Usage: imageResize.sh [src_dir] [dest_dir]

./imageResize.sh ./2019 ./2019-Gallery
```

## Generate Photo Gallery
```bash
python3 gen_photo_album.py 
Usage: gen_photo_album.py [album_name] [image_directory]

python3 gen_photo_album.py "Best of 2019" "./2019-Gallery"
```

## To Run
```
cd ./2019-Gallery
python3 -m http.server 8080
```

