#!/bin/bash

if [ "$#" -ne 1 ]
then
   echo 'remote machine IP Please'
   exit 1
fi

HOST=$1
KEYGEN="/usr/bin/ssh-keygen"
SSH="/usr/bin/ssh"

# check ~/.ssh/id_rsa exists
#otherwise create ssh-keygen -t rsa
echo "Checking id_rsa.pub file"
if [ ! -f "$HOME/.ssh/id_rsa.pub" ]
then
    echo "Generating rsa public key"
    $KEYGEN -t rsa 
else
    echo "$HOME/.ssh/id_rsa.pub already exists"
fi

#check remote .ssh dir exists
#otherwise create .ssh in remote machine
$SSH $HOST 'mkdir -p $HOME/.ssh'

#upload public key to remote server
echo 'uploading public key...'
cat .ssh/id_rsa.pub | ssh $USER@$HOST 'cat >> .ssh/authorized_keys' 

echo 'setting up right permission'
# set permissions on .ssh and authorized_keys
$SSH $USER@$HOST "chmod 700 .ssh; chmod 640 .ssh/authorized_keys"
echo 'Done'
