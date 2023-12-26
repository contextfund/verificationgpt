# Brave search server API for verification:
# Docs: https://docs.bravesoftware.com/brave-search/api/

import os
import requests
import pprint

def search(query):
    """Curl query:
        Search: url -s --compressed "https://api.search.brave.com/res/v1/web/search?q=brave+search" -H "Accept:
      application/json" -H "Accept-Encoding: gzip" -H "X-Subscription-Token: """
    # calls search API using GET
    search_url = "https://api.search.brave.com/res/v1/web/search"
    params = {"q": query}
    headers = {"Accept": "application/json", "Accept-Encoding": "gzip", "X-Subscription-Token": os.environ["BRAVE_API_KEY"]}
    response = requests.get(search_url, params=params, headers=headers)
    print(response.json())
    return response.json()

def summarize(query):
    """curl - s - -compressed
    "https://api.search.brave.com/res/v1/web/search?q=what+is+the+second+highest+mountain" - H
    "Accept: application/json" - H
    "Accept-Encoding: gzip" - H
    "X-Subscription-Token:
    < YOUR_API_KEY > """""
    # calls search API using GET
    search_url = "https://api.search.brave.com/res/v1/web/search"
    params = {"q": query}
    headers = {"Accept": "application/json", "Accept-Encoding": "gzip", "X-Subscription-Token": os.environ["BRAVE_API_KEY"]}
    response = requests.get(search_url, params=params, headers=headers)
    pprint.pprint(response.json())
    return response.json()


if __name__ == "__main__":
    search("brave search")
    print("")
    summarize("what is the second highest mountain")

