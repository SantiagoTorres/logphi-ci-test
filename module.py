#!/usr/bin/env python
import glob
import hashlib
import os
from base64 import b64encode

def get_filenames():

    filenames = glob.glob("*")

    filenames_no_dir = []

    for filename in filenames:
        if os.path.isdir(filename):
            continue

        filenames_no_dir.append(filename)

    return filenames_no_dir

def check_sums(filenames):
    
    checksums = []
    for filename in filenames:
        with open(filename) as fp:
            data = fp.read()
        
        checksum = hashlib.sha256(data).digest()
        checksum = b64encode(checksum)
        checksums.append((filename, checksum))

    return checksums



if __name__ == '__main__':

    filenames = get_filenames() 
    checksums = check_sums(filenames)
    for checksum in checksums:
        print("{}: {}".format(checksum[0], checksum[1]))
