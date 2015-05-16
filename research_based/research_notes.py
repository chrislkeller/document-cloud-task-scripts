"""
file: research_notes.py
what: searches documents for their notes and details from notes and outputs
"""

# import the modules for this script
from documentcloud import DocumentCloud
from config_file import config_settings
import csv

class ResearchNotes(object):

    # authenticate with document cloud with user_name & password in docConfig.py
    client = DocumentCloud(
        config_settings["user_name"], config_settings["password"]
    )

    # can be document or project
    SCOPE = "document"

    # required if scope is document
    DOCUMENT_ID = ""

    # required if scope is project
    PROJECT_ID = 1234

    # can be csv or txt
    OUTPUT = "csv"

    def _init(self, *args, **kwargs):
        """
        set up the routing
        """

        # if you want notes from a document
        if self.SCOPE == "document":

            # what shall we call the output file
            output_file_prefix = "%s_notes" % (self.DOCUMENT_ID.lower())

            # build the list of notes
            notes_list = self.return_notes_from_document(self.DOCUMENT_ID)

            # sort it by ascending document title
            notes_list = self.construct_sorted_list(notes_list)

        # if you want notes from a project
        elif self.SCOPE == "project":

            # what shall we call the output file
            output_file_prefix = "project_%s_notes" % (self.PROJECT_ID)

            # build the list of notes
            notes_list = self.return_notes_from_project(self.PROJECT_ID)

            # sort it by ascending document title
            notes_list = self.construct_sorted_list(notes_list)

        # otherwise
        else:
            # we go nowhere
            print "You picked an option that is not valid"
            output_file_prefix = None
            notes_list = None

        if notes_list != None:

            # build a csv
            if self.OUTPUT == "csv":
                self.build_csv_output(output_file_prefix, notes_list)
                print "requested csv file created"

            # or build a text file
            elif self.OUTPUT == "txt":
                self.build_txt_output(output_file_prefix, notes_list)
                print "requested txt file created"

            # or do nothing because you picked an invalid option
            else:
                print "You picked an option that is not valid"


    def return_notes_from_document(self, document_id):
        """
        return notes from a single document
        """

        # get a given document based on its id
        doc = self.client.documents.get(document_id)

        # create an empty list to append notes to
        notes_list = []

        # if no notes then don't return a value
        if len(doc.annotations) == 0:
            print "* %s does not have annotations\n" % (doc)

        # otherwise
        else:

            # tell us you are building a list of entities
            print "* Building list of notes for %s\n" % (doc)

            # loop through the annotations
            for note in doc.annotations:

                # creating a dictionary
                note_dict = {
                    "doc_id": doc.id,
                    "doc_title": doc.title,
                    "note_page": note.page,
                    "note_author": note.author,
                    "note_access": note.access,
                    "note_title": note.title.encode("ascii", "ignore"),
                    "note_content": note.content.encode("ascii", "ignore"),
                }

                # append it to the empty list
                notes_list.append(note_dict)

        # return our list of notes
        return notes_list


    def return_notes_from_project(self, project_id):
        """
        return notes from documents in a project
        """

        # creates an object that contains the documents in the project
        obj = self.client.projects.get(id = project_id)

        # list to hold all of the documents ids
        list_of_documents = obj.document_ids

        # create an empty list to append notes to
        notes_list = []

        # begin looping through each document in our list
        for document_id in list_of_documents:

            # get a given document based on its id
            doc = self.client.documents.get(document_id)

            # if no notes then don't return a value
            if len(doc.annotations) == 0:
                print "* %s does not have annotations\n" % (doc)

            # otherwise
            else:

                # tell us you are building a list of entities
                print "* Building list of notes for %s\n" % (doc)

                # loop through the annotations
                for note in doc.annotations:

                    # creating a dictionary
                    note_dict = {
                        "doc_id": doc.id,
                        "doc_title": doc.title,
                        "note_page": note.page,
                        "note_author": note.author,
                        "note_access": note.access,
                        "note_title": note.title.encode("ascii", "ignore"),
                        "note_content": note.content.encode("ascii", "ignore"),
                    }

                    # append it to the empty list
                    notes_list.append(note_dict)

        # return our list of notes
        return notes_list


    def construct_sorted_list(self, entities_list):
        sorted_entities_list = sorted(entities_list, key = lambda k: k["doc_title"])
        return sorted_entities_list


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
                "doc_id",
                "doc_title",
                "note_page",
                "note_author",
                "note_access",
                "note_title",
                "note_content",
            ]

            # writes our csv headers
            csv_output_file.writerow(csv_header_row)

            # loop through each entity associated with the document
            for entity in entities_list:

                # create a list that will hold data for our csv row
                csv_data_row = [
                    entity["doc_id"],
                    entity["doc_title"],
                    entity["note_page"],
                    entity["note_author"],
                    entity["note_access"],
                    entity["note_title"].rstrip("\n"),
                    entity["note_content"].rstrip("\n"),
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
                line = "* %s\n\t* Page: %s (%s - %s)\n\t\t* %s\n\t\t\t* %s\n" % (
                    entity["doc_title"],
                    entity["note_page"],
                    entity["note_author"],
                    entity["note_access"],
                    entity["note_title"].rstrip("\n"),
                    entity["note_content"].rstrip("\n"),
                )

                # write it to the our file
                new_txt_file.write(line)


# implements the class and runs the function
if __name__ == "__main__":
    task_run = ResearchNotes()
    task_run._init()