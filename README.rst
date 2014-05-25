Gulper
======

Provides interface to `DigitalOcean <https://www.digitalocean.com>`_ API.

Usage
=====

Get all droplets::

    import gulper
    droplets = gulper.get_all_droplets(client_id='id', api_key='key')
    for droplet in droplets:
        print droplet.name, droplet.status


Each droplet object can manipulate it's actual represntation.
Rebooting all droplets::

    import gulper
    droplets = gulper.get_all_Droplets(**credentials)
    for droplet in droplets:
        droplet.reboot()

