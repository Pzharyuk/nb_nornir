# Generate dynamic host.yaml for Nornir from Netbox - Draft
This code is used to gererate a Nornir host file, it was specifically designed to be used with Cisco devices, but can be changed to be used with any vendor.

## Instructions
### Netbox Prerequisites:
<i>1) Netbox up and running</i><br/>
<i>2) Device roles created</i><br/>
<i>3) Site(s) and devices added to Netbox with IP addresses</i>

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
~/nb_nornir  ‹main› » 
tree my-first-project/
my-first-project/
├── LICENSE
├── NOTICE
└── README.md

0 directories, 3 files
use-cases$
```

### Manual Repo Creation

If you are only creating one use case, this process is probably easier. 

1. Create a new repository.
2. Copy all the files inside `manual-sample-repo` into your new repository. 
3. Update the [README](./README.md), replacing the contents below as described in text within each section of the README. Feel free to combine or omit sections where appropriate. 
4. Update the [LICENSE](./LICENSE), replacing the file with the license selected for your code. See the *Licensing info* section of this README for more info. 
5. Delete these instructions and everything up to the _Project Title_ from the README.
6. Write some great software and [submit](https://developer.cisco.com/codeexchange/github/submit) it to Code Exchange and/or Automation Exchange.

### Refference Links:
> Netbox GitHub page:</b> https://github.com/netbox-community/netbox.git/<br/>
> Netbox on Docker GitHub page:</b> https://github.com/netbox-community/netbox-docker.git
