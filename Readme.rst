
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

There's still a ton of things that need to be added but I'll only be able to do this If I get help from other people (mostly for adding support for other platforms.)

platforms
~~~~~~~~~

I've only tested topdf on Ubuntu 14.04 / 15.10 which had libreoffice, pandoc, latex, all installed. If you have that setup too, then *theoretically* it should just work fine on any platform, but if there's anything the theory has taught us, it's to never trust it without some experiments.

* need to test out windows, mac osx support
* topdf tries to be completely generic, so writing a new engine for these platforms shouldn't be too hard.

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

* RedditHandler

  * Convert Reddit permalink urls

  https://www.reddit.com/r/getdisciplined/comments/1x99m6/im_a_piece_of_shit_no_more_games_no_more_lies_no/cf9dz72


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
  * https://readthedocs.org/projects/cuckoo/downloads/
  * https://readthedocs.org/projects/cuckoo/downloads/pdf/1.1/
  * https://readthedocs.org/projects/cuckoo/downloads/pdf/latest/

* GoogleDocsHandler

  * convert normal docs.google.com links to direct download links
  * https://docs.google.com/file/d/0Bz-Gm-MUNPLFalZySjZlSHJDSEU/edit?usp=sharing
  * https://docs.google.com/uc?export=download&id=0Bz-Gm-MUNPLFalZySjZlSHJDSEU

.. random links
.. https://github.com/kxxoling/markdown2pdf/
.. http://www.xhtml2pdf.com/
