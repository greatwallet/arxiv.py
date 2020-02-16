# arxiv.py [![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/) [![Python 3.6](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

Python wrapper for [the arXiv API](http://arxiv.org/help/api/index). This repo is a fork of [`https://github.com/lukasschwab/arxiv.py`](https://github.com/lukasschwab/arxiv.py) with more user-friendly scripts.

## New Functions
* Progress bar visualization when downloading via `tqdm`
* Save query results as json file
* User-friendly python and shell Scripts for daily use w/o writing your own code
* Add `cmd` scripts for Windows

## About arXiv

[arXiv](http://arxiv.org/) is a project by the Cornell University Library that provides open access to 1,000,000+ articles in Physics, Mathematics, Computer Science, Quantitative Biology, Quantitative Finance, and Statistics.

## Usage

### Installation

```bash
git clone https://github.com/greatwallet/arxiv.py
cd arxiv.py
python setup.py install
```

Verify the installation with

```bash
python setup.py test
```

### Usage of Python script [`query_and_download.py`](https://github.com/greatwallet/arxiv.py/blob/master/query_and_download.py)

[`query_and_download.py`](https://github.com/greatwallet/arxiv.py/blob/master/query_and_download.py) is a user-friendly script with arguments. The usage lies below:
```
$ python query_and_download.py --help
usage: query_and_download.py [-h] [--query QUERY]
                             [--id-list [ID_LIST [ID_LIST ...]]]
                             [--url-list [URL_LIST [URL_LIST ...]]]
                             [--max-results MAX_RESULTS] [--start START]
                             [--sort-by {relevance,lastUpdatedDate,submittedDate}]
                             [--order {descending,ascending}] [--prune]
                             [--max-chunk-results MAX_CHUNK_RESULTS]
                             [--query-save-path QUERY_SAVE_PATH] [--silent]
                             [--download] [--full-name]
                             [--download-directory DOWNLOAD_DIRECTORY]

Perform Query and Download from Arxiv

optional arguments:
  -h, --help            show this help message and exit
  --query QUERY, -q QUERY
                        An arXiv query string. Format documented
                        https://arxiv.org/help/api/user-manual#Quickstart.
                        Default: ""
  --id-list [ID_LIST [ID_LIST ...]], -i [ID_LIST [ID_LIST ...]]
                        List of arXiv record IDs. Default: []
  --url-list [URL_LIST [URL_LIST ...]], -u [URL_LIST [URL_LIST ...]]
                        List of url to be downloaded, would be overridden if
                        either query or id-list is specified. Default: []
  --max-results MAX_RESULTS, -m MAX_RESULTS
                        The maximum number of results returned by the query.
                        Default: 10
  --start START, -idx START
                        The offset of the first returned object from the arXiv
                        query results. Default: 0
  --sort-by {relevance,lastUpdatedDate,submittedDate}, -sb {relevance,lastUpdatedDate,submittedDate}
                        The arXiv field by which the result should be sorted,
                        which can be can be 'relevance', 'lastUpdatedDate',
                        'submittedDate'. Default: 'relevance'
  --order {descending,ascending}, -o {descending,ascending}
                        The sorting order, which can be 'descending' or
                        'ascending'. Default: 'descending'
  --prune, -p           If specified, received abstract objects will be
                        simplified
  --max-chunk-results MAX_CHUNK_RESULTS, -mcr MAX_CHUNK_RESULTS
                        The maximum number of abstracts ot be retrieved by a
                        single internal request to the arXiv API. Default:
                        1000
  --query-save-path QUERY_SAVE_PATH, -qsp QUERY_SAVE_PATH
                        If specified, The path of the query results saved as
                        json. Default: None
  --silent, -st         If specified, the query results will not be printed to
                        screen
  --download, -d        If specified, the query results will be downloaded
  --full-name, -f       If specified, the PDF will be saved as
                        `id`+`caption`.pdf, otherwise `id`.pdf
  --download-directory DOWNLOAD_DIRECTORY, -dp DOWNLOAD_DIRECTORY
                        The directory of the PDFs saved in, only valid when
                        `download` is specified. Default: ./

```
<b>Note: </b> If you plan to download PDFs in batches, please keep in mind that a rapid visiting action or a huge amount of downloading may trigger the alarm of arxiv api, thus raising HTTP error.

### Usage of Shell Scripts

I also provide shell scripts for simplifing the arguments.

```
# make 3 queries and print results to screen 
# example
export QUERY="here is your query"
sh query.sh $QUERY

# make 10 queries silently and save the results as pretty-looking json file
# example
export QUERY="here is your query"
export JSON_SAVE_PATH="your path for query results"
sh query_and_save.sh $QUERY $JSON_SAVE_PATH

# Download single link and save pdf
# example 1: save to ./
export URL="your pdf url, e.g. 'https://arxiv.org/pdf/1804.00175.pdf'"
sh download_link.sh $URL
# example 2: save to custom path
export URL="your pdf url"
export PDF_DIR="your directory for saving pdf"
sh download_link.sh $URL $PDF_DIR
```

### Usage of CMD Scripts
The functions are the same as the shell namesakes 
```
REM Windows Powershell or cmd
set QUERY="here is your query"
.\query.cnd %QUERY%

set QUERY="here is your query"
set JSON_SAVE_PATH="your path for query results"
.\query_and_save.cmd %QUERY% %JSON_SAVE_PATH%

set URL="your pdf url"
set PDF_DIR="your directory for saving pdf"
.\download_link.cmd %URL% %PDF_DIR%
```

## Contact
If you have any problems, please contact [`cxt_tsinghua@126.com`](cxt_tsinghua@126.com) or refer to the original repo [`https://github.com/lukasschwab/arxiv.py`](https://github.com/lukasschwab/arxiv.py).

