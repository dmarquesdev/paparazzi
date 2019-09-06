# Paparazzi

Take screenshots from Web Servers detected by Nessus through a .nessus file

Usage: ./paparazzi.py <nessus file>

TODO:
- Set parameters (output directory, input file, resolution, etc) through argparse
- Detect OS, Chrome version and download appropriate chromedriver
- Handle connection problems
- Work not only with IPs, but with domains and FQDN as well
- Build a HTML report using bootstrap

## Installation
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements
*** Then search the appropriate version of chromedriver for your Chrome version and copy to the root directory of the script ***
```