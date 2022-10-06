.. index:: oracle, solaris10, zfs, patch, eis

.. meta::
   :keywords: oracle, solaris10, zfs, patch, eis

.. _oracle-solaris10-zfs-patching:

Solaris 10 + ZFS Patching
=========================

.. warning::

   * Перед выполнением обязательно нужно сделать бэкап всех ваших данных.
   * Так же обращаю внимание, что после удаления snapshot'ов восстановление будет возможно только из бэкапа.
   * В случае повреждения пула zfs или невозможности выполнить откат zfs snapshot'ов, может потребоваться восстановление из бэкапа.

План работ:

1. Распаковать архив с обновлениями 10_Recommended.zip в /tmp

2. Создать snapshot системных ФС для возможности быстрого отката на предыдущую конфигурацию (не заменяет бэкапа)

  .. code-block:: none
  
    zfs snapshot -r rpool@20210622

3. Проверить что snapshot успешно создан

  .. code-block:: none
  
    zpool set listsnapshots=on rpool
    zfs list -t snapshot

4. Перевести сервер в OBP

  .. code-block:: none
  
    init 0

5. Загрузить сервер в single user mode

  .. code-block:: none
  
    ok> boot -s

6. Перейти в каталог с обновлениями

  .. code-block:: none
  
    cd /tmp/10_Recommended

7. Запустить установку патчей

  .. code-block:: none
  
    ./installpatchset --s10patchset

8. После успешной установки патчей перезапустить сервер

  .. code-block:: none
  
    init 6

9. После перезагрузки и проверки что патчивание прошло успешно можно удалить все snapshot'ы поочередно (названия для примера)

  .. code-block:: none
  
    zfs destroy rpool@20210622
    zfs destroy rpool/ROOT@20210622
    zfs destroy rpool/dump@20210622

План отката:

1. Загружаем сервер в failsafe режиме (из OBP)

  .. code-block:: none
  
    ok> boot -F failsafe

2. Выполняем откат zfs снапшотов

  .. code-block:: none
  
    zfs rollback rpool@20210622

3. Перезагружаемся в предыдущей конфигурации системы

  .. code-block:: none
  
    init 6
