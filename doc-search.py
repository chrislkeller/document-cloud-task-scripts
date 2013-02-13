# doc-search.py
# uses http://datadesk.github.com/python-documentcloud/
# searches documents for a keyword

from documentcloud import DocumentCloud
client = DocumentCloud('USERNAME', 'PASSWORD')

obj_list = client.documents.search('STRING TO SEARCH FOR')

print obj_list[0]