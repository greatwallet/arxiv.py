# /bin/sh
# Silently perform query and save as json

QUERY=$1
JSON_SAVE_PATH=$2
python query_and_download.py -q $QUERY -qsp $JSON_SAVE_PATH -p -st