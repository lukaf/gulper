import urllib
import urllib2
import logging
import json

log = logging.getLogger(__name__)


class Request(object):
    def __init__(self, path, uri='https://api.digitalocean.com', client_id=None, api_key=None):
        self.uri = uri
        self.client_id = client_id
        self.api_key = api_key
        self.path = path
        self.rq = '{uri}/{path}?{query}'.format(
            uri=self.uri, path=path,
            query=urllib.urlencode({'api_key': self.api_key, 'client_id': self.client_id}))
        log.debug("Constructed URL: %s", self.rq)

    def send(self):
        response = urllib2.urlopen(self.rq).read()
        response = json.loads(response)
        if response['status'] == 'OK':
            return response
        return None
