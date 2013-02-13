# doc-key-value-data.py
# uses http://datadesk.github.com/python-documentcloud/
# pulls key/value data associated with a document referenced in the list

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
        obj = obj.data

        for key, value in obj.iteritems():
            print '%s -- %s' % (key, value)

        # repeat loop
        count_length = count_length + 1
        print 'Finished'