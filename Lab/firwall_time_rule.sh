#!/bin/bash

iptables -F

iptables -A INPUT -p tcp --dport 22 -m time --timestart 10:00 --timestop 16:00 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j DROP
