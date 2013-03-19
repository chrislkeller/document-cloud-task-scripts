# doc-key-value-data.py
# uses http://datadesk.github.com/python-documentcloud/
# pulls key-value data associated with a document referenced in the list

from documentcloud import DocumentCloud
from docConfig import config_settings

# authenticate with document cloud
# set user_name & password in docConfig.py
client = DocumentCloud(config_settings['user_name'], config_settings['password'])

# target documents set in docConfig.py
document_list = config_settings['document_list']

# begin function to return key-value data
def return_document_key_value_data():

    # loop through the list
    for document in document_list:

        # get document in list
        obj = client.documents.get(document)

        # get key-value data from the document object
        key_value = obj.data

        # loop through key-value in the document object
        for type, value in key_value.iteritems():

            # see what we're getting back
            print '%s: %s' % (type, value)

        # end group of key-value for document
        print 'Finished printing key-value data for %s\n' % (document)

# run the function
return_document_key_value_data()