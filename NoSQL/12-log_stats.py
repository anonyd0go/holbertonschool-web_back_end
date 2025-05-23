#!/usr/bin/env python3
"""
Connects to a MongoDB database and provides statistics
about Nginx logs stored in the database.
"""

from pymongo import MongoClient


def log_stats():
    """
    Connect to MongoDB and display stats about Nginx logs.

    The stats include:
        - Total number of logs.
        - Count of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE).
        - Count of logs for GET requests to the "/status" path.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\t{method}: {count}")

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
