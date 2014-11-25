"""
file: doc-key-value-data.py
what: given a project id returns the key/value data for a document
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

# begin function to return key-value data
def return_document_key_value_data(project_id):

    # creates an object that contains the documents in the project
    project_object = client.projects.get(id=project_id)

    # list to hold all of the documents ids
    list_of_documents = project_object.document_ids

    # loop through the list
    for document in list_of_documents:

        # get document in list
        obj = client.documents.get(document)

        # get key-value data from the document object
        key_value = obj.data

        # loop through key-value in the document object
        for type, value in key_value.iteritems():

            # see what we're getting back
            print '%s: %s' % (type, value)

# runs the function specified
if __name__ == "__main__":
    return_document_key_value_data(MY_PROJECT_ID)