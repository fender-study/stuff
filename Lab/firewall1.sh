#!/bin/bash

iptables -F
# Drops all incoming traffic to port 22 (SSH)
iptables -A INPUT -p tcp  --dport 22 -j DROP

# Drops outgoing http and https traffic
iptables -A OUTPUT -p tcp --dport 80 -j DROP
iptables -A OUTPUT -p tcp --dport 443 -j DROP

iptables - t nat -A POSTROUTING -s 10.0.0.0/8 -o enp0s3 -j SNAT --too-source 80.0.0.1
