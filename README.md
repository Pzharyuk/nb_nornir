# Generate dynamic host.yaml for Nornir from Netbox
This code is used to gererate a Nornir host file, it was specifically designed to be used with Cisco devices, but can be changed to be used with any vendor. 
Cisco Modeling Labs (CML2.1) is used to generate a host file. 

### Netbox Prerequisites:
*1. Netbox up and running*<br/>
*2. Device roles created*<br/>
*3. Site(s) and devices added to Netbox with IP addresses*

### CML2 Prerequisites:
*1. Go to https://devnetsandbox.cisco.com/RM/Diagram/Index/685f774a-a5d6-4df5-a324-3774217d0e6b?diagramType=Topology to reserve the lab
> Note: Cisco account is required, an accounte can be created for free
*2. Reserve, Cisco Anyconnet VPN credentials will be emailed to you
> Cisco Anyconnect can be download via the following link: https://developer.cisco.com/site/sandbox/anyconnect/

### Topology used in the example:

## Instructions

### Cloning repo and installing requirements via pip

1. Clone this repo `git clone https://github.com/Pzharyuk/nb_nornir.git`
2. cd into `nb_nornir'
3. Create python virtual environment `python3 -m venv venv'
4. Activate virtual environment `source venv/bin/activate`
5. Install required python packages via `pip install -r requirements.txt`

### Using .ENV
This project uses .env file to popopulate environment variables used in the code<br/>
1. Populate .env file with Netbox url and token
```
PRD_TOKEN=123423454565678678123234345
PRD_URL=https://example-netbox.com
DEV_TOKEN=123423454565678678123234345
DEV_URL=http://example-netbox.com:8085
```

#### Example 
```zsh
~ » git clone https://github.com/Pzharyuk/nb_nornir.git
~ » cd nb_nornir
~/nb_nornir  ‹main› » python3 -m venv venv
~/nb_nornir  ‹main› » source venv/bin/activate
(venv) ~/nb_nornir  ‹main› » pip install -r requirements.txt
(venv) ~/nb_nornir  ‹main› » python gen_hostfile_from_nb.py
Enter site code: cml2-example-site 
```
# Example output will be presented using tables and will be color coded using rich python library.<br/>
![Example output](/EkL96qxUYAYv1wt.png)
<br/>
# At this point the /inventory/hosts.yaml file should be populated.<br/>
![Example output2](/EkL6Go5UwAAn7kk.jpeg)

### Refference Links:
> Netbox GitHub page:</b> https://github.com/netbox-community/netbox.git/<br/>
> Netbox on Docker GitHub page:</b> https://github.com/netbox-community/netbox-docker.git
