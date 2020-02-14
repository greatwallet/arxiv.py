import argparse
import json
import os
import os.path as osp

import arxiv

def parse_args():
    parser = argparse.ArgumentParser(description='Perform Query and Download from Arxiv')
    parser.add_argument('--query', '-q', default="", 
                        help="An arXiv query string. Format documented https://arxiv.org/help/api/user-manual#Quickstart. Default: \"\"")
    parser.add_argument('--id-list', '-i', default=[], nargs='*', help="List of arXiv record IDs. Default: []")
    parser.add_argument('--url-list', '-u', default=[], nargs='*', help="List of url to be downloaded, would be overridden if either query or id-list is specified. Default: []")
    parser.add_argument('--max-results', '-m', default=10, type=int, help="The maximum number of results returned by the query. Default: 10")
    parser.add_argument('--start', '-idx', default=0, type=int, help="The offset of the first returned object from the arXiv query results. Default: 0")
    parser.add_argument('--sort-by', '-sb', default='relevance', choices=['relevance', 'lastUpdatedDate', 'submittedDate'], help="The arXiv field by which the result should be sorted, which can be can be 'relevance', 'lastUpdatedDate', 'submittedDate'. Default: 'relevance'")
    parser.add_argument('--order', '-o', default='descending', choices=['descending', 'ascending'], help="The sorting order, which can be 'descending' or 'ascending'. Default: 'descending'")
    parser.add_argument('--prune', '-p', action='store_true', help="If specified, received abstract objects will be simplified")
    parser.add_argument('--max-chunk-results', '-mcr', default=1000, type=int, help="The maximum number of abstracts ot be retrieved by a single internal request to the arXiv API. Default: 1000")
    parser.add_argument('--query-save-path', '-qsp', default=None, help="If specified, The path of the query results saved as json. Default: None")
    parser.add_argument('--silent', '-st', action='store_true', help="If specified, the query results will not be printed to screen")
    parser.add_argument('--download', '-d', action='store_true', help="If specified, the query results will be downloaded")
    parser.add_argument('--full-name', '-f', action='store_true', help="If specified, the PDF will be saved as `id`+`caption`.pdf, otherwise `id`.pdf")
    parser.add_argument('--download-directory', '-dp', default='./', help="The directory of the PDFs saved in, only valid when `download` is specified. Default: ./")
    
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if args.query == "" and args.id_list == []:
        if args.url_list == []:
            raise ValueError("None of`query`, `id_list` or `url_list` is specified.")
        if args.download is False:
            import warnings
            warnings.warn("You only specified url list without downloading them")
        results = [
            {
            "pdf_url": url, 
            "title": "UNKNOWN TITLE"
            } for url in args.url_list
        ]
    else:
        results = arxiv.query(
            query=args.query, 
            id_list=args.id_list, 
            max_results=args.max_results, 
            start=args.start, 
            sort_by=args.sort_by, 
            sort_order=args.order, 
            prune=args.prune, 
            max_chunk_results=args.max_chunk_results
        )
        
        # Print query results
        if args.silent is False:
            print(json.dumps(results, indent=4))
            
        # Save query results
        if args.query_save_path is not None:
            json_path = args.query_save_path
            ext = osp.splitext(json_path)[-1]
            if ext == '':
                json_path += '.json'
            elif ext != '.json':
                raise ValueError("The filetype should be .json, not {}".format(ext))

            with open(json_path, 'w') as f:
                json.dump(results, f, indent=4)
                
            print("\nSave the json file in {}\n".format(json_path))
        
    # Save PDF
    if args.download is True:
        if not osp.exists(args.download_directory):
            os.makedirs(args.download_directory)
        slugify = arxiv.slugify if args.full_name else arxiv.custom_slugify
        for paper in results:
            arxiv.download(paper, slugify=slugify, dirpath=args.download_directory)
            
        print("\n Save the PDF in {}\n".format(args.download_directory))