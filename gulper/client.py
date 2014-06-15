import logging
from gulper.request import Request
from gulper.droplet import Droplet
from gulper.ssh_key import Key

log = logging.getLogger(__name__)


class Client(object):
    """
    Client object with connection details. Methods describe different contexts of
    DigitalOcean API and return objects representing those contexts.
    """
    def __init__(self, client_id=None, api_key=None):
        self.client_id = client_id
        self.api_key = api_key
        if None in (self.client_id, self.api_key):
            raise ValueError("Missing client_id and/or api_key")
        self.credentials = {'client_id': self.client_id, 'api_key': self.api_key}

    def get_all_droplets(self):
        response = Request('droplets', client_id=self.client_id, api_key=self.api_key).send()
        if response is None:
            return None
        return [Droplet(credentials=self.credentials, **droplet_info) for droplet_info in response['droplets']]

    def get_all_ssh_keys(self):
        response = Request('ssh_keys', client_id=self.client_id, api_key=self.api_key).send()
        if response is None:
            return None
        return [Key(credentials=self.credentials, **ssh_key) for ssh_key in response['ssh_keys']]

    def create_droplet(self, name, size='512mb', image='centos-5-8-x64', region='ams1', ssh_key_ids=None, private_networking=False):
        options = {}
        options['name'] = name
        try:
            size = int(size)
            options['size_id'] = size
        except:
            options['size_slug'] = size

        try:
            image = int(image)
            options['image_id'] = image
        except:
            options['image_slug'] = image

        try:
            region = int(region)
            options['region_id'] = region
        except:
            options['region_slug'] = region

        options.update({'ssh_key_ids': ssh_key_ids, 'private_networking': private_networking})
        options.update({'credentials': self.credentials})
        droplet = Droplet(**options)
        return droplet.create()
