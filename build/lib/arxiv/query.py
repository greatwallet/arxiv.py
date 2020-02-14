import arxiv

# Keyword queries
arxiv.query(query="quantum", max_results=100)
# Multi-field queries
# arxiv.query(query="au:balents_leon AND cat:cond-mat.str-el")
# Get single record by ID
# arxiv.query(id_list=["1707.08567"])
# Get multiple records by ID
# arxiv.query(id_list=["1707.08567", "1707.08567"])

# Get interator over query results
# result = arxiv.query(query="quantum", max_chunk_results=10, iterative=True)
# for paper in result():
#    print(paper)
