"""
file: doc-return-mentions.py
what: return instances of a search term and the pages it appears on
      in a series of documents for a given project
uses: http://datadesk.github.com/python-documentcloud/
"""

# import the modules for this script
from documentcloud import DocumentCloud
from ConfigFile import config_settings

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings["user_name"], config_settings["password"]
)

def retrieve_search_term(term_to_search):

    obj_list = client.documents.search(term_to_search)
    for document in obj_list:
        print document.title
        for mention in document.mentions:
            print "Page %s\n%s\n\n" % (mention.page, mention.text)

if __name__ == "__main__":
    retrieve_search_term("St Louis")
