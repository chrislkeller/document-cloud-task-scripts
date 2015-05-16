"""
file: _research_key_value_data.py
what: given a project id returns the key/value data for a document
"""

# import the modules for this script
from documentcloud import DocumentCloud
from config_file import config_settings
import csv

class ResearchKeyValue(object):

    # authenticate with document cloud with user_name & password in docConfig.py
    client = DocumentCloud(
        config_settings["user_name"], config_settings["password"]
    )

    # can be document or project
    SCOPE = "project"

    # required if scope is document
    DOCUMENT_ID = ""

    # required if scope is project
    PROJECT_ID = 1234

    # can be csv or txt
    OUTPUT = "txt"

    def _init(self, *args, **kwargs):
        """
        set up the routing
        """

        # if you want notes from a document
        if self.SCOPE == "document":

            # build the list of notes
            data_list = self.return_data_from_document(self.DOCUMENT_ID)

        # if you want notes from a project
        elif self.SCOPE == "project":

            # build the list of notes
            data_list = self.return_data_from_project(self.PROJECT_ID)

        # otherwise
        else:
            # we go nowhere
            print "You picked an option that is not valid"
            data_list = None

        if data_list != None:

            # build a csv
            if self.OUTPUT == "csv":
                self.build_csv_output(data_list)
                print "requested csv file created"

            # or build a text file
            elif self.OUTPUT == "txt":
                self.build_txt_output(data_list)
                print "requested txt file created"

            # or do nothing because you picked an invalid option
            else:
                print "You picked an option that is not valid"


    def return_data_from_document(self, document_id):
        """
        return notes from a single document
        """

        # get a given document based on its id
        doc = self.client.documents.get(document_id)

        # create an empty list to append notes to
        data_list = []

        # if no notes then don't return a value
        if len(doc.data) == 0:
            print "* %s does not have key-value data\n" % (doc)

        # otherwise
        else:

            # tell us you are building a list of entities
            print "* Building list of key-value data for %s\n" % (doc)

            data_dict = {
                "doc_id": doc.id,
                "doc_title": doc.title,
                "doc_data": doc.data,
            }

            data_list.append(data_dict)

        # return our list of key-value data
        return data_list


    def return_data_from_project(self, project_id):
        """
        return notes from documents in a project
        """

        # creates an object that contains the documents in the project
        obj = self.client.projects.get(id = project_id)

        # list to hold all of the documents ids
        list_of_documents = obj.document_ids

        # create an empty list to append notes to
        data_list = []

        # begin looping through each document in our list
        for document_id in list_of_documents:

            # get a given document based on its id
            doc = self.client.documents.get(document_id)

            # if no notes then don't return a value
            if len(doc.data) == 0:
                print "* %s does not have key-value data\n" % (doc)

            # otherwise
            else:

                # tell us you are building a list of entities
                print "* Building list of key-value data for %s\n" % (doc)

                data_dict = {
                    "doc_id": doc.id,
                    "doc_title": doc.title,
                    "doc_data": doc.data,
                }

                data_list.append(data_dict)

        # return our list of key-value data
        return data_list

    def build_csv_output(self, data_list):
        """
        build a csv report of key-value data found in a document cloud document
        """

        # creates a csv file we'll write to
        with open("_output_key_value_data.csv", 'wb', buffering=0) as new_csv_file:
            csv_output_file = csv.writer(new_csv_file, delimiter=',', quoting=csv.QUOTE_ALL)

            # list to hold our csv headers
            csv_header_row = [
                "doc_id",
                "doc_title",
                "key",
                "value",
            ]

            # writes our csv headers
            csv_output_file.writerow(csv_header_row)

            # loop through our list of key-value data
            for item in data_list:

                # isolate the keys and values
                for key, value in item["doc_data"].iteritems():

                    # create a list that will hold data for our csv row
                    csv_data_row = [
                        item["doc_id"],
                        item["doc_title"],
                        key,
                        value,
                    ]

                    # writes this csv row to our file
                    csv_output_file.writerow(csv_data_row)


    def build_txt_output(self, data_list):
        """
        build a txt report of key-value data found in a document cloud document
        """

        # creates a txt file we'll write to
        with open("_output_key_value_data.txt", "w") as new_txt_file:

            # loop through our list of key-value data
            for item in data_list:

                # write a line with our document title
                new_txt_file.write("* %s\n" % (item["doc_title"]))

                # isolate the keys and values
                for key, value in item["doc_data"].iteritems():

                    # create a text line
                    line = "\t* %s: %s\n" % (key, value)

                    # write it to the our file
                    new_txt_file.write(line)


# implements the class and runs the function
if __name__ == "__main__":
    task_run = ResearchKeyValue()
    task_run._init()