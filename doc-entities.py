"""
file: doc-entities.py
what: given a project id returns entities associated with document
      in the project and writes to csv
uses: http://datadesk.github.com/python-documentcloud/
more: https://www.documentcloud.org/help/searching
"""

# import the modules for this script
from documentcloud import DocumentCloud
from docConfig import config_settings

# varible to hold the project we're targeting
MY_PROJECT_ID = 123345

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings['user_name'], config_settings['password']
)

# function to retrieve documents from a project
def retrieve_documents_from(project_id):

    # creates an object that contains the documents in the project
    project_object = client.projects.get(id=project_id)

    # list to hold all of the documents ids
    list_of_documents = project_object.document_ids

    # begin looping through each document in our list
    for document in list_of_documents:

        # grab this particular document
        document = client.documents.get(document)

        # loop through each entity associated with the document
        for entity in document.entities:

            # print the data associated with each entity
            print '%s: %s (%s)' % (entity.type, entity.value, entity.relevance)

# runs the function specified
if __name__ == "__main__":
    retrieve_documents_from(MY_PROJECT_ID)