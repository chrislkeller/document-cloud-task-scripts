"""
file: doc-get-project-ids.py
what: returns project ids associated with a user account
uses: http://datadesk.github.com/python-documentcloud/
"""

# import the modules for this script
from documentcloud import DocumentCloud
from ConfigFile import config_settings

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings["user_name"], config_settings["password"]
)

def return_project_ids():
    obj_list = client.projects.all()
    for obj in obj_list:
        print "%s - %s" % (obj, obj.id)

if __name__ == '__main__':
    return_project_ids()