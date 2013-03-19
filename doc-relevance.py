# doc-relevance.py
# uses http://datadesk.github.com/python-documentcloud/
# searches entities for type, value and relevance

from documentcloud import DocumentCloud
from docConfig import config_settings

# authenticate with document cloud
# set user_name & password in docConfig.py
client = DocumentCloud(config_settings['user_name'], config_settings['password'])

# target documents set in docConfig.py
document_list = config_settings['document_list']

# string to search for in entities
target = 'Los Angeles'

# set threshold for entity relevance
relevance_threshold = 0.600

# begin function to return entity relevance
def return_entity_relevance():

    # loop through the list
    for document in document_list:

        # get document in list
        obj = client.documents.get(document)

        # get the entities from the document object
        entities = obj.entities

        # loop through entities in the document object
        for entity in entities:

            # determine which match the entity targets or the threshold
            if entity.value == target or entity.relevance > relevance_threshold:

                # see what we're getting back
                print '%s: %s (%s)' % (entity.type, entity.value, entity.relevance)

        # end group of entities for document
        print 'Finished printing entities for %s\n' % (document)

# run the function
return_entity_relevance()