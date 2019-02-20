#!/bin/bash

set -e

pip install --trusted-host pypi.python.org -r requirements.txt

#instalar hmmer
cd /tmp
wget -nv http://eddylab.org/software/hmmer/hmmer-3.2.1.tar.gz
tar xf hmmer-3.2.1.tar.gz
cd hmmer-3.2.1 
./configure
make
#make check
make install

# cleanup
rm -rf /tmp/hmmer* ~/.cache
