#!/usr/bin/env python3
""" function that lists all documents in a collection """


def list_all(mongo_collection):
    """ returns a list of all docs in collection """
    return list(mongo_collection.find())