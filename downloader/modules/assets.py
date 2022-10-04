"""
Assets Module
~~~~~~~~~~~~~

(...)
"""

import modules.catalogs as catalogs
import requests
import plistlib


class UserAgent:
    # Client used to connect to the Software CDN
    osinstall = {"User-Agent":"osinstallersetupplaind (unknown version) CFNetwork/720.5.7 Darwin/14.5.0 (x86_64)"}
    # Client used to connect to the Software Distribution service
    swupdate = {"User-Agent":"Software%20Update (unknown version) CFNetwork/807.0.1 Darwin/16.0.0 (x86_64)"}


class Catalog:
    @staticmethod
    def get_catalog(url: str):
        data = requests.get(url, headers = UserAgent.swupdate).text.encode('UTF-8')
        root = plistlib.loads(data)