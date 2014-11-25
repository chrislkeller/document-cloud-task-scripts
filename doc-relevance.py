"""
file: doc-relevance.py
what: searches for an entity string and an entity
      that matches a given relevance threshold
uses: http://datadesk.github.com/python-documentcloud/
more: https://www.documentcloud.org/help/searching
"""

from documentcloud import DocumentCloud
from ConfigFile import config_settings

# varible to hold the project we're targeting
MY_PROJECT_ID = 123345

# string to search for in entities
MY_TARGET_ENTITY = "St. Louis"

# set threshold for entity relevance
MY_TARGET_THRESHOLD = 0.600

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings["user_name"], config_settings["password"]
)

# begin function to return entity relevance
def return_targeted_entities(project_id, target_entity, target_threshold):

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

            # determine which match the entity targets or the threshold
            if entity.value == target_entity or entity.relevance >= target_threshold:

                # see what we're getting back
                print '%s: %s (%s)' % (entity.type, entity.value, entity.relevance)

        # end group of entities for document
        print 'Finished printing entities for %s\n' % (document)

# runs the function specified
if __name__ == "__main__":
    return_targeted_entities(MY_PROJECT_ID, MY_TARGET_ENTITY, MY_TARGET_THRESHOLD)