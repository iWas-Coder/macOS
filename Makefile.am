bin_PROGRAMS = dmg2img

dmg2img_SOURCES = \
    src/dmg2img/dmg2img.c \
    src/dmg2img/base64.c \
    src/dmg2img/adc.c

dmg2img_LDADD = \
    -lz \
    -lbz2

python_PYTHON = \
    src/downloader/downloader.py \
    src/downloader/fetch.py \
    src/downloader/funcs.py \
    src/downloader/catalogs.py