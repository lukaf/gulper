from gulper.request import Request

import StringIO
import logging


logger = logging.getLogger(__name__)


class Key(object):
    def __init__(self, **kwargs):
        self.id = None
        self.name = None
        self.credentials = None

        self.__dict__.update(kwargs)

    def _request(self, path, **kwargs):
        options = {}
        if kwargs:
            options.update(kwargs)
        options.update(self.credentials)
        return Request(path, **options).send()

    def create_from_file(self, name, fp):
        try:
            ssh_key = fp.read()
        except:
            logger.error("Failed to read from %r", fp)
            raise

        response = self._request('ssh_keys/new', name=name, ssh_pub_key=ssh_key)
        if response and response.get('status', '') == 'OK':
            self.__dict__.update(response['status'])
            return self
        return response

    def create_from_filename(self, name, filename):
        with open(filename, 'rb') as fp:
            return self.create_from_file(name, fp)

    def create_from_string(self, name, data):
        if isinstance(data, unicode):
            data = data.encode('utf-8')
        fp = StringIO.StringIO(data)
        response = self.create_from_file(name, fp)
        fp.close()
        return response

    def destroy(self):
        return self._request('ssh_keys/{9}/destroy'.format(self.id))

    def edit_from_file(self, fp):
        try:
            ssh_key = fp.read()
        except:
            logger.error("Failed to read %r.", fp)
            raise

        response = self._request('ssh_keys/{0}/edit'.format(self.id), name=self.name, ssh_pub_key=ssh_key)
        if response and response.get('status', '') == 'OK':
            self.__dict__.update(response['status'])
            return self
        return response

    def edit_from_filename(self, filename):
        with open(filename, 'rb') as fp:
            return self.edit_from_file(fp)

    def edit_from_string(self, data):
        if isinstance(data, unicode):
            data = data.encode('utf-8')
        fp = StringIO.StringIO(data)
        response = self.create_from_file(fp)
        fp.close()
        return response
