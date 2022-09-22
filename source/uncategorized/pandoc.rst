.. index:: linux, pandoc

.. _pandoc:

Pandoc на практике
==================

Установка Pandoc
----------------

.. note::
  
  В составе пакетов есть пакеты *LaTex*, поэтому объем занимаемый на диске будет несколько Гб

.. code-block:: bash

   aptitude install pandoc texlive texlive-xetex texlive-luatex texlive-lang-cyrillic texlive-fonts-recommended cm-super
   wget https://github.com/jgm/pandoc/releases/download/2.19.2/pandoc-2.19.2-1-amd64.deb
   dpkg -i pandoc-2.19.2-1-amd64.deb
   updmap

Markdown to PDF
---------------

Для корректной работы с русским языком требуется заменить шаблон, который формирует pandoc при передаче файла в latex. В шаблон добавлено
подключение пакетов: ``\usepackage{cmap}`` и ``\usepackage[russian]{babel}``.

Далее, при перекодировании запускаем pandoc стандартным образом, указав при этом шаблон:

.. code-block:: bash

   pandoc --template=t.tex -s rutest.md -o rutest.pdf
   pandoc --template=t.tex -V papersize=a4 -V fontsize=10pt -V documentclass=article -V geometry=left=1cm,right=1cm,top=1cm,bottom=1cm -s rutest.md -o rutest.pdf

.. tip::
  
  Скачать :download:`t.tex <_static/t.tex>`

HTML to Markdown
----------------

Скачиваем страницу из интернета и переводим ее в Markdown

.. code-block:: bash

  curl --silent https://pandoc.org/installing.html | pandoc --from html --to markdown_strict -o installing.md

Для пакетной обработки большого количества файлов можно использовать конвейер. На выходе файлы будут переконвертированы в .md, а исходные файлы будут удалены.

.. code-block:: bash

  for d in *.html; do (pandoc -s -o md-$d -f html $d -t markdown_strict && rm $d && mv md-$d $d && rename 's/.html/.md/' $d); done

Markdown to RST
----------------

Для перевода Markdown в reStructuredText используем тот же конвейер, но изменим формат трансляции.

.. code-block:: bash

  for d in *.md; do (pandoc -s -o rst-$d $d -t rst && rm $d && mv rst-$d $d && rename 's/.md/.rst/' $d); done
