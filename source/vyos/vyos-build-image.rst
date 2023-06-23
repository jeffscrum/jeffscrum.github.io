.. index:: vyos, build, docker, iso, equuleus

.. meta::
   :keywords: vyos, docker, build, iso, equuleus

.. _vyos-build-image:

Build the image
===============

.. code-block:: bash

  # For VyOS 1.3 (equuleus)
  git clone -b equuleus --single-branch https://github.com/vyos/vyos-build
  cd vyos-build
  docker run --rm -it --privileged -v $(pwd):/vyos -w /vyos vyos/vyos-build:equuleus bash
  ./configure \
    --custom-package vim \
    --architecture amd64 \
    --build-by "j.randomhacker@vyos.io" \
    --build-type release \
    --version "1.3.1" \
    --debian-mirror "https://mirror.yandex.ru/debian" \
    --debian-security-mirror "https://mirror.yandex.ru/debian-security"
  sudo make iso

После успешной сборки готовый iso-файл будет находиться в каталоге `build` с именем `live-image-[architecture].hybrid.iso`