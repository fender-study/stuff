#!/bin/bash

# Set accept policy
iptables -p INPUT ACCEPT
iptables -p OUTPUT ACCEPT
iptables -p FORWARD ACCEPT

# Flush all tables with rules
iptables -t filter -F
iptables -t nat -F
iptables -t mangle -F
iptables -t raw -F

# Delete user-defined chains
iptables -X
