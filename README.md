## Gulper

Provides interface to [DigitalOcean](https://www.digitalocean.com).

### Usage

Get all droplets:

```python
import gulper
client = gulper.client(client_id='id', api_key='key')
droplets = client.get_all_droplets()
for droplet in droplets:
    print droplet.name, droplet.status
```

Each droplet object can manipulate it's actual representation.
Rebooting all droplets:

```python
import gulper
droplets = gulper.client(client_id='id', api_key='key').get_all_droplets()
for droplet in droplets:
    droplet.reboot()
```

### Supported droplet methods

- **update**: update droplet status
- **reboot**: reboot droplet
- **power_cycle**: power cycle droplet
- **shutdown**: shutdown droplet
- **power_off**: power off droplet
- **power_on**: power on droplet
- **password\_reset**: reset droplet root password
- **destroy**: destroy droplet
