"""
file: doc-entities-to-csv.py
what: given a project id returns entities associated with document
      in the project and writes to csv
uses: http://datadesk.github.com/python-documentcloud/
more: https://www.documentcloud.org/help/searching
"""

# import the modules for this script
from documentcloud import DocumentCloud
from ConfigFile import config_settings
import csv

# varible to hold the project we're targeting
MY_PROJECT_ID = 123345

# authenticate with document cloud with user_name & password in docConfig.py
client = DocumentCloud(
    config_settings["user_name"], config_settings["password"]
)

# function to retrieve documents from a project
def retrieve_documents_from(project_id):

    # creates an object that contains the documents in the project
    project_object = client.projects.get(id=project_id)

    # list to hold all of the documents ids
    list_of_documents = project_object.document_ids

    # creates a csv file we'll write to
    with open("doc-entities-to.csv", 'wb', buffering=0) as newCsvFile:
        dataForCsv = csv.writer(newCsvFile, delimiter=',', quoting=csv.QUOTE_ALL)

        # list to hold our csv headers
        csv_header_row = ["document", "title", "type", "value", "relevance"]

        # writes our csv headers
        dataForCsv.writerow(csv_header_row)

        # begin looping through each document in our list
        for document in list_of_documents:

            # grab this particular document
            document = client.documents.get(document)

            # loop through each entity associated with the document
            for entity in document.entities:

                # create a list that will hold data for our csv row
                data_to_csv = [
                    document.id,
                    document.title,
                    entity.type,
                    entity.value.rstrip("\n"),
                    entity.relevance
                ]

                # outputs this csv row to terminal
                print data_to_csv

                # writes this csv row to our file
                dataForCsv.writerow(data_to_csv)

        # closes our file
        newCsvFile.close()

# runs the function specified
if __name__ == "__main__":
    retrieve_documents_from(MY_PROJECT_ID)