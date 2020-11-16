# Generate dynamic host.yaml for Nornir from Netbox
This code is used to gererate a Nornir host file, it was specifically designed to be used with Cisco devices, but can be changed to be used with any vendor. 
Cisco Modeling Labs (CML2.1) is used to generate a host file. This project is not focused on how to get devices into Netbox, it assumes that the user has some prior knowledge with Netbox.

### Netbox Prerequisites:
*1. Netbox up and running*<br/>
*2. Device roles created*<br/>
*3. Site(s) and devices added to Netbox with IP addresses*<br/>
## Example:
![Netbox Site](/netbox_site.png)<br/>
![Netbox Devices](/netbox_devices.png)<br/>

### CML2 Prerequisites:
*1. Go to https://devnetsandbox.cisco.com/RM/Diagram/Index/685f774a-a5d6-4df5-a324-3774217d0e6b?diagramType=Topology to reserve the lab<br/>
  <i> Note: Cisco account is required, an account can be created for free</i><br/>
*2. Reserve, Cisco Anyconnet VPN credentials will be emailed to you<br/>
  <i> Note: Cisco Anyconnect can be download via the following link: https://developer.cisco.com/site/sandbox/anyconnect/</i><br/>
*3. Once connected, CML2 lab can be accesses via https://10.10.20.161 - credentials are porvided inside the sandbox.<br/>

### Topology used in the example:
![CML2 Topology](/cml_topology.png)
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
NB_TOKEN=123423454565678678123234345
NB_URL=http://example-netbox.com:8085
```

#### Example 
```zsh
~ » git clone https://github.com/Pzharyuk/nb_nornir.git
~ » cd nb_nornir
~/nb_nornir  ‹main› » python3 -m venv venv
~/nb_nornir  ‹main› » source venv/bin/activate
(venv) ~/nb_nornir  ‹main› » pip install -r requirements.txt
(venv) ~/nb_nornir  ‹main› » python gen_hostfile_from_nb.py
Enter site code: devnetsandbox
```
### Example output will be presented using tables and will be color coded using rich python library.<br/>
![Example output](/nb_host_file_output1.png)<br/>
### At this point the /inventory/hosts.yaml file should be populated.<br/>
![Example output2](/nb_host_file_output2.png)<br/>
### Refference Links:
> Netbox GitHub page:</b> https://github.com/netbox-community/netbox.git/<br/>
> Netbox on Docker GitHub page:</b> https://github.com/netbox-community/netbox-docker.git
> CML2 Sandbox: https://devnetsandbox.cisco.com/RM/Diagram/Index/685f774a-a5d6-4df5-a324-3774217d0e6b?diagramType=Topology
> Cisco Anyconnect: https://developer.cisco.com/site/sandbox/anyconnect/
