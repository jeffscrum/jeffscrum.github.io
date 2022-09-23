.. index:: mediawiki

.. _mw-hide-talk-tab:

Скрыть закладку обсуждений
==========================

Согласно документации на `официальном сайте MediaWiki <https://www.mediawiki.org/wiki/User:Subfader/Hide_page_tabs>`_, нужно внести изменения в файл *MediaWiki:Common.css*

.. code-block:: none

   .page-Заглавная_страница #ca-talk { display: none !important; }

Теперь на заглавной странице wiki вкладка обсуждений пропадет.
