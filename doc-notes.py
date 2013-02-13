# doc-notes.py
# uses http://datadesk.github.com/python-documentcloud/
# searches documents for their notes, description and the pages they are on

from documentcloud import DocumentCloud
client = DocumentCloud('USERNAME', 'PASSWORD')

document_id_list = ['EXAMPLE_DOCUMENT_ID']

# get the loop length
search_length = len(document_id_list)

# set the count
count_length = 0

while (count_length < search_length):
    for document in document_id_list:

        # Fetch using the id
        obj = client.documents.get(document)

        # get the ids for the project
        obj = obj.annotations

        for item in obj:
            try:
                access = item.access
                title = item.title
                description = item.description
                page = item.page
                print '%s -- %s (%s)' % (title, description, page)

            except:
                access = item.access
                title = item.title
                page = item.page
                print '%s -- (%s)' % (title, page)

        # repeat loop
        count_length = count_length + 1
        print 'Finished'