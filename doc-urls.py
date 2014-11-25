"""
file: doc-urls.py
what: gets an url for a document in a given project
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

# begin function to return document ids
def retrieve_document_urls(project_id):

    # creates an object that contains the documents in the project
    project_object = client.projects.get(id=project_id)

    # list to hold all of the documents ids
    list_of_documents = project_object.document_ids

    # begin looping through each document in our list
    for document in list_of_documents:

        # use to contruct document URLs
        urlPrefix = 'https://www.documentcloud.org/documents/'
        urlSuffix = '.html'
        url = urlPrefix + document + urlSuffix
        print url

# runs the function specified
if __name__ == "__main__":
    retrieve_document_urls(MY_PROJECT_ID)