#!/usr/bin/env python3
""" 8-main """

def list_all(mongo_collection):
    """list all in mongo_collection"""
    return list(mongo_collection.find())
