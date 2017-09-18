# Predicting the Helpfulness of Product Reviews Using Discourse Relations

Check the [project documentation](docs/project-documentation.md) for background information.

Dependencies
------------

* python3.6
* make
* virtualenv

Building
--------

To build the complete project, execute:

    make

To delete all files that are normally created by building the program, except
distribution files, execute:

    make clean

To delete all files that are normally created by building the program,
including distribution files, execute:

    make dist-clean

Dependencies (including versions) are defined in:

	requirements.txt
	test-requirements.txt

Obtaining Data
--------------

The data used for this experiment contains:

* a development dataset of 2,000 reviews
* a cross-validation dataset of 18,000 reviews
* the explicitly expressed discourse-relation types for the complete dataset

Download the data from [Google Drive](https://drive.google.com/open?id=0B4FHGozCmQFEeTQtMUEzLWpLcTA) and extract it in the top-level directory of this project.

Testing
-------

To run all tests, execute:

	make test
