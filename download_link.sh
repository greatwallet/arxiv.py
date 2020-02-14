# /bin/sh
# Download single link

LINK=$1
if [ $# -ge 2 ]; then
    PDF_SAVE_DIR=$2
else
    PDF_SAVE_DIR="./"
fi
python query_and_download.py -u $LINK -d -dp $PDF_SAVE_DIR 