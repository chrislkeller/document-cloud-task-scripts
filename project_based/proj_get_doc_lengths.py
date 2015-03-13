"""
file: proj_get_doc_lengths.py
what: gets the length of documents in a give project
"""

# import the modules for this script
from documentcloud import DocumentCloud
from config_file import config_settings

# varible to hold the project we're targeting
PROJECT_ID = 1234

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings["user_name"], config_settings["password"]
)

def proj_get_doc_lengths(project_id):
    """
    function to retrieve lengths from docs in a project
    and sort by descending doc page length
    """

    # creates an object that contains the documents in the project
    obj = client.projects.get(id = project_id)

    # list to hold all of the documents ids
    list_of_documents = []

    # begin looping through each document in our list
    for document in obj.document_ids:

        # get document in list
        doc = client.documents.get(document)

        # build a dictionary holding the title and length
        doc_dict = {
            "document": document,
            "pages": doc.pages
        }

        # append each dictionary to a list
        list_of_documents.append(doc_dict)

    # sort the list of dicts based on the pages key
    descending_list = sorted(list_of_documents, key = lambda k: k["pages"], reverse = True)

    # output the sorted list
    print descending_list

# runs the function specified
if __name__ == "__main__":
    proj_get_doc_lengths(PROJECT_ID)