import logging
from gulper.request import Request
from gulper.droplet import Droplet

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
