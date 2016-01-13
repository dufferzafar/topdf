
topdf
-----

Convert anything to a beautiful PDF.

install
-------

**dependencies**

* `pandoc`
* `latex`

**package:**

`pip install topdf`

todo
----

handlers
~~~~~~~~

* IPythonNotebook
  * Handler / Engine ?
  * nbconvert --to latex --post pdf

* GithubHandler
  * convert normal github urls to raw ones and then pass on to pandoc

  https://github.com/safiyat/terminator-conf/blob/master/README.md
  https://github.com/safiyat/terminator-conf/raw/master/README.md
  https://raw.githubusercontent.com/safiyat/terminator-conf/master/README.md

engines
~~~~~~~

* GitPrintEngine
  * requires: nothing
  * will work with github markdowns only
  * pdfs are good, but don't have table of contents

  https://gitprint.com/mshang/python-elevator-challenge/blob/master/README.md?download

* QtWebkitEngine
  * requires: qt4, pyqt4
  * use python adblocker to block all sorts of ads while opening webpage

* NodeMarkdownPDFEngine
  * requires: nodejs, phantomjs
  * css based customizations
  * used by GitPrint

* GimliEngine
  * requires: ruby, wkhtmltopdf
  * does support windows
  * wkhtmltopdf allows table of contents too!
  * all markup files supported by: https://github.com/github/markup

  http://kevin.deldycke.com/uploads/2012/readme-gimli.pdf


others
~~~~~~

*this stuff doesn't make much sense in this project*

* ReadTheDocsHandler
  * given a project.readthedocs.org url, download it's latest pdf

  https://readthedocs.org/projects/cuckoo/downloads/
  https://readthedocs.org/projects/cuckoo/downloads/pdf/1.1/
  https://readthedocs.org/projects/cuckoo/downloads/pdf/latest/

* GoogleDocsHandler
  * convert normal docs.google.com links to direct download links

  https://docs.google.com/file/d/0Bz-Gm-MUNPLFalZySjZlSHJDSEU/edit?usp=sharing
  https://docs.google.com/uc?export=download&id=0Bz-Gm-MUNPLFalZySjZlSHJDSEU


.. random links
.. https://github.com/kxxoling/markdown2pdf/
.. http://www.xhtml2pdf.com/
