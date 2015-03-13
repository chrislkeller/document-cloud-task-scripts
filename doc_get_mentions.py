"""
file: doc_get_mentions.py
what: return instances of a search term and the pages it appears on in a series of documents for a given project
"""

# import the modules for this script
from documentcloud import DocumentCloud
from config_file import config_settings

# set your document ID
SEARCH_TERM = "St Louis"

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings["user_name"], config_settings["password"]
)

def doc_get_mentions(term_to_search):
    """
    return instances of a search term and the pages it appears on
    in a series of documents for a given project
    """

    # searches document for the given term
    obj_list = client.documents.search(term_to_search)

    # loops through the results
    for document in obj_list:

        # prints the document title
        print document.title

        # for each search term found
        for mention in document.mentions:

            # prints the page and the context
            print "Page %s\n%s\n\n" % (mention.page, mention.text)

# runs the function specified
if __name__ == "__main__":
    doc_get_mentions(SEARCH_TERM)
