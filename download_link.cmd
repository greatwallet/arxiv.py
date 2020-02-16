@ echo off
REM Download single link
set LINK=%1
if "%2%"=="" (
    set PDF_SAVE_DIR="./" 
) else ( 
    set PDF_SAVE_DIR=%2 
)
python query_and_download.py -u %LINK% -d -dp %PDF_SAVE_DIR% 