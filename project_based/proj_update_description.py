"""
file: proj_put_description.py
what: updates the description for a series of documents in a project
"""

# import the modules for this script
from documentcloud import DocumentCloud
from config_file import config_settings

# varible to hold the project we're targeting
PROJECT_ID = 1234

# set your document title
NEW_DESCRIPTION = ""

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings["user_name"], config_settings["password"]
)

# begin function to update document metadata
def proj_put_description(project_id, new_description):
    """
    updates the description for a series of documents in a project
    """

    # creates an object that contains the documents in the project
    obj = client.projects.get(id = project_id)

    # list to hold all of the documents ids
    list_of_documents = obj.document_ids

    # begin looping through each document in our list
    for document in list_of_documents:

        # get an invidual document
        doc = client.documents.get(document)

        # add the new description
        doc.description = new_description

        # commit the change
        obj.put()

        # tell me the change has been committed
        print "Description for %s updated" % (doc)

# runs the function specified
if __name__ == "__main__":
    proj_put_description(PROJECT_ID, NEW_DESCRIPTION)
