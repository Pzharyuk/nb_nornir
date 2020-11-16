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

# EMPTY LISTS TO BE USED LATER IN THE CODE #
name = []
ip = []
role = []
dev = []

# MAKE A REQUEST TO NETBOX AND GET DEVICES FOR A SPECIFIC SITE #
try:
    devices = nb.dcim.devices.filter(
        site=input("Enter site code: "), 
        has_primary_ip=True
    )
except pynetbox.core.query.RequestError as e:
    console.print("[bold red]{}[/bold red]".format(e.error))

# COLLECT AND ADD DEVICE INFORMATION FROM NETBOX TO EMPTY LIST AND REMOVE THE CIDR FROM THE IP ADDRESS #
for device in devices:
    name.append(device.name)
    ip.append(device.primary_ip.address[:-3])
    role.append(device.device_role.slug)

# CREATE AND APPEND DEVICE DICTIONARY TO DEV = [] LIST #
for device in devices:
    dev.append(
        dict(
        name = device.name,
        ip = device.primary_ip.address[:-3],
        role = device.device_role.slug,
    )
)

# LOOKUP HOSTS.J2 TEMPLATE TO RENDER HOSTS.YAML FILE #
loader = jinja2.FileSystemLoader(searchpath="./templates")
jenv = jinja2.Environment(loader=loader)
template = jenv.get_template('hosts.j2')
hosts_out = template.render(data=dev)

# LOOP OVER NETBOX DEVICES AND ADD DEVICE INFORMATION TO HOSTS.YAML FILE #
console.print("[bold #f58142]Rendering Host File:[/bold #f58142]")
for r in dev:
    # Building device specific templates
    with open("./inventory/hosts.yaml", "w") as f:
        f.write(hosts_out)

# JUST FOR FUN, OUTPUT THE DEVICES TO A TABLE USING RICH LIBRARY #
table = Table(show_header=True, header_style="bold #4248f5")
table.add_column("Device", style="bold green")
table.add_column("IP", justify="right", style="blue")
table.add_column("Role", justify="right", style="yellow")
for (a,b,c) in itertools.zip_longest(name,ip,role):
    table.add_row(a,b,c)
console.print(table)
console.print("""[bold #f58142]host.yaml file has succesfully been created :thumbs_up:[/bold #f58142]""")
