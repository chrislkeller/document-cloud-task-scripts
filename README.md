document-cloud-task-scripts
===========================

* [Overview](#overview)
* [Example Setup and Usage](#example-setup-and-usage)
* [The Scripts](#the-scripts)


Overview
========

This is a collection of task-oriented <del>*(aka spaghetti'd)*</del> Python scripts I wrote to leverage [python-documentcloud wrapper](https://github.com/datadesk/python-documentcloud) written by the [Los Angeles Times Data Desk](https://github.com/datadesk) and [Ben Welsh](https://github.com/palewire) and perform batch tasks on [DocumentCloud](https://www.documentcloud.org/) files.

The documentation for [python-documentcloud wrapper](https://github.com/datadesk/python-documentcloud) is top-notch, and you could use most of the methods contained in the library via the python shell. I've always liked to create re-usable scripts, and so here are some.


Example Setup and Usage
=======================

##### Example Setup

* Using the scripts require a [Document Cloud](https://www.documentcloud.org/home) account and some files added to your account.

* [python-documentcloud wrapper](https://github.com/datadesk/python-documentcloud) needs to be installed. Assuming you're using a [virtualenv](http://virtualenv.readthedocs.org/en/latest/) and have activated it...

    ```pip install python-documentcloud```

    ...or if you've cloned this repo

    ```pip install -r requirements.txt```

* You'll want to open the ```config_file_template.py``` file and add your [Document Cloud](https://www.documentcloud.org/home) username and password. Save this as ```config_file.py```. It should contain:

        config_settings = {
            "user_name": "USERNAME",
            "password": "PASSWORD",
        }

    * ```config_file.py``` is ignored from the repo so user credentials aren't committed by mistake. **But take a look yourself and avoid committing this file**.

##### Example Usage

* Some scripts are written to work on an individual document. These are prefaced with ```doc_```. Some are written to work on documents within a [given project](https://www.documentcloud.org/help/collaboration). These are prefaced with ```proj_```. Others will work on either an invidual document or on each document in a project. These are prefaced with ```research_```.

* I'm a big fan of Document Cloud's use of Open Calais for entity extraction. Depending on the shape of the PDFs when I upload, I find it to be a nice high-level view of data available in the documents.

* Let's export the entities from the documents related to the St. Louis County grand jury investigation into the Aug. 9, 2014 shooting of Michael Brown by Ferguson police officer Darren Wilson. The 752 MB zip file contained nearly 80 PDF files filled with grand jury testimony, reports and forensic evidence and interviews with witnesses that spanned more than 6,000 pages.

* In my Document Cloud instance, the project containing the grand jury documents is ```12345```. So I will open ```research_entities.py``` and set the ```SCOPE``` variable to "project" and add 16900 to the ```PROJECT_ID``` variable. I won't be using an individual document for now, so I can set that to ```None``` and let's output a ```.csv``` file to start with.

        # can be document or project
        SCOPE = "project"

        # required if scope is document
        DOCUMENT_ID = None

        # required if scope is project
        PROJECT_ID = 12345

        # can be csv or txt
        OUTPUT = "csv"

* Hopefully that is all you have to changce. ```cd``` into the scripts repo and run ```python research_entities.py``` and if everything goes right you should see something like this for your particular project.

        "document","title","type","value","relevance"
        "0.948","Wilson Wilson","person","Interview Po Darren Wilson","1371540-interview-po-darren-wilson"
        "0.914","Michael Brown","person","Interview Witness 41 2","1371579-interview-witness-41-2"
        "0.899","Michael Brown","person","Interview Witness 37","1371569-interview-witness-37"
        "0.885","Michael Brown","person","Interview Witness 14 1","1371548-interview-witness-14-1"
        "0.884","Ok","person","Interview Witness 48 1","1371587-interview-witness-48-1"
        "0.881","Michael Brown","person","Interview Witness 41 1","1371578-interview-witness-41-1"
        "0.874","Gordon Brown","person","Interview Witness 42","1371580-interview-witness-42"
        "0.865","I. Ok","person","Interview Witness 35","1371567-interview-witness-35"
        "0.855","Michael Brown","person","Interview Witness 44 2","1371582-interview-witness-44-2"
        "0.828","Michael Brown","person","Interview Witness 12 3","1371545-interview-witness-12-3"


The Scripts
===========

##### Scripts to work with documents

* **[doc_get_mentions.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_get_mentions.py)**
    * **What**: Given an authenticated user returns instances of a search term and the pages it appears on in a document.

* **[doc_update_description.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_description.py)**
    * **What**: Given an authenticated user and a document ID updates the [description](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.description) of the document.
    * **Example**:

            # creates an object that contains the given document
            obj = client.documents.get(document_id)

            # set the new title
            obj.description = new_description

            # commit the change
            obj.put()

* **[doc_update_published_url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_published_url.py)**
    * **What**: Given an authenticated user and a document ID updates the [published url](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.published_url) of the document.
    * **Example**:

            # creates an object that contains the given document
            obj = client.documents.get(document_id)

            # set the new title
            obj.published_url = new_published_url

            # commit the change
            obj.put()

* **[doc_update_related_url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_related_url.py)**
    * **What**: Given an authenticated user and a document ID updates the [related article url](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.related_article) of the document.
    * **Example**:

            # creates an object that contains the given document
            obj = client.documents.get(document_id)

            # set the new related article url
            obj.related_article = new_related_url

            # commit the change
            obj.put()

* **[doc_update_title.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_title.py)**
    * **What**: Given an authenticated user and a document ID updates the [title](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.title) of the document.
    * **Example**:

            # creates an object that contains the given document
            obj = client.documents.get(document_id)

            # set the new title
            obj.title = new_document_title

            # commit the change
            obj.put()

##### Scripts to work with projects

* **[proj_get_ids.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_get_ids.py)**
    * **What**: Given an authenticated user returns the project name and project id the user is associated with. Because many of these scripts need an ID to a specific Document Cloud project I like starting with this script.
    * **Example**:

            2014 Ferguson Grand Jury Testimony: 16900
            California State of State Address: 12099
            2015 State of the Union: 17603

* **[proj_get_doc_lengths.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_get_doc_lengths.py)**
    * **What**: Given an authenticated user and a project ID returns the number pages in each document in the project.
    * **Example**:

            [{'document': u'1371510-grand-jury-volume-5', 'pages': 286}, {'document': u'1371530-grand-jury-volume-19', 'pages': 270}, {'document': u'1371511-grand-jury-volume-6', 'pages': 270}, {'document': u'1371536-grand-jury-volume-23', 'pages': 266}, {'document': u'1371522-grand-jury-volume-13', 'pages': 258}, {'document': u'1371527-grand-jury-volume-17', 'pages': 255}, {'document': u'1371519-grand-jury-volume-12', 'pages': 255}, {'document': u'1371513-grand-jury-volume-8', 'pages': 234}, {'document': u'1371524-grand-jury-volume-15', 'pages': 231}, {'document': u'1371533-grand-jury-volume-21', 'pages': 225}, {'document': u'1371512-grand-jury-volume-7', 'pages': 215}, ...]

* **[proj_get_doc_urls.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_get_doc_urls.py)**
    * **What**: Given an authenticated user and a project ID returns an url for each document in the project.
    * **Example**:

            https://www.documentcloud.org/documents/1371620-witness-40-journal-entry.html
            https://www.documentcloud.org/documents/1371619-riot-a-calls.html
            https://www.documentcloud.org/documents/1371618-radio-traffic.html
            https://www.documentcloud.org/documents/1371617-michael-brown-private-autopsy-report.html
            https://www.documentcloud.org/documents/1371616-dna-analysis-report.html

* **[proj_update_description.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_update_description.py)**
    * **What**: Given an authenticated user and a project ID updates the [description](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.description) of each document in the project.
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
    * **What**: Given an authenticated user and a project ID updates the [published url](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.published_url) of each document in the project.
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
    * **What**: Given an authenticated user and a project ID updates the [related article url](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.related_article) of each document in the project.
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
    * **What**: Given an authenticated user and a project ID updates the [title](http://python-documentcloud.readthedocs.org/en/latest/documents.html#document_obj.title) of each document in the project.
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

* <del>Blog Post</del>
* [Repo](https://github.com/chrislkeller/document-cloud-task-scripts)


License
=======

[The MIT License](http://opensource.org/licenses/MIT)