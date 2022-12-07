"""
Functions Module
~~~~~~~~~~~~~

(...)
"""

import requests
import plistlib
import click
import errno
import os


class UserAgent:
    # Client used to connect to the Software CDN
    osinstall = {"User-Agent":"osinstallersetupplaind (unknown version) CFNetwork/720.5.7 Darwin/14.5.0 (x86_64)"}
    # Client used to connect to the Software Distribution service
    swupdate = {"User-Agent":"Software%20Update (unknown version) CFNetwork/807.0.1 Darwin/16.0.0 (x86_64)"}


def download_file(url, size, path):
    label = url.split('/')[-1]
    filename = os.path.join(path, label)
    # Set to stream mode for large files
    remote = requests.get(url, stream = True, headers = UserAgent.osinstall)
    
    with open(filename, 'wb') as f:
        with click.progressbar(remote.iter_content(1024), length = size/1024, label = "Fetching {} ...".format(filename)) as stream:
            for data in stream:
                f.write(data)
    
    return filename


def check_directory(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def fetch_plist(url):
    plist_raw = requests.get(url, headers = UserAgent.swupdate)
    plist_data = plist_raw.text.encode("UTF-8")
    return plist_data


def parse_plist(catalog_data):
    root = plistlib.loads(catalog_data)
    return root
