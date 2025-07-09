#!/usr/bin/env python3
""" 9-main """

def insert_school(mongo_collection, **kwargs):
    """Inserting new document"""
    result = mongo_collection.insert_one(kwargs)
    return(result.inserted_id)
