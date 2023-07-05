.. index:: linux, debian, geoip, geoip2, nginx

.. meta::
   :keywords: linux, debian, geoip, geoip2, nginx

.. _linux-nginx-geoip2-block:

GeoIP2 Block NGINX Debian 11
============================

Block or filter IPs based on location in Nginx (tested on 1.18.0) on
Debian 11.

Install Nginx modules
---------------------

To make use of the geographical filtering, we must first install the Nginx GeoIP2 module as well as the GeoIP database containing the
mappings between visitors IP addresses and their respective countries. To do so, let’s execute:



.. code-block:: none

    $ sudo apt install libnginx-mod-http-geoip2

Download the GeoIPLite2 database.

.. code-block:: none

    $ sudo mkdir /usr/share/GeoIP
    $ cd /usr/share/GeoIP
    $ sudo wget -P /tmp https://centminmod.com/centminmodparts/geoip2-lite/GeoLite2-Country.tar.gz
    $ sudo tar -xzf /tmp/GeoLite2-Country.tar.gz -C /usr/share/GeoIP --strip-components=1
    $ sudo rm COPYRIGHT.txt LICENSE.txt

Edit nginx config ``/etc/nginx/nginx.conf``. Add this below the ``http {`` line to only allow Russian IPs You can use `ISO’s full,
searchable list of all country codes <https://www.iso.org/obp/ui/#search>`_ to find your code.

.. code-block:: none

           ##
           # GeoIP database path
           ##
           
           geoip2 /usr/share/GeoIP/GeoLite2-Country.mmdb {
                  $geoip2_data_country_iso_code country iso_code;
           }
           
           ##
           # GeoIP Block
           ##
           
           map $geoip2_data_country_iso_code $allowed_country {
               default no;
               RU yes; # Russia
           }

Check config file syntax.

.. code-block:: none

    nginx -t

Finally, add this to your sites virtual config ``/etc/nginx/sites-available/siteconfig`` below ``server {``:

.. code-block:: none

        if ($allowed_country = no) {
            return 403;
        }

And reload Nginx ``sudo systemctl restart nginx``
