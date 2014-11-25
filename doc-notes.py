"""
file: doc-notes.py
what: searches documents for their notes, description and the pages they are on
uses: http://datadesk.github.com/python-documentcloud/
"""

from documentcloud import DocumentCloud
from ConfigFile import config_settings

# varible to hold the project we're targeting
MY_PROJECT_ID = 123345

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings["user_name"], config_settings["password"]
)

# begin function to return notes
def return_document_notes(project_id):

    # creates an object that contains the documents in the project
    project_object = client.projects.get(id=project_id)

    # list to hold all of the documents ids
    list_of_documents = project_object.document_ids

    # loop through the list
    for document in list_of_documents:

        # Fetch using the id
        obj = client.documents.get(document)

        # if there aren't notes let me know
        if len(obj.annotations) == 0:
            print "document does not have annotations"

        # otherwise
        else:
            # loop through the notes
            for note in obj.annotations:
                try:
                    print '%s: %s (%s) - (%s)' % (note.title, note.description, note.page, note.access)
                except:
                    print '%s (%s) - (%s)' % (note.title, note.page, note.access)

# runs the function specified
if __name__ == "__main__":
    return_document_notes(MY_PROJECT_ID)