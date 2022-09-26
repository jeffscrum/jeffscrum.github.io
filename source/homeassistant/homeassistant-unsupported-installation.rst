.. index:: homeassistant, unsupported

.. _homeassistant-unsupported-installation:

Unsupported Installation
========================

Supervisor unhealthy state

Такой статус влечет за собой невозможность обновления версии и обновлений аддонов. 

Вариантов решения проблемы на самом деле 3:

- Вариант 1: Переустановка системы

- Вариант 2: Временное решение - игнорировать ошибки. Ниже привожу пример как включить игнор ошибок

  .. code-block:: bash

    cd /usr/share/hassio/homeassistant
    ha jobs options --ignore-conditions healthy

- Вариант 3: Повторный запуск установки Supervisor

  .. code-block:: bash

    curl -Lo installer.sh https://raw.githubusercontent.com/jeffscrum/supervised-installer/master/installer.sh
    bash installer.sh --machine intel-nuc
