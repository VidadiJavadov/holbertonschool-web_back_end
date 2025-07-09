#!/usr/bin/env python3
""" 11-main """

def schools_by_topic(mongo_collection, topic):
    """specific topic"""
    return mongo_collection.find({"topic": topic})
