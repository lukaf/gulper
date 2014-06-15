from gulper.request import Request


class Droplet(object):
    def __init__(self, **kwargs):
        self.id = None
        self.name = None
        self.image_id = None
        self.size_id = None
        self.region_id = None
        self.backups_active = False
        self.ip_address = None
        self.private_ip_address = None
        self.locked = None
        self.status = None
        self.created_at = None
        self.ssh_key_ids = None
        self.private_networking = None

        self.__dict__.update(kwargs)

    def _status_update(self, response, state):
        if response is not None:
            self.status = state
        return response

    def _request(self, path, **kwargs):
        options = {}
        if kwargs:
            options.update(kwargs)
        options.update(self.credentials)
        return Request(path, **options).send()

    def create(self, ssh_key_ids=None, private_networking=False):
        if ssh_key_ids is None:
            ssh_key_ids = self.ssh_key_ids

        if private_networking is False:
            private_networking = self.private_networking

        options = {'name': self.name}
        try:
            options['size_slug'] = self.size_slug
        except:
            options['size_id'] = self.size_id

        try:
            options['image_slug'] = self.image_slug
        except:
            options['image_id'] = self.image_id

        try:
            options['region_slug'] = self.region_slug
        except:
            options['region_id'] = self.region_id

        options.update({'ssh_key_ids': ssh_key_ids, 'private_networking': private_networking})
        response = self._request('droplets/new', **options)
        if response is None:
            return response
        if 'status' in response and response['status'] == 'OK':
            self.__dict__.update(response['droplet'])
        return self

    def update(self):
        response = self._request('droplets/{0}'.format(self.id))
        if response is None:
            return response
        if 'status' in response and response['status'] == 'OK':
            self.__dict__.update(response['droplet'])
            return True
        return False

    def reboot(self):
        response = self._request('droplets/{0}/reboot'.format(self.id))
        return self._status_update(response, 'reboot')

    def power_cycle(self):
        response = self._request('droplets/{0}/power_cycle'.format(self.id))
        return self._status_update(response, 'power_cycle')

    def shutdown(self):
        response = self._request('droplets/{0}/shutdown'.format(self.id))
        return self._status_update(response, 'shutdown')

    def power_off(self):
        response = self._request('droplets/{0}/power_off'.format(self.id))
        return self._status_update(response, 'power_off')

    def power_on(self):
        response = self._request('droplets/{0}/power_on'.format(self.id))
        return self._status_update(response, 'power_on')

    def password_reset(self):
        return self._request('droplets/{0}/password_reset'.format(self.id))

    def destroy(self):
        response = self._request('droplets/{0}/destroy'.format(self.id))
        return self._status_update(response, 'destroy')

    def resize(self):
        raise NotImplementedError()
