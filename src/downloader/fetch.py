"""
Fetch Module
~~~~~~~~~~~~~

(...)
"""

import funcs
import catalogs


class Product:
    def __init__(self, catalog, product_id):
        root = funcs.parse_plist(catalog)
        products = root["Products"]
        self.date = root["IndexDate"]
        self.product = products[product_id]
    
    
    def fetchpackages(self, path, keyword = None):
        funcs.check_directory(path)
        packages = self.product["Packages"]
        if keyword:
            for item in packages:
                if keyword in item.get("URL"):
                    funcs.download_file(item.get("URL"), item.get("Size"), path)
        else:
            for item in packages:
                funcs.download_file(item.get("URL"), item.get("Size"), path)


class Remote:
    def __init__(self, version):
        self.version = version
        self.catalog_url = catalogs.catalog_list.get(version)
        self.catalog_data = ""
    
    
    def getcatalog(self):
        self.catalog_data = funcs.fetch_plist(self.catalog_url)
        return self.catalog_data
    
    
    def getosinstall(self):
        # Load catalogs
        root = funcs.parse_plist(self.catalog_data)
        
        # Iterate to find valid OSInstall packages
        ospackages = []
        products = root['Products']
        for product in products:
            if products.get(product, {})                              \
                       .get("ExtendedMetaInfo", {})                   \
                       .get("InstallAssistantPackageIdentifiers", {}) \
                       .get("OSInstall", {})                          \
            == "com.apple.mpkg.OSInstall":
                ospackages.append(product)
        
        # Iterate for an specific version
        candidates = []
        for product in ospackages:
            meta_url = products.get(product, {}).get("ServerMetadataURL", {})
            if self.version in funcs.parse_plist(funcs.fetch_plist(meta_url)).get("CFBundleShortVersionString", {}):
                candidates.append(product)
        
        return candidates
