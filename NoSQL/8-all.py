#!/usr/bin/env python3
""" Nosql """
from pymongo import MongoClient


def list_all(mongo_collection):
    """list all documenti in collection"""
    return list(mongo_collection.find())
