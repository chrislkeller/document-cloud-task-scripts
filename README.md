document-cloud-task-scripts
===========================

## Overview

This is a collection of task-oriented *(aka spaghetti'd)* Python scripts I wrote to leverage [python-documentcloud wrapper](https://github.com/datadesk/python-documentcloud) written by the [Los Angeles Times Data Desk](https://github.com/datadesk) and [Ben Welsh](https://github.com/palewire) to perform batch and speciality tasks on [DocumentCloud](https://www.documentcloud.org/) files.

The documentation for python-documentcloud wrapper is top-notch, and you could use most of the methods contained in the library via the python shell. I've always liked to create re-usable scripts, and so here are some.

## Usage

* Using the scripts require a [Document Cloud](https://www.documentcloud.org/home) account and some files.
* Most are written to work on documents within a [given project](https://www.documentcloud.org/help/collaboration)
* The [python-documentcloud wrapper](https://github.com/datadesk/python-documentcloud) needs to be installed. Assuming you're using a [virtualenv](http://virtualenv.readthedocs.org/en/latest/) and have activated it...

    ```pip install python-documentcloud```

    ...or if you've cloned this repo

    ```pip install -r requirements.txt```

* You'll want to open the ```ConfigFile_template.py``` file and add your user credentials. Save this as ```ConfigFile.py```. The latter file is ignored from the repo so user credentials aren't committed by mistake, but take a look yourself and avoid committing this.

* Because many of these scripts need an ID to a specific DocumentCloud project, I'd start with [doc-get-project-ids.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-get-project-ids.py) which will give you the name of each project as well as the ID.

* Any script specific variables -- you'll see ```MY_PROJECT_ID = 123345``` a lot -- will be near the top of the file, below the import statements. Here's an example from ```doc-relevance.py```

        # varible to hold the project we're targeting
        MY_PROJECT_ID = 123345

        # string to search for in entities
        MY_TARGET_ENTITY = "St. Louis"

        # set threshold for entity relevance
        MY_TARGET_THRESHOLD = 0.600

## The Scripts
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

* **[doc-put-title.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-put-title.py)**
    * Bulk method of updating the [title](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.title) for a series of documents in a project

* **[doc-relevance.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-relevance.py)**
    * Building off of [doc-entities.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-entities.py), given a project id, a target string and an "[entity relevance threshold](http://datadesk.github.com/python-documentcloud/otherdata.html#location_obj.revelance)," this script will return for each document a list of [entities](http://datadesk.github.com/python-documentcloud/otherdata.html#entities) matching the criteria.

* **[doc-return-mentions.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-return-mentions.py)**
    * Takes a string and searches Document Cloud documents for matches.

* **[doc-urls.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-urls.py)**
    * Given a Document Cloud project id, this script will return the [document ids](http://datadesk.github.com/python-documentcloud/projects.html#project_obj.document_ids), the unique identifier of the documents assigned to this project.

<!--(

## Links & Resources

- [Blog Post](X)
- [Repo](X)
- [Demo](X)

)-->

## License

[The MIT License](http://opensource.org/licenses/MIT)