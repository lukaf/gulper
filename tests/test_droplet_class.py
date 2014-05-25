from __future__ import print_function
import unittest
import mock

from gulper.droplet import Droplet


class DropletTest(unittest.TestCase):
    def setUp(self):
        self.response = {'status': 'OK', 'droplet': {'created_at': 'future'}}
        self.credentials = {
            'client_id': 'id',
            'api_key': 'key'
        }
        Droplet._request = mock.Mock(return_value=self.response)
        self.droplet = Droplet(
            id=10,
            name='droplet_name',
            image_id='image_id',
            size_id='size_id',
            region_id='region_id',
            backups_active=False,
            ip_address='192.168.2.1',
            private_ip_address='192.168.1.1',
            locked=False,
            status='testing',
            created_at='now',
            credentials=self.credentials
        )

    def tearDown(self):
        self.gulper = None
        self.credentials = None
        self.droplet = None

    def test_droplet(self):
        self.assertEqual(self.droplet.id, 10)
        self.assertEqual(self.droplet.name, 'droplet_name')
        self.assertEqual(self.droplet.image_id, 'image_id')
        self.assertEqual(self.droplet.size_id, 'size_id')
        self.assertEqual(self.droplet.region_id, 'region_id')
        self.assertFalse(self.droplet.backups_active)
        self.assertEqual(self.droplet.ip_address, '192.168.2.1')
        self.assertEqual(self.droplet.private_ip_address, '192.168.1.1')
        self.assertFalse(self.droplet.locked)
        self.assertEqual(self.droplet.status, 'testing')
        self.assertEqual(self.droplet.created_at, 'now')
        self.assertEqual(self.droplet.credentials, self.credentials)

    def test_update_method(self):
        self.droplet.update()
        Droplet._request.assert_called_once_with('droplet/{0}'.format(self.droplet.id))
        self.assertEqual(self.droplet.created_at, 'future')

    def test_reboot_method(self):
        self.droplet.reboot()
        Droplet._request.assert_called_once_with('droplet/{0}/reboot'.format(self.droplet.id))
        self.assertEqual(self.droplet.status, 'reboot')

    def test_power_cycle_method(self):
        self.droplet.power_cycle()
        Droplet._request.assert_called_once_with('droplet/{0}/power_cycle'.format(self.droplet.id))
        self.assertEqual(self.droplet.status, 'power_cycle')

    def test_shutdown_method(self):
        self.droplet.shutdown()
        Droplet._request.assert_called_once_with('droplet/{0}/shutdown'.format(self.droplet.id))
        self.assertEqual(self.droplet.status, 'shutdown')

    def test_power_off_method(self):
        self.droplet.power_off()
        Droplet._request.assert_called_once_with('droplet/{0}/power_off'.format(self.droplet.id))
        self.assertEqual(self.droplet.status, 'power_off')

    def test_power_on_method(self):
        self.droplet.power_on()
        Droplet._request.assert_called_with('droplet/{0}/power_on'.format(self.droplet.id))
        self.assertEqual(self.droplet.status, 'power_on')

    def test_password_reset_method(self):
        self.droplet.password_reset()
        Droplet._request.assert_called_once_with('droplet/{0}/password_reset'.format(self.droplet.id))

if __name__ == '__main__':
    unittest.main()
