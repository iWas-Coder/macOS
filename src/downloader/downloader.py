#!/usr/bin/env python3

import catalogs
import fetch


def main():
    # Get the catalog data
    remote = fetch.Remote(catalogs.default)
    catalog = remote.getcatalog()
    # Get the latest product from the catalog
    product = fetch.Product(catalog, remote.getosinstall()[0])
    product.fetchpackages("../../build", keyword = "BaseSystem")


if __name__ == "__main__":
    main()
