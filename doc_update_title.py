"""
file: doc_update_title.py
what: script to update the title of a document given its id.
"""

# import the modules for this script
from documentcloud import DocumentCloud
from config_file import config_settings

# set your document ID
DOCUMENT_ID = ""

# set your document title
NEW_DOCUMENT_TITLE = ""

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings["user_name"], config_settings["password"]
)

def doc_update_title(document_id, new_document_title):
    """
    begin function to update document metadata
    """

    # creates an object that contains the given document
    obj = client.documents.get(document_id)

    # set the new title
    obj.title = new_document_title

    # commit the change
    obj.put()

    # tell me the change has been committed
    print "Title for %s updated" % (obj)

# runs the function specified
if __name__ == "__main__":
    doc_update_title(DOCUMENT_ID, NEW_DOCUMENT_TITLE)