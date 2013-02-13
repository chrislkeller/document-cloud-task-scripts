# doc-urls.py
# uses http://datadesk.github.com/python-documentcloud/
# Gets document urls for all documents in a project

from documentcloud import DocumentCloud
client = DocumentCloud('USERNAME', 'PASSWORD')

# Fetch using the id
obj = client.projects.get(id='PROJECT_NUMERIC_ID')

# get a list of docs in a project
#obj = obj.document_list

# get the ids for the project
obj = obj.document_ids

# separate the list
for item in obj:

    # set url components to var
    urlPrefix = 'https://www.documentcloud.org/documents/'
    urlSuffix = '.html'
    url = urlPrefix + item + urlSuffix

    # print the list
    print '%s' % (url)