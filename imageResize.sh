SRC_DIR="$1"
DEST_DIR="$2"

if [ -z "$SRC_DIR" ] || [ -z "$DEST_DIR" ]; then
    echo "Usage: imageResize.sh [src_dir] [dest_dir]"
    exit 0
fi

if [ ! -d "$DEST_DIR" ]; then
    mkdir -p "$DEST_DIR"
fi

RESIZE_RATIO="20%"

find "$SRC_DIR" -maxdepth 1 \( -iname "*.jpg" -o -iname "*.png" \) -print0 | 
   while read -r -d '' eachFile; do 
       echo Processing "$eachFile"
       imageName=`basename $eachFile`
       convert -resize $RESIZE_RATIO "$eachFile" "$DEST_DIR"/"$imageName"
       # Preserve the same atime and mtime
       touch -r "$eachFile" "$DEST_DIR"/"$imageName"
   done

echo "Image Resize Finished"
