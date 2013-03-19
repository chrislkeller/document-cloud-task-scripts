# doc-put-metadata.py
# uses http://datadesk.github.com/python-documentcloud/
# can be used to update a document's meta data, such as
# title, source, description, related_article & published_url

from documentcloud import DocumentCloud
from docConfig import config_settings

# authenticate with document cloud
# set user_name & password in docConfig.py
client = DocumentCloud(config_settings['user_name'], config_settings['password'])

# target documents set in docConfig.py
document_list = config_settings['document_list']

# set if using a custom document cloud viewer as seen here:
# https://github.com/jfkeefe/Custom-Viewer-for-DocumentCloud
document_custom_viewer_prefix = '#'

# set to add related article URL
document_related_article_url = '#'

# begin function to update document title
def create_document_updated_title(target_document):

    '''
    this example takes a document
    that uploaded as 'last name, first name'
    and converted it to 'first name last name'
    '''

    target_title_data = target_document.split(' ')
    first_name = target_title_data[1]
    last_name = target_title_data[0]
    updated_title = first_name + ' ' + last_name
    return updated_title

# begin function to update document description
def create_document_updated_description(title, pages):

    '''
    this example takes a document
    and adds description information
    based on title and pages
    '''

    document_updated_description = 'The document titled %s contains %s pages.' % (title, pages)
    return document_updated_description

# begin function to update document metadata
def update_document_metadata():

    # loop through the list
    for document in document_list:

        # get document in list
        obj = client.documents.get(document)

        # updates document title
        obj.title = create_document_updated_title(obj.title)

        # updates description of a document
        obj.description = create_document_updated_description(obj.title, obj.pages)

        # updates the published url for a document
        # to custom document cloud viewer
        doc_viewer_url = document_custom_viewer_prefix + obj.id
        obj.published_url = doc_viewer_url

        # updates the related_article url for a document
        obj.related_article = document_related_article_url

        # writes the metadata to the document
        obj.put()

    # end group of entities for document
    print 'Finished updating metadata for %s\n' % (document)

update_document_metadata()