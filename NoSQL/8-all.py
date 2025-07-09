#!/usr/bin/env python3
""" 8-main """

def list_all(mongo_collection):
    """list"""
    return list(db.mongo_collection.find())
