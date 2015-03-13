"""
file: proj_get_doc_urls.py
what: script to get an url for each document in a given project
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

def proj_get_doc_urls(project_id):
    """
    begin function to return document ids
    """

    # creates an object that contains the documents in the project
    obj = client.projects.get(id = project_id)

    # list to hold all of the documents ids
    list_of_documents = obj.document_ids

    # begin looping through each document in our list
    for document in list_of_documents:

        # contruct document URLs
        url_prefix = 'https://www.documentcloud.org/documents/'
        url_suffix = '.html'

        # print the document URLs
        print url_prefix + document + url_suffix

# runs the function specified
if __name__ == "__main__":
    proj_get_doc_urls(PROJECT_ID)