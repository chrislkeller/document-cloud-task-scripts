# doc-notes.py
# uses http://datadesk.github.com/python-documentcloud/
# searches documents for their notes, description and the pages they are on

from documentcloud import DocumentCloud
from docConfig import config_settings

# authenticate with document cloud
# set user_name & password in docConfig.py
client = DocumentCloud(config_settings['user_name'], config_settings['password'])

# target documents set in docConfig.py
document_list = config_settings['document_list']

# begin function to return notes
def return_document_notes():

    # loop through the list
    for document in document_list:

        # Fetch using the id
        obj = client.documents.get(document)

        # get notes from the document object
        document_notes = obj.annotations

        # loop through the notes
        for note in document_notes:
            try:
                print '%s: %s (%s) - (%s)' % (item.title, item.description, item.page, item.access)

            except:
                print '%s (%s) - (%s)' % (item.title, item.page, item.access)

        # end group of notes for document
        print 'Finished printing notes for %s\n' % (document)

# run the function
return_document_notes()