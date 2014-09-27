#!/bin/bash


sudo apt-get --yes update
sudo apt-get install --yes git
sudo apt-get install --yes python-pip
sudo apt-get install --yes python-dev
sudo pip install tornado
sudo pip install ipython
mkdir -p ~/work
cd work
git clone https://github.com/ekeydar/mypthonex.git
cat << EOF > ~/.inputrc
"\ep": history-search-backward
"\en": history-search-forward
EOF

cat << EOF >> ~/.bashrc
alias ws='cd /home/ubuntu/work/mypthonex/websocket/server'
EOF






