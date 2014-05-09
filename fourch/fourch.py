# -*- coding: utf-8 -*-
from ._version import __version__

urls = {
    "api": "lupchan.org",
    "boards": "lupchan.org",
    "images": "lupchan.org",
    "thumbs": "lupchan.org",

    # These are tacked to the end of the api url after formatting.
    "api_board": "/{board}/{page}.json",
    "api_thread": "/{board}/res/{thread}.json",
    "api_threads": "/{board}/threads.json",
    "api_catalog": "/{board}/catalog.json"  #not sure if this works, I'll just leave it
}


class struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
