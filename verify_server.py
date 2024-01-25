import quart
from client import brave_search, pubmed, protein_databank
import os
import arxiv
import json

app = quart.Quart(__name__)
from quart.json.provider import DefaultJSONProvider

@app.route('/', methods=['GET'])
def get_index():
    return quart.redirect("https://chat.openai.com/g/g-xtb4B1XDY-verificationgpt-public")

@app.route('/search', methods=['GET'])
def get_search():
    query = quart.request.args.get('query')
    count = quart.request.args.get('count', default=20, type=int)
    offset = quart.request.args.get('offset', default=0, type=int)
    api_key = quart.request.headers.get('Authorization')
    if api_key != os.environ["CONTEXT_API_KEY"]:
        return 'Invalid API key'
    else:
        r = brave_search.search(query, count=count, offset=offset)
        return r

@app.route('/pubmed_search', methods=['GET'])
def get_pubmed_search():
    query = quart.request.args.get('query')
    api_key = quart.request.headers.get('Authorization')
    if api_key != os.environ["CONTEXT_API_KEY"]:
        return 'Invalid API key'
    else:
        return pubmed.search(query)

@app.route('/protein_databank_search', methods=['GET'])
def get_protein_databank_search():
    query = quart.request.args.get('query')
    api_key = quart.request.headers.get('Authorization')
    if api_key != os.environ["CONTEXT_API_KEY"]:
        return 'Invalid API key'
    else:
        return protein_databank.search(query)

@app.route('/protein_databank_papers', methods=['GET'])
def get_protein_databank_papers():
    query = quart.request.args.get('query')
    api_key = quart.request.headers.get('Authorization')
    if api_key != os.environ["CONTEXT_API_KEY"]:
        return 'Invalid API key'
    else:
        return protein_databank.get_papers(query)

@app.route('/protein_databank_urls', methods=['GET'])
def get_protein_databank_urls():
    pdb_ids = quart.request.args.get('pdb_ids') # Comma-separated
    api_key = quart.request.headers.get('Authorization')
    if api_key != os.environ["CONTEXT_API_KEY"]:
        return 'Invalid API key'
    else:
        pdb_ids = pdb_ids.split(',')
        return protein_databank.get_pdb_url(pdb_ids)

@app.route('/summarize')
def get_summarize():
    query = quart.request.args.get('query')
    api_key = quart.request.headers.get('Authorization')
    if api_key != os.environ["CONTEXT_API_KEY"]:
        return 'Invalid API key'
    else:
        return brave_search.summarize(query)

@app.route('/arxiv_search')
def get_arxiv_search():
    query = quart.request.args.get('query')
    api_key = quart.request.headers.get('Authorization')
    if api_key != os.environ["CONTEXT_API_KEY"]:
        return 'Invalid API key'
    else:
        client = arxiv.Client()
        search = arxiv.Search(
          query,
          id_list = [],
          max_results = None,
          sort_by = arxiv.SortCriterion.Relevance,
          sort_order = arxiv.SortOrder.Descending)
        papers = []
        generator = client.results(search)
        try:
            for i in range(5):
                p = next(generator)
                papers.append({"title": p.title, "summary": p.summary, "pdf_url": p.pdf_url})
        except StopIteration:
            pass
        print(query)
        print(papers)
        return papers

@app.route('/privacy')
def get_privacy():
    return 'Search queries are logged and logs are expired after 1 week. Third parties are not allowed access to logs.'

if __name__ == "__main__":
    if os.environ.get("DEBUG", "") is not "":
        app.run(debug=True)
    else:
        app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))

