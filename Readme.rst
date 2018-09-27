
topdf
-----

Convert anything to a beautiful PDF.

usage
-----

Github Readme::

    $ topdf https://github.com/user/repo/Readme.md

Stack Overflow Answer::

    $ topdf

Local files::

    $ topdf ~/Documents/{*.pptx,*.docx}

``topdf`` tries to follow the 'sane defaults' philosophy and tries to keep options to a bare minimum.


install
-------

I started writing ``topdf`` as a little wrapper around the existing tools I had, so I didn't think much about what the installation process would be like, which is why it is currently a mess.

I don't have much experience with deploying applications, so the installation procedure is not as straightforward as I'd like it to be. Any help in this area is really appreciated.

**dependencies**

These dependencies are flexible, so you don't really require them for ``topdf`` to start, they'll only be needed when you perform conversions on a particular format. For eg. Conversion from Github readmes currently uses the `GitPrint <http://gitprint.com/>`_ website and won't require any existing tool (apart from an internet connection, of course.)

* ``libreoffice`` - needed for docx, pptx etc. files
* ``pandoc`` - needed for markdown, html etc. files
* ``latex`` - required by pandoc!

**package:**::

  $ pip install topdf

todo
----

There's still a ton of things that need to be added but I don't think I'll be able to do it all on my own (adding support for other platforms especially.)

cli
~~~

* `-O, --output` option to change output file

* Allow user to select which PDF engine / Handler to use
  - Probably via a curses menu

platforms
~~~~~~~~~

I've only tested topdf on (K)ubuntu which had libreoffice, pandoc, latex, all installed. If you already have that setup, then *theoretically* it should just work fine on any platform, but if there's anything the theory has taught us, it's to never trust it without real experimentation.

* needs testing on mac osx and windows
* topdf tries to be completely generic, so writing new engines for these platforms shouldn't be too hard

* stitch all code files in a git repository (or a generic folder) into PDF ``topdf git://home/dufferzafar/dev/topdf/*.py``

windows
~~~~~~~

* test out PyInstaller for Windows
* PyQt based GUI?

handlers
~~~~~~~~

* Standard Input Handler

  * Input text could be anything!

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

* MarkdownEngine
  * Pure Python Markdown to PDF
  * Should work on Windows too
  * Integrate with Github markdowns

* GitPrintEngine

  * requires: nothing
  * will work with github markdowns only
  * pdfs are good, but don't have table of contents

  https://gitprint.com/mshang/python-elevator-challenge/blob/master/README.md?download

* CutyCapt Engine

  * requires: Qt
  * based on screenshotting the page
  * PDFs are exactly the way the webpage looks

* QtWebkitEngine

  * requires: qt4, pyqt4
  * will allow us to convert arbitrary webpages to pdf
  * use python adblocker to block all sorts of ads while opening webpage

* MSOfficeEngine

  * requires: powerpoint, word
  * will allow us to support Windows
  * might need stuff like helper `VBS <http://superuser.com/questions/641471/how-can-i-automatically-convert-powerpoint-to-pdf>`_ or `BAS <https://github.com/oleksiykovtun/Word-Export-to-PDF>`_ files or an `external tool <https://officetopdf.codeplex.com/documentation>`_

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

* Use unoconv for some stuff?

config
~~~~~~

Once we have a lot of handlers and engines, it might make sense to support some sort of configuration file (perhaps YAML based?) that will come with 'sane defaults' but will allow users to tweak topdf behaviour according to their needs.

It'll have stuff like which engine to prefer while converting a URI that can be converted by multiple engines. For eg. let's say you want to convert a Github readme file to PDF, you can either do so by using the `GitPrintEngine`, or you might want to first download the markdown of the Readme and then use the `PandocEngine`.

The config file might also store stuff like extra arguments to pass to `pandoc`, perhaps to specify a tex template to use while converting to PDF.

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

.. Register topdf organization on Github. Move geeks-pdf, codechef-pdf, topdf there.

http://crypto.stackexchange.com/a/18614/24075
