# doc-relevance.py
# uses http://datadesk.github.com/python-documentcloud/
# searches entities for type, value and relevance

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
        obj = obj.entities

        for item in obj:

            key = item.type
            value = item.value
            relevance = item.relevance
            target = 'STRING TO SEARCH FOR'

            if value == target or relevance > 0.400:
                print "%s: %s (%s)" % key value str(relevance)

        # repeat loop
        count_length = count_length + 1
        print 'Finished