.. index:: mediawiki, disqus

.. _mw-configure-disqus-comments:

Configure DISQUS comments
=========================

`DISQUS <https://disqus.com>`_ предоставляет сервис системы комментариев, который можно встроить на свой сайт. Я захотел такие комментарии на свой wiki.

Установка дополнения
--------------------

Нужно установить дополнение Extension:Widgets

.. code-block:: bash

       cd (path-to-your-wiki)
       cd extensions
       git clone https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Widgets.git
       cd Widgets
       git submodule init
       git submodule update

Добавляем строчку в *LocalSettings.php*

.. code-block:: none

       # Widgets
       require_once("$IP/extensions/Widgets/Widgets.php");

Теперь создаем аккаунт в DISQUS, после чего создаем страницу Widget:DISQUS и вписываем следующий код

.. code-block:: none

  <noinclude>__NOTOC__
  This widget allows you to embed '''[http://www.disqus.com/ DISQUS Comments]''' on your wiki page.
  Created by [http://www.mediawikiwidgets.org/User:Sergey_Chernyshev Sergey Chernyshev]
  == Using this widget ==
  For information on how to use this widget, see [http://www.mediawikiwidgets.org/DISQUS widget description page on MediaWikiWidgets.org].
  == Copy to your site ==
  To use this widget on your site, just install [http://www.mediawiki.org/wiki/Extension:Widgets MediaWiki Widgets extension] and copy [{{fullurl:{{FULLPAGENAME}}|action=edit}} full source code] of this page to your wiki as '''{{FULLPAGENAME}}''' article.
  </noinclude><includeonly><div id="disqus_thread"></div>
  <script type="text/javascript">
      /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
      var disqus_shortname = '<!--{$id|escape:'urlpathinfo '}-->'; // required: replace example with your forum shortname
      <!--{if (isset($uniqid))}-->var disqus_identifier = '<!--{$uniqid|escape:'quotes'}-->';<!--{/if}-->
      <!--{if (isset($url))}-->var disqus_url = '<!--{$url|escape:'quotes'}-->';<!--{/if}-->
      /* * * DON'T EDIT BELOW THIS LINE * * */
      (function() {
          var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
          dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
          (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
      })();
  </script>
  <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
  </includeonly>

Создаем страничку *Template:Comments* и вставляем следующий код

.. code-block:: none

  {{#widget:DISQUS
  |id=<yourid>            <---- Ваш ID здесь
  |uniqid={{PAGENAME}}
  |url={{fullurl:{{PAGENAME}}}}
  }}

Для того чтобы на страничке появились комментарии достаточно вставить ``{{comments}}`` в текст страницы.

--------------

Если нужно, чтобы комментарии были внизу каждой страницы, то устанавливаем дополнение “Extension:HeaderFooter”

.. code-block:: bash

  cd (path-to-your-wiki)
  cd extensions
  git clone https://github.com/jamesmontalvo3/MediaWiki-HeaderFooter.git
  mv MediaWiki-HeaderFooter HeaderFooter

В *LocalSettings.php* добавляем строчку:

.. code-block:: none

  # Header Footer
  require_once("$IP/extensions/HeaderFooter/HeaderFooter.php");

Создаем страничку **MediaWiki:Hf-nsfooter-** cо следующим содержимым. Чуть подробнее вы можете посмотреть в мануале `Header Footer <http://www.mediawiki.org/wiki/Extension:Header_Footer>`_

.. code-block:: none

  {{comments}}

Чтобы убрать комменты с конкретной странички используйте ``__NONSFOOTER__``
