"""
file: doc-page-length.py
what: gets the length of documents in a give project
uses: http://datadesk.github.com/python-documentcloud/
"""

# import the modules for this script
from documentcloud import DocumentCloud
from ConfigFile import config_settings

# varible to hold the project we're targeting
MY_PROJECT_ID = 123345

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings["user_name"], config_settings["password"]
)

# function to retrieve page length from documents in a project
def retrieve_number_of_pages(project_id):

    # creates an object that contains the documents in the project
    project_object = client.projects.get(id=project_id)

    # list to hold all of the documents ids
    list_of_documents = project_object.document_ids

    # begin looping through each document in our list
    for document in list_of_documents:

        # get document in list
        obj = client.documents.get(document)

        # get the entities from the document object
        number_of_pages = obj.pages

        # see what we're getting back
        print "%s, %s" % (document, number_of_pages)

# runs the function specified
if __name__ == "__main__":
    retrieve_number_of_pages(MY_PROJECT_ID)