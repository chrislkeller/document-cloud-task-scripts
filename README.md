document-cloud-task-scripts
===========================

* [Overview](#overview)
* [Usage](#usage)
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

The Scripts
===========

**Scripts to work with documents**

* ```**[doc_get_mentions.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_get_mentions.py)```: return instances of a search term and the pages it appears on in a series of documents for a given project

* ```**[doc_update_description.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_description.py)```: script to update the description of a document given its id.

* ```**[doc_update_published_url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_published_url.py)```: script to update the published url of a document given its id.

* ```**[doc_update_related_url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_related_url.py)```: script to update the related url of a document given its id.

* ```**[doc_update_title.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc_update_title.py)```: script to update the [title](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.title) of a document given its id.

**Scripts to work with projects**

* ```**[proj_get_doc_ids.py](#)```:  returns the project titles and project ids associated with a given user account

* ```**[proj_get_doc_lengths.py](#)```: gets the length of documents in a give project

* ```**[proj_get_doc_urls.py](#)```: script to get an url for each document in a given project

* ```**[proj_update_description.py](#)```: updates the description for a series of documents in a project

* ```**[proj_update_published_url.py](#)```: updates the published url for a series of documents in a project

* ```**[proj_update_related_article_url.py](#)```: updates the related article for a series of documents in a project

* ```**[proj_update_title.py](#)```: Script to update the [titles](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.title) for a series of documents in a project.

**Scripts to pull metadata from documents or documents in projects**

* ```**[research_entities.py](#)```: searches documents for their entities, organizes by highest relevance, and output data associated with each entity

* ```**[research_key_value_data.py](#)```: given a project id returns the key/value data for a document

* ```**[research_notes.py](#)```: searches documents for their notes and details from notes and outputs











* **[doc-get-project-ids.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-get-project-ids.py)**
    * Given an authenticated user, returns the project name and project id for each the user is associated with.

* **[doc-entities-to-csv.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-entities-to-csv.py)**
    * Given a project id returns for each document [entities](http://datadesk.github.com/python-documentcloud/otherdata.html#entities) -- people, places and organizations -- that Document Cloud extracts via [OpenCalais](http://www.opencalais.com/) --associated with each document in the project, and writes each entity type, entity value and entity relevance to a [csv](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/data-output/doc-entities-to.csv).

* **[doc-entities.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-entities.py)**
    * Given a project id returns for each document [entities](http://datadesk.github.com/python-documentcloud/otherdata.html#entities) -- people, places and organizations -- that Document Cloud extracts via [OpenCalais](http://www.opencalais.com/) -- associated with each document in the project.

* **[doc-key-value-data.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-key-value-data.py)**
    * Given a project id returns for each document a series of [key/value data](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.data) -- supplementary data -- that users can add to Document Cloud documents.

* **[doc-notes.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-notes.py)**
    * Given a project id returns for each document the [annotations](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.annotations) that users can add to Document Cloud documents.

* **[doc-page-length.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-page-length.py)**
    * Given a project id returns for each document the [document title and the number of pages](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/data-output/doc-page-length.csv) it contains.

* **[doc-put-description.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-put-description.py)**
    * Bulk method of updating the [description](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.description) for a series of documents in a given project.

* **[doc-put-published-url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-put-published-url.py)**
    * Bulk method of updating the [published_url](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.published_url) for a series of documents in a project.

* **[doc-put-related-article-url.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-put-related-article-url.py)**
    * Bulk method of updating the [related_article](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.related_article) for a series of documents in a project.

* **[doc-relevance.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-relevance.py)**
    * Building off of [doc-entities.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-entities.py), given a project id, a target string and an "[entity relevance threshold](http://datadesk.github.com/python-documentcloud/otherdata.html#location_obj.revelance)," this script will return for each document a list of [entities](http://datadesk.github.com/python-documentcloud/otherdata.html#entities) matching the criteria.

* **[doc-return-mentions.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-return-mentions.py)**
    * Takes a string and searches Document Cloud documents for matches.

* **[doc-urls.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-urls.py)**
    * Given a Document Cloud project id, this script will return the [document ids](http://datadesk.github.com/python-documentcloud/projects.html#project_obj.document_ids), the unique identifier of the documents assigned to this project.

<!--(

## Links & Resources

- [Blog Post](X)
- [Repo](https://github.com/chrislkeller/document-cloud-task-scripts)

)-->

## License

[The MIT License](http://opensource.org/licenses/MIT)






