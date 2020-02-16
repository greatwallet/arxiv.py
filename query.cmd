@ echo off
REM Perform 3 queries and print to screen
set QUERY=%1
python query_and_download.py -q %QUERY% -p -m 3