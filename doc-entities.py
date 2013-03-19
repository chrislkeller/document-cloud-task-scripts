# doc-entities.py
# uses http://datadesk.github.com/python-documentcloud/
# to return entities associated with a document

from documentcloud import DocumentCloud
from docConfig import config_settings

# authenticate with document cloud
# set user_name & password in docConfig.py
client = DocumentCloud(config_settings['user_name'], config_settings['password'])

# target documents set in docConfig.py
document_list = config_settings['document_list']

# begin function to return entities
def return_document_entities():

    # loop through the list
    for document in document_list:

        # get document in list
        obj = client.documents.get(document)

        # get the entities from the document object
        entities = obj.entities

        # loop through entities in the document object
        for entity in entities:

            # see what we're getting back
            print '%s: %s (%s)' % (entity.type, entity.value, entity.relevance)

        # end group of entities for document
        print 'Finished printing entities for %s\n' % (document)

# run the function
return_document_entities()