#!/usr/bin/env python3
""" Function to list all documents in a collection """
def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection"""
    return list(mongo_collection.find()) if mongo_collection else []
