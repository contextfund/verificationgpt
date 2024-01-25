from pymed import PubMed
def search(query):
    """ """
    # calls search API using GET
    pubmed = PubMed(tool="VerificationGPT", email="ian@context.fund")
    results = list(pubmed.query(query, max_results=10))
    results = [r.toJSON() for r in results]
    return results