#!/bin/bash

# Drops all incoming traffic to port 22 (SSH)
iptables -A INPUT -p tcp  --dport 22 -j DROP

# Drops outgoing http and https traffic
iptables -A OUTPUT -p tcp --dport 80 -j DROP
iptables -A OUTPUT -p tcp --dport 443 -j DROP