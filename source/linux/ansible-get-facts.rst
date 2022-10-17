.. index:: linux, ansible, facts

.. meta::
   :keywords: linux, ansible, facts

.. _ansible-get-facts:

Сбор и вывод ansible_facts
==========================

Кусочек из `документации <https://docs.ansible.com/ansible/latest/user_guide/playbooks_vars_facts.html>`_, чтобы было под рукой

Для сбора и просмотра фактов со всех хостов можно выполнить вот такой плейбук

.. code-block:: yaml

  - name: Print all available facts
    ansible.builtin.debug:
      var: ansible_facts

Еще один из вариантов, это добавить задачу в плейбук, чтобы отследить какие переменные передаются

.. code-block:: yaml

  - debug:
      msg: "{{ ansible_facts.distribution_version }}"

Либо собрать факты с одного хоста при помощи команды ``ansible <hostname> -m ansible.builtin.setup``

Если сбор фактов для конкретного плейбука (задачи) не требуется, то его можно отключить, указав

.. code-block:: yaml

  - hosts: whatever
    gather_facts: no