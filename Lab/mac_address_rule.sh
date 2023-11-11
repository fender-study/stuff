#!/bin/bash

iptables -F INPUT

PERMITTED_MACS="08:01:25:04:61:21 08:00:53:04:65:22"

for MAC in $PERMITTED_MACS
do
  iptables -A FORWARD -m mac --mac-source $MAC -j ACCEPT
  echo "%MAC permitted"
done

iptables -P FORWARD DROP
