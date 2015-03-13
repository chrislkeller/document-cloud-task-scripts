document-cloud-task-scripts
===========================

* [Overview](#overview)
* [Usage](#usage)
* [Example](#example)
* [The Scripts](#the-scripts)


Overview
========

This is a collection of task-oriented <del>*(aka spaghetti'd)*</del> Python scripts I wrote to leverage [python-documentcloud wrapper](https://github.com/datadesk/python-documentcloud) written by the [Los Angeles Times Data Desk](https://github.com/datadesk) and [Ben Welsh](https://github.com/palewire) and perform batch tasks on [DocumentCloud](https://www.documentcloud.org/) files.

The documentation for [python-documentcloud wrapper](https://github.com/datadesk/python-documentcloud) is top-notch, and you could use most of the methods contained in the library via the python shell. I've always liked to create re-usable scripts, and so here are some.


Usage
======

* Using the scripts require a [Document Cloud](https://www.documentcloud.org/home) account and some files.

* Some are written to work on an individual document. Some are written to work on documents within a [given project](https://www.documentcloud.org/help/collaboration)

* The [python-documentcloud wrapper](https://github.com/datadesk/python-documentcloud) needs to be installed. Assuming you're using a [virtualenv](http://virtualenv.readthedocs.org/en/latest/) and have activated it...

    ```pip install python-documentcloud```

    ...or if you've cloned this repo

    ```pip install -r requirements.txt```

* You'll want to open the ```config_file_template.py``` file and add your user credentials. Save this as ```config_file.py```. The latter file is ignored from the repo so user credentials aren't committed by mistake, but take a look yourself and avoid committing this.

        config_settings = {
            "user_name": "USERNAME",
            "password": "PASSWORD",
        }

* Because many of these scripts need an ID to a specific DocumentCloud project, I'd start with [proj_get_doc_ids.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_get_doc_ids.py) which will give you the name of each project as well as the ID.

* Any script specific variables -- you'll see ```PROJECT_ID = 123345``` a lot -- will be near the top of the file, below the import statements. Here's an example from ```research_entities.py```

        # can be document or project
        SCOPE = "project"

        # required if scope is document
        DOCUMENT_ID = ""

        # required if scope is project
        PROJECT_ID = 1234

        # can be csv or txt
        OUTPUT = "txt"


Example
=======



The Scripts
===========

##### Scripts to work with documents

* **[doc_get_mentions.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_get_mentions.py)**
    * **What**: Given an authenticated user returns instances of a search term and the pages it appears on in a document

* **[doc_update_description.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_description.py)**
    * **What**: Given an authenticated user and a document ID updates the [description](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.description) of the document
    * **Example**:

            # creates an object that contains the given document
            obj = client.documents.get(document_id)

            # set the new title
            obj.description = new_description

            # commit the change
            obj.put()

* **[doc_update_published_url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_published_url.py)**
    * **What**: Given an authenticated user and a document ID updates the [published url](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.published_url) of the document
    * **Example**:

            # creates an object that contains the given document
            obj = client.documents.get(document_id)

            # set the new title
            obj.published_url = new_published_url

            # commit the change
            obj.put()

* **[doc_update_related_url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_related_url.py)**
    * **What**: Given an authenticated user and a document ID updates the [related article url](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.related_article) of the document
    * **Example**:

            # creates an object that contains the given document
            obj = client.documents.get(document_id)

            # set the new related article url
            obj.related_article = new_related_url

            # commit the change
            obj.put()

* **[doc_update_title.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_title.py)**
    * **What**: Given an authenticated user and a document ID updates the [title](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.title) of the document
    * **Example**:

            # creates an object that contains the given document
            obj = client.documents.get(document_id)

            # set the new title
            obj.title = new_document_title

            # commit the change
            obj.put()

##### Scripts to work with projects

* **[proj_get_ids.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_get_ids.py)**
    * **What**: Given an authenticated user returns the project name and project id the user is associated with
    * **Example**:

            2014 Ferguson Grand Jury Testimony: 16900
            California State of State Address: 12099
            2015 State of the Union: 17603

* **[proj_get_doc_lengths.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_get_doc_lengths.py)**
    * **What**: Given an authenticated user and a project ID returns the number pages in each document in the project
    * **Example**:

            [{'document': u'1371510-grand-jury-volume-5', 'pages': 286}, {'document': u'1371530-grand-jury-volume-19', 'pages': 270}, {'document': u'1371511-grand-jury-volume-6', 'pages': 270}, {'document': u'1371536-grand-jury-volume-23', 'pages': 266}, {'document': u'1371522-grand-jury-volume-13', 'pages': 258}, {'document': u'1371527-grand-jury-volume-17', 'pages': 255}, {'document': u'1371519-grand-jury-volume-12', 'pages': 255}, {'document': u'1371513-grand-jury-volume-8', 'pages': 234}, {'document': u'1371524-grand-jury-volume-15', 'pages': 231}, {'document': u'1371533-grand-jury-volume-21', 'pages': 225}, {'document': u'1371512-grand-jury-volume-7', 'pages': 215}, ...]

* **[proj_get_doc_urls.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_get_doc_urls.py)**
    * **What**: Given an authenticated user and a project ID returns an url for each document in the project
    * **Example**:

            https://www.documentcloud.org/documents/1371620-witness-40-journal-entry.html
            https://www.documentcloud.org/documents/1371619-riot-a-calls.html
            https://www.documentcloud.org/documents/1371618-radio-traffic.html
            https://www.documentcloud.org/documents/1371617-michael-brown-private-autopsy-report.html
            https://www.documentcloud.org/documents/1371616-dna-analysis-report.html

* **[proj_update_description.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_update_description.py)**
    * **What**: Given an authenticated user and a project ID updates the [description](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.description) of each document in the project
    * **Example**:

            # begin looping through each document in our list
            for document in list_of_documents:

                # get an invidual document
                doc = client.documents.get(document)

                # add the new description
                doc.description = new_description

                # commit the change
                obj.put()

* **[proj_update_published_url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_update_published_url.py)**
    * **What**: Given an authenticated user and a project ID updates the [published url](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.published_url) of each document in the project
    * **Example**:

            # begin looping through each document in our list
            for document in list_of_documents:

                # get an invidual document
                doc = client.documents.get(document)

                # add the new description
                doc.description = new_description

                # commit the change
                obj.put()

* **[proj_update_related_article_url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_update_related_article_url.py)**
    * **What**: Given an authenticated user and a project ID updates the [related article url](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.related_article) of each document in the project
    * **Example**:

            # begin looping through each document in our list
            for document in list_of_documents:

                # get an invidual document
                doc = client.documents.get(document)

                # add the new description
                doc.related_article = related_article_url

                # commit the change
                obj.put()

* **[proj_update_title.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_update_title.py)**
    * **What**: Given an authenticated user and a project ID updates the [title](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.title) of each document in the project
    * **Example**:

            # begin looping through each document in our list
            for document in list_of_documents:

                # get an invidual document
                doc = client.documents.get(document)

                # add the new description
                doc.title = new_document_title

                # commit the change
                obj.put()

##### Scripts to pull metadata from documents or documents in projects

* **[research_entities.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/research_entities.py)**
    * **What**: Given an authenticated user, and an individual document id or project id, returns the [entities](http://python-documentcloud.readthedocs.org/en/latest/otherobjects.html#entities) extracted by Document Cloud using  OpenCalais during the OCR process. Organizes the entities by highest relevance and offers ```.csv``` and ```.txt``` output files.
    * **Examples**:
        * [Document .csv output file](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/data_output/1371510-grand-jury-volume-5_entities.csv)
        * [Document .txt output file](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/data_output/1371510-grand-jury-volume-5_entities.txt)
        * [Project .csv output file](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/data_output/project_16900_entities.csv)
        * [Project .txt output file](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/data_output/project_16900_entities.txt)

* **[research_key_value_data.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/research_key_value_data.py)**
    * **What**: Given an authenticated user, and an individual document id or project id, returns the [key-value data](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.data). Offers ```.csv``` and ```.txt``` output files.

* **[research_notes.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/research_notes.py)**
    * **What**: Given an authenticated user, and an individual document id or project id, returns the notes or [annotations](http://python-documentcloud.readthedocs.org/en/latest/otherobjects.html#annotations). Offers ```.csv``` and ```.txt``` output files.
    * **Example**:
        * [Document .csv output file](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/data_output/1390043-governor-brown-sworn-in-delivers-inaugural-address_notes.csv)
        * [Document .txt output file](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/data_output/1390043-governor-brown-sworn-in-delivers-inaugural-address_notes.txt)
        * [Project .csv output file](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/data_output/project_12099_notes.csv)
        * [Project .txt output file](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/data_output/project_12099_notes.txt)


Links & Resources
=================

* [Blog Post](X)
* [Repo](https://github.com/chrislkeller/document-cloud-task-scripts)


License
=======

[The MIT License](http://opensource.org/licenses/MIT)