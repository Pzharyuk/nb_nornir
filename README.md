# Generate dynamic host.yaml for Nornir from Netbox - Draft
This code is used to gererate a Nornir host file, it was specifically designed to be used with Cisco devices, but can be changed to be used with any vendor.

## Instructions
### Netbox Prerequisites:
<i>1) Netbox up and running</i><br/>
<i>2) Device roles created</i><br/>
<i>3) Site(s) and devices added to Netbox with IP addresses</i>
You have two options, if you have familiarity with Python, use the cookiecutter steps. Otherwise you can manually create a copy of this repo template. 


### Cookiecutter Automated Repo Creation

This process uses [cookiecutter](https://github.com/audreyr/cookiecutter) to auto-generate the files for you. This is helpful if you create multiple use cases. 

> Note: This template assumes the BSD 3-Clause License, you can change it be other licenses afterwards if that is not what you want.


1. Issue this command `pip install cookiecutter` to get ready to use the template.
2. Use this command and answer the questions: `cookiecutter https://github.com/CiscoDevNet/code-exchange-repo-template`
3. Update the [README](./README.md), replacing the contents below as described in text within each section of the README. Feel free to combine or omit sections where appropriate. 
4. Update the [LICENSE](./LICENSE), replacing the file with the license selected for your code. See the *Licensing info* section of this README for more info. 
5. Delete these instructions and everything up to the _Project Title_ from the README.
6. Write some great software and [submit](https://developer.cisco.com/codeexchange/github/submit) it to Code Exchange and/or Automation Exchange.



#### Example 
```bash
use-cases$ cookiecutter https://github.com/CiscoDevNet/code-exchange-repo-template
project_name [my-awesome-devnet-code-exchange-project]: my-first-project
project_description [baseline DevNet Code Exchange Project]: New Things to come!
author_name [Your Name Here]: User Name
author_email [youremail@domain.com]: user@cisco.com
use-cases$ tree
.DS_Store                          devnet-code-exchange/              my-first-project/
cookiecutter-devnet-code-exchange/ 
use-cases$ tree my-first-project/
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
