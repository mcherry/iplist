# IPList
A simple python script that use the IPNetwork module to display and optionally ping all IP addresses within a CIDR netrange. An optional delimiter to separate IP addresses can be specified. This script can be useful for generating lists of IP adresses that are active in a given netrange.

# Usage
iplist.py [-h] -n NETWORK [-d DELIMITER] [-p] [-q]

# Optional Arguments
| Argument | Input | Description |
| -------- | ----- | ----------- |
| -h, --help |   | Show the build in help message and exit |
| -n, --network | NETWORK | Network range to display. Example: 10.100.5.0/24. Any CIDR netrange supported by the IPNetwork module will work. |
| -d, --delimiter | DELIMITER | Delimiter between each IP address. Default is a newline (\n). Delimiter can be multiple characters if necessary |
| -p, --ping |    | Ping each IP and only display hosts that are up. |
| -q, --quiet  |   | Do not display details about the network such as total IP addresses and starting and ending IP addresses. |

# Examples
Display all possible IP addresses in the 10.100.5.0/24 network using a comma to separate them.

`iplist.py -n 10.100.5.0/24 -d ", "`


Display only IP addresses in the 10.100.5.0/24 network that respond to ping and do not display network details.

`iplist.py -n 10.100.5.0/24 -p -q`
