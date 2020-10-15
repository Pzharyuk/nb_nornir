import pynetbox
from nb_helper import nb_prd
import yaml
import jinja2
from rich.console import Console
from rich.table import Table
import itertools
import sys

console = Console()
sys.tracebacklimit = 0

#Empty lists to be used later in the code #
name = []
ip = []
role = []
dev = []

# Make a request to Netbox and get devices for a specific site #
try:
    devices = nb_prd.dcim.devices.filter(
        site=input("Enter site code: "), 
        has_primary_ip=True, 
        platform='ios',
    )
except pynetbox.core.query.RequestError as e:
    console.print("[bold red]{}[/bold red]".format(e.error))

# Create 3 different lists for device name, ip and role, append to empty lists created above #
for device in devices:
    name.append(device.name)
    ip.append(device.primary_ip.address[:-3])
    role.append(device.device_role.slug)

# Append device dictionary to dev = [] list
for device in devices:
    dev.append(
        dict(
        name = device.name,
        ip = device.primary_ip.address[:-3],
        role = device.device_role.slug,
    )
)

# Lookup hosts.j2 template to render hosts.yaml file #
loader = jinja2.FileSystemLoader(searchpath="./templates")
jenv = jinja2.Environment(loader=loader)
template = jenv.get_template('hosts.j2')
hosts_out = template.render(data=dev)

# Loop over Netbox devices and add devices to hosts.yaml file #
console.print("[bold #f58142]Rendering Host File:[/bold #f58142]")
for r in dev:
    # Building device specific templates
    with open("./inventory/hosts.yaml", "w") as f:
        f.write(hosts_out)

# Just for fun, output the devices to a table using rich module #
table = Table(show_header=True, header_style="bold #4248f5")
table.add_column("Device", style="bold green")
table.add_column("IP", justify="right", style="blue")
table.add_column("Role", justify="right", style="yellow")
for (a,b,c) in itertools.zip_longest(name,ip,role):
    table.add_row(a,b,c)
console.print(table)
console.print("""[bold #f58142]host.yaml file has succesfully been created\n
                please check your invenory (./inventory) directory! :thumbs_up:[/bold #f58142]""")