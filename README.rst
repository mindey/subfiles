.. image:: https://raw.githubusercontent.com/mindey/subfiles/master/misc/subfiles.png
    :alt: Subfiles Illustration
    :width: 100%
    :align: center

```
[.graph.json] - https://www.wikidata.org/wiki/Q182598
cat: https://www.wikidata.org/wiki/Q146
dog: https://www.wikidata.org/wiki/Q144
love: https://www.wikidata.org/wiki/Q316

[.products.csv] - https://www.wikidata.org/wiki/Q278425
url: https://www.wikidata.org/wiki/Q42253
currency: https://www.wikidata.org/wiki/Q8142
price: https://www.wikidata.org/wiki/Q160151
name: https://www.wikidata.org/wiki/Q1786779
```

Purpose
-------

Extracts file subtypes to create or append all found subtypes in a project
to a single file, e.g., .subfiles

Usage
-----

Set up::

    $ pip install subfiles

In any project, or directory, run::

    $ subfiles init > .subfiles

This will output ``.subfiles`` with all different file sub-extensions* in the project.

* sub-extension: a file extension with a second dot, e.g. sub-extension of file:
``hello.new.txt`` is ``.new.txt``.

Development reminder
====================

To publish new version on PyPI::

    $ python setup.py sdist bdist_wheel
    $ twine upload dist/*
