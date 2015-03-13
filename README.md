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

**Scripts to work with documents**

* **[doc_get_mentions.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_get_mentions.py)**
    * return instances of a search term and the pages it appears on in a series of documents for a given project

* **[doc_update_description.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_description.py)**
    * script to update the description of a document given its id.

* **[doc_update_published_url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_published_url.py)**
    * script to update the published url of a document given its id.

* **[doc_update_related_url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_related_url.py)**
    * script to update the related url of a document given its id.

* **[doc_update_title.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_title.py)**
    * script to update the [title](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.title) of a document given its id.

**Scripts to work with projects**

* **[proj_get_doc_ids.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_get_doc_ids.py)**
    * returns the project titles and project ids associated with a given user account

* **[proj_get_doc_lengths.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_get_doc_lengths.py)**
    * gets the length of documents in a give project

* **[proj_get_doc_urls.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_get_doc_urls.py)**
    * script to get an url for each document in a given project

* **[proj_update_description.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_update_description.py)**
    * updates the description for a series of documents in a project

* **[proj_update_published_url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_update_published_url.py)**
    * updates the published url for a series of documents in a project

* **[proj_update_related_article_url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_update_related_article_url.py)**
    * updates the related article for a series of documents in a project

* **[proj_update_title.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/proj_update_title.py)**
    * Script to update the [titles](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.title) for a series of documents in a project.

**Scripts to pull metadata from documents or documents in projects**

* **[research_entities.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/research_entities.py)**
    * searches documents for their entities, organizes by highest relevance, and output data associated with each entity

* **[research_key_value_data.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/research_key_value_data.py)**
    * given a project id returns the key/value data for a document

* **[research_notes.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/research_notes.py)**
    * searches documents for their notes and details from notes and outputs








Links & Resources
=================

* [Blog Post](X)
* [Repo](https://github.com/chrislkeller/document-cloud-task-scripts)


License
=======

[The MIT License](http://opensource.org/licenses/MIT)