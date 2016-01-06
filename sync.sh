#!/bin/bash

MACHINE="machine-name"
URL="https://firebase-app-name.firebaseio.com/$MACHINE/global_ip.json"
USER="username"
echo "requesting $MACHINE ip from firebase"
IP=$(eval "curl $URL")
echo "$MACHINE ip: $IP"
tput setaf 1;tput smul;
echo "starting sync...password + yubikey OTP required"
tput setaf 7;tput rmul;
eval "rsync -ahv prodx/* $USER@$IP:/opt/prodx"
tput setaf 2;
echo "Done";
tput setaf 7;

