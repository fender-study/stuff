#!/bin/bash

read -p "Enter the ip address to block: " ip
iptables -I INPUT -s $ip -j DROP

echo "The packets from $ip will be dropped."