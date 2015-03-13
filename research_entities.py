"""
file: research_entities.py
what: searches documents for their entities, organizes by highest relevance, and output data associated with each entity
"""

# import the modules for this script
from documentcloud import DocumentCloud
from config_file import config_settings
import csv

class ResearchEntities(object):

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

        # if you want entities from a document
        if self.SCOPE == "document":

            # what shall we call the output file
            output_file_prefix = "%s_entities" % (self.DOCUMENT_ID.lower())

            # build the list of entities
            entities_list = self.return_entities_from_document(self.DOCUMENT_ID)

            # sort it by descending relevance
            descending_entities_list = self.construct_descending_list(entities_list)

        # if you want entities from a project
        elif self.SCOPE == "project":

            # what shall we call the output file
            output_file_prefix = "project_%s_entities" % (self.PROJECT_ID)

            # build the list of entities
            entities_list = self.return_entities_from_project(self.PROJECT_ID)

            # sort it by descending relevance
            descending_entities_list = self.construct_descending_list(entities_list)

        else:
            print "You picked an option that is not valid"
            output_file_prefix = None
            descending_entities_list = None

        if descending_entities_list != None:

            # build a csv
            if self.OUTPUT == "csv":
                self.build_csv_output(output_file_prefix, descending_entities_list)
                print "requested csv file created"

            # or build a text file
            elif self.OUTPUT == "txt":
                self.build_txt_output(output_file_prefix, descending_entities_list)
                print "requested txt file created"

            # or do nothing because you picked an invalid option
            else:
                print "You picked an option that is not valid"


    def return_entities_from_document(self, document_id):
        """
        return entities from a single document
        """

        # get a given document based on its id
        doc = self.client.documents.get(document_id)

        # create an empty list to append to
        entities_list = []

        # if no entities then don't return a value
        if len(doc.entities) == 0:
            print "* %s does not have entities\n" % (doc)

        # otherwise
        else:

            # loop through the entities
            for entity in doc.entities:

                # creating a dictionary
                entity_dict = {
                    "id": doc.id,
                    "title": doc.title,
                    "type": entity.type,
                    "value": entity.value.encode("ascii", "ignore"),,
                    "relevance": entity.relevance,
                }

                # append it to the empty list
                entities_list.append(entity_dict)

        # return our list of entities
        return entities_list


    def return_entities_from_project(self, project_id):
        """
        return entities from documents in a project
        """

        # creates an object that contains the documents in the project
        obj = self.client.projects.get(id = project_id)

        # list to hold all of the documents ids
        list_of_documents = obj.document_ids

        # create an empty list to append to
        entities_list = []

        # begin looping through each document in our list
        for document_id in list_of_documents:

            # get a given document based on its id
            doc = self.client.documents.get(document_id)

            # if no entities then don't return a value
            if len(doc.entities) == 0:
                print "* %s does not have entities\n" % (doc)

            # otherwise
            else:

                # tell us you are building a list of entities
                print "* Building list of entities for %s" % (doc)

                # loop through the entities
                for entity in doc.entities:

                    # creating a dictionary
                    entity_dict = {
                        "id": doc.id,
                        "title": doc.title,
                        "type": entity.type,
                        "value": entity.value.encode("ascii", "ignore"),,
                        "relevance": entity.relevance,
                    }

                    # append it to the empty list
                    entities_list.append(entity_dict)

        # return our list of entities
        return entities_list


    def construct_descending_list(self, entities_list):
        descending_entities_list = sorted(entities_list, key = lambda k: k["relevance"], reverse = True)
        return descending_entities_list


    def build_csv_output(self, output_file_prefix, entities_list):
        """
        build a csv report of entities found in a document cloud document
        """

        output_file_path = "data_output/%s.csv" % (output_file_prefix)

        # creates a csv file we'll write to
        with open(output_file_path, "wb", buffering=0) as new_csv_file:
            csv_output_file = csv.writer(new_csv_file, delimiter=',', quoting=csv.QUOTE_ALL)

            # list to hold our csv headers
            csv_header_row = [
                "document",
                "title",
                "type",
                "value",
                "relevance",
            ]

            # writes our csv headers
            csv_output_file.writerow(csv_header_row)

            # loop through each entity associated with the document
            for entity in entities_list:

                # create a list that will hold data for our csv row
                csv_data_row = [
                    entity["relevance"],
                    entity["value"].rstrip("\n"),
                    entity["type"],
                    entity["title"],
                    entity["id"],
                ]

                # writes this csv row to our file
                csv_output_file.writerow(csv_data_row)


    def build_txt_output(self, output_file_prefix, entities_list):
        """
        build a csv report of entities found in a document cloud document
        """

        output_file_path = "data_output/%s.txt" % (output_file_prefix)

        # creates a txt file we'll write to
        with open(output_file_path, "wb") as new_txt_file:

            # loop through our list of entities
            for entity in entities_list:

                # create a text line
                line = "\n* %s: %s (%s)\n\t* %s\n" % (
                    entity["relevance"],
                    entity["value"].rstrip("\n"),
                    entity["type"],
                    entity["title"],
                )

                # write it to the our file
                new_txt_file.write(line)


# implements the class and runs the function
if __name__ == "__main__":
    task_run = ResearchEntities()
    task_run._init()