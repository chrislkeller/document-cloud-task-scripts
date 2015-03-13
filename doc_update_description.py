"""
file: doc_update_description.py
what: script to update the description of a document given its id.
"""

# import the modules for this script
from documentcloud import DocumentCloud
from config_file import config_settings

# set your document ID
DOCUMENT_ID = ""

# set your document title
NEW_DESCRIPTION = ""

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings["user_name"], config_settings["password"]
)

def doc_update_description(document_id, new_description):
    """
    script to update the related url of a document given its id
    """

    # creates an object that contains the given document
    obj = client.documents.get(document_id)

    # set the new title
    obj.description = new_description

    # commit the change
    obj.put()

    # tell me the change has been committed
    print "Related URL for %s updated" % (obj)

# runs the function specified
if __name__ == "__main__":
    doc_update_description(DOCUMENT_ID, NEW_DESCRIPTION)