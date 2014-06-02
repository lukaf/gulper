import logging
from gulper.client import Client

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
log = logging.getLogger(__name__)


def client(client_id, api_key):
    return Client(client_id, api_key)
