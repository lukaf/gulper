import urllib
import urllib2
import logging
import json

log = logging.getLogger(__name__)


class Request(object):
    def __init__(self, path, uri='https://api.digitalocean.com/v1', client_id=None, api_key=None, **kwargs):
        self.uri = uri
        self.client_id = client_id
        self.api_key = api_key
        self.path = path
        self.params = {'api_key': self.api_key, 'client_id': self.client_id}
        if kwargs:
            self.params.update(kwargs)
        self.rq = '{uri}/{path}?{query}'.format(
            uri=self.uri, path=path,
            query=urllib.urlencode(self.params)
        )
        log.debug("Constructed URL: %s", self.rq)

    def send(self):
        try:
            response = urllib2.urlopen(self.rq).read()
        except urllib2.HTTPError as err:
            response = json.loads(err.read())
            log.error(response['message'])
            return None

        response = json.loads(response)
        if response['status'] == 'OK':
            return response
        log.error(response['message'])
        return None
