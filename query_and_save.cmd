@ echo off
REM Silently perform query and save as json

set QUERY=%1
set JSON_SAVE_PATH=%2
python query_and_download.py -q %QUERY% -qsp %JSON_SAVE_PATH% -p -st