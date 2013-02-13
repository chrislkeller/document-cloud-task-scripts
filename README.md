document-cloud-task-scripts
===========================

## Overview

This is a collection of task-oriented *(spaghetti'd)* Python Scripts I used in conjunction with Ben Welsh's [python-documentcloud wrapper](https://github.com/datadesk/python-documentcloud) to perform basic tasks on Document Cloud files.

## Usage

Scripts require a [Document Cloud](https://www.documentcloud.org/home) account and a Document Cloud project, and Ben Welsh's [python-documentcloud wrapper](https://github.com/datadesk/python-documentcloud) installed.

        pip install python-documentcloud

**[doc-urls.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-urls.py)**

* Given a Document Cloud project id, this script will return the [document ids](http://datadesk.github.com/python-documentcloud/projects.html#project_obj.document_ids), the unique identifier of the documents assigned to this project.

**[doc-key-value-data.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-key-value-data.py)**

* Given a list of Document Cloud document ids, this script will return a series of [key/value data](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.data) -- supplementary data -- that users can add to Document Cloud documents.

**[doc-notes.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-notes.py)**

* Given a list of Document Cloud document ids, this script will return the [annotations](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.annotations) that users can add to Document Cloud documents.

**[doc-search.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-search.py)**

* Takes a string and searches Document Cloud documents for matches.

**[doc-entities.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-entities.py)**

* Given a list of Document Cloud document ids, this script will return a series of [entities](http://datadesk.github.com/python-documentcloud/otherdata.html#entities) -- people, places and organizations -- that Document Cloud extracts via [OpenCalais](http://www.opencalais.com/).

**[doc-relevance.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-relevance.py)**

* Building off of [doc-entities.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-entities.py), given a list of Document Cloud document ids, a target string and an "[entity relevance threshold](http://datadesk.github.com/python-documentcloud/otherdata.html#location_obj.revelance)," this script will return a list of  [entities](http://datadesk.github.com/python-documentcloud/otherdata.html#entities) matching the criteria.

**[doc-put-metadata.py](https://github.com/chrislkeller/document-cloud-task-scripts/blob/master/doc-put-metadata.py)**

* This script is the most *(spaghetti'd)*  of them all, and from the commented out portion you can see why.  But given a list of Document Cloud document ids this script  can be used to update a document's meta data, such as its title, source, description, related_article, published_url, access and data. The examples for [title](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.title), [description](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.description), [related_article](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.related_article), [published_url](http://datadesk.github.com/python-documentcloud/documents.html#document_obj.published_url) are commented out below.

<!--(

## Links & Resources

- [Blog Post](X)
- [Repo](X)
- [Demo](X)

)-->

## License

[The MIT License](http://opensource.org/licenses/MIT)