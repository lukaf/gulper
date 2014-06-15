## Gulper

Provides interface to [DigitalOcean](https://www.digitalocean.com).

Requires no third-party libraries.

### Usage

To get started, create a client:
```python
import gulper
client = gulper.client(client_id='id', api_key='key')
```

Credentials are then automatically passed on to subsequent calls
and merged to relevant objects.

Get all droplets:

```python
droplets = client.get_all_droplets()
for droplet in droplets:
    print droplet.name, droplet.status
```

Create a droplet:
```python
droplet = client.create_droplet('mydroplet')
```

Wait until status is active:
```python
while droplet.status != 'active':
    time.sleep(10)
    droplet.update()
```

Destroy droplet:
```python
droplet.destroy()
```

### Droplet methods

- **update**: update droplet status
- **reboot**: reboot droplet
- **power_cycle**: power cycle droplet
- **shutdown**: shutdown droplet
- **power_off**: power off droplet
- **power_on**: power on droplet
- **password\_reset**: reset droplet root password
- **destroy**: destroy droplet
