Gulper
======

Provides interface to `DigitalOcean <https://www.digitalocean.com>`_ API.

Usage
=====

Get all droplets::

    import gulper
    droplets = gulper.droplets(client_id='id', api_key='key')
    for droplet in droplets:
        print droplet.name, droplet.status
