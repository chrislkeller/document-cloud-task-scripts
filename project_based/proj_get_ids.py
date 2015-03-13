"""
file: proj_get_doc_ids.py
what: returns the project titles and project ids associated with a given user account
"""

# import the modules for this script
from documentcloud import DocumentCloud
from config_file import config_settings

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings["user_name"], config_settings["password"]
)

def proj_get_doc_ids():
    """
    returns project ids associated with a user account
    """

    # get all of the projects for an account
    obj_list = client.projects.all()

    # loop through
    for obj in obj_list:

        # output the project title and project id
        print "%s: %s" % (obj, obj.id)

# runs the function specified
if __name__ == "__main__":
    proj_get_doc_ids()