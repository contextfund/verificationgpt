import quart
from client import brave_search
import os
import arxiv

app = quart.Quart(__name__)

@app.route('/', methods=['GET'])
def get_index():
    return quart.redirect("https://chat.openai.com/g/g-2xe4GhrBR-verification-gpt")

@app.route('/search', methods=['GET'])
def get_search():
    query = quart.request.args.get('query')
    api_key = quart.request.headers.get('Authorization')
    if api_key != os.environ["CONTEXT_API_KEY"]:
        return 'Invalid API key'
    else:
        return brave_search.search(query)

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
        for i in range(5):
            p = next(generator)
            papers.append({"title": p.title, "summary": p.summary, "pdf_url": p.pdf_url})
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

