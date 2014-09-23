#!/bin/bash

#sudo apt-get --yes update
#sudo apt-get install --yes git
#sudo apt-get install --yes python-pip
#sudo apt-get install --yes python-dev
#sudo pip install tornado

mkdir -p ~/work
cd work
if [ -f mypythonex ] ; then
    git clone https://github.com/ekeydar/mypthonex.git
    cd mypthonex
else
    cd mypthonex
    git pull
fi







