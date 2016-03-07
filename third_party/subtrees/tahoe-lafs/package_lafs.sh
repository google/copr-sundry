#!/bin/bash

set -e


sudo yum update -y

sudo yum install -y \
    @development-tools \
    fedora-packager

sudo usermod -a -G mock vagrant

rpmdev-setuptree

cd ~/rpmbuild/

sudo yum install -y \
    unzip \
    git \
    gcc-c++ \
    python2-devel \
    libffi \
    python-cffi

rm -rf ./SOURCES/*
rm -rf ./RPMS/*

cp -r /vagrant/allmydata-tahoe-1.10.0/* ./SOURCES/
cp -r /vagrant/allmydata-tahoe-1.10.0.zip ./SOURCES/

#cd SOURCES/ && wget https://tahoe-lafs.org/source/tahoe-lafs/releases/allmydata-tahoe-1.10.0.zip

rpmbuild -ba /vagrant/tahoe-lafs.spec
