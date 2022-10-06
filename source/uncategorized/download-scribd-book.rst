.. index:: scribd, book, download, script

.. meta::
   :keywords: scribd, book, download, script

.. _download-scribd-book:

How to download a book from Scribd
==================================

При помощи скрипт можно автоматизировать просмотр страниц документа и их сохранение в файл JPG.

Для получения доступа к документу:

1. Get Trial or paid account
2. Open your book in Google Chrome (Continue Reading)
3. Open Developer Tools and go to Console
4. Paste next code and press enter

  .. code-block:: javascript

    if (injectDomToImage == undefined) {
        var injectDomToImage = document.createElement('script');
        injectDomToImage.src = "https://cdnjs.cloudflare.com/ajax/libs/dom-to-image/2.6.0/dom-to-image.min.js";
        document.getElementsByTagName('head')[0].appendChild(injectDomToImage);
    }

5. And then, you could define functions such as these:

  .. code-block:: javascript

    function downloadPage(page, prefix) {
        domtoimage.toJpeg(document.getElementsByClassName('reader_and_banner_container')[0], {
                quality: 1,
            })
            .then(function(dataUrl) {
                var link = document.createElement('a');
                link.download = `${prefix}_page_${page}.jpg`;
                link.href = dataUrl;
                link.click();
                nextPage(page, prefix);
            });
    }
    function checkPageChanged(page, oldPageCounter, prefix) {
        let newPageCounter = $('.page_counter').html();
        if (oldPageCounter === newPageCounter) {
            setTimeout(function() {
                checkPageChanged(page, oldPageCounter, prefix);
            }, 500);
        } else {
            setTimeout(function() {
                downloadPage(page + 1, prefix);
            }, 500);
        }
    }
    function nextPage(page, prefix) {
        let oldPageCounter = $('.page_counter').html();
        $('.next_btn').trigger('click');
        // Wait until page counter has changed (page loading has finished).
        checkPageChanged(page + 1, oldPageCounter, prefix);
    }
    function download(prefix) {
        downloadPage(1, prefix);
    }

6. Finally, you could download each book page as a JPG image using:

  .. code-block:: javascript

    download('test_');

--------------

Информация со `Stackoverflow <https://stackoverflow.com/questions/50293501/how-does-scribd-prevent-download>`_
