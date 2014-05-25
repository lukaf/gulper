# TODO:
# test droplet
from gulper.request import Request


class Droplet(object):
    def __init__(self, **kwargs):
        self.id = None
        self.name = None
        self.image_id = None
        self.size_id = None
        self.region_id = None
        self.backups_active = None
        self.ip_address = None
        self.private_ip_address = None
        self.locked = None
        self.status = None
        self.created_at = None
        self.credentials = None

        self.__dict__.update(kwargs)

    def _status_update(self, response, state):
        if response is not None:
            self.status = state
        return response

    def _request(self, path):
        return Request(path, **self.credentials).send()

    def update(self):
        response = self._request('droplet/{0}'.format(self.id))
        if 'status' in response and response['status'] == 'OK':
            self.__dict__.update(response['droplet'])
            return True
        return None

    def reboot(self):
        response = self._request('droplet/{0}/reboot'.format(self.id))
        return self._status_update(response, 'reboot')

    def power_cycle(self):
        response = self._request('droplet/{0}/power_cycle'.format(self.id))
        return self._status_update(response, 'power_cycle')

    def shutdown(self):
        response = self._request('droplet/{0}/shutdown'.format(self.id))
        return self._status_update(response, 'shutdown')

    def poweroff(self):
        response = self._request('droplet/{0}/power_off'.format(self.id))
        return self._status_update(response, 'poweroff')

    def poweron(self):
        response = self._request('droplet/{0}/power_on'.format(self.id))
        return self._status_update(response, 'poweron')

    def password_reset(self):
        return self._request('droplet/{0}/password_reset')

    def resize(self):
        raise NotImplementedError()
