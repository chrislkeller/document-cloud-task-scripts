# doc-put-metadata.py
# uses http://datadesk.github.com/python-documentcloud/
# can be used to update a document's meta data, such as
# title, source, description, related_article, published_url, access and data
# examples of title, description, related_article, published_url are commented out below

from documentcloud import DocumentCloud
client = DocumentCloud('USERNAME', 'PASSWORD')

document_id_list = ['EXAMPLE_DOCUMENT_ID']
custom_document_viewer_prefix = '#'
document_related_article_url = '#'

# get the loop length
search_length = len(document_list)

# set the count
count_length = 0

while (count_length < search_length):
    for document in document_list:

        obj = client.documents.get(document)

        ### updates document title ###
        # 'first name last name'
        # from 'last name, first name'
        #target_data = obj.title.split(',')
        #first_name = target_data[1]
        #last_name = target_data[0]
        #updated_title = first_name + ' ' + last_name
        #print updated_title
        #obj.title = updated_title

        ### updates the description for a document ###
        last_name = obj.title.split()[1]
        document_description = '%s\'s will appear in the description indicating it has %s pages.' % (last_name, obj.pages)
        print document_description
        obj.description = document_description

        ### updates the related_article url for a document ###
        #obj.related_article = document_related_article_url

        ### updates the published url for a document ###
        #doc_viewer_url = custom_document_viewer_prefix + url
        #obj.published_url = doc_viewer_url

        # writes the metadata to the document
        obj.put()

    # repeat loop
    count_length = count_length + 1
    print 'Finished'