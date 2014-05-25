import logging
from gulper.client import Client

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
log = logging.getLogger(__name__)


def droplet(id=None):
    # initialize client and send a request
    pass


def droplets(client_id=None, api_key=None):
    global client
    client = Client(client_id, api_key)
    return client.droplets()


def key():
    pass


def domain():
    pass
