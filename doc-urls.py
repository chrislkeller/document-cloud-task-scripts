# doc-urls.py
# uses http://datadesk.github.com/python-documentcloud/
# Gets document urls for all documents in a project

from documentcloud import DocumentCloud
from docConfig import config_settings

# authenticate with document cloud
# set user_name & password in docConfig.py
client = DocumentCloud(config_settings['user_name'], config_settings['password'])

# target projects
project_list = ['EXAMPLE_PROJECT_ID']

# begin function to return document ids
def return_document_ids():

    # create an empty document list
    document_id_list = []

    # loop through the list
    for project in project_list:

        # get project in list
        obj = client.projects.get(project)

        # get the ids for each document in the project
        document_ids = obj.document_ids

        # loop through ids in the document object
        for document in document_ids:

            # use to contruct document URLs
            urlPrefix = 'https://www.documentcloud.org/documents/'
            urlSuffix = '.html'
            url = urlPrefix + document + urlSuffix

            # use to construct a document_list
            output = '%s' % (str(document))
            document_id_list.append(output)

    # see what we're getting back
    print document_id_list

# run the function
return_document_ids()