#!/usr/bin/env python3
""" Nosql """
import pymongo


def list_all(mongo_collection):
    """list all documenti in collection"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())