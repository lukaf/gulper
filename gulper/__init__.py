import logging
from gulper.client import Client

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
log = logging.getLogger(__name__)


def get_all_droplets(client_id=None, api_key=None):
    global client
    client = Client(client_id, api_key)
    return client.get_all_droplets()
