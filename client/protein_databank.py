import pypdb
def search(query: str):
    # calls search API using GET
    results = pypdb.Query(query).search()
    return results

def get_pdb_url(pdb_ids):
    return [f'https://www.rcsb.org/structure/{pdb_id}' for pdb_id in pdb_ids]

def get_papers(query: str):
    results = pypdb.find_papers(query)
    return results