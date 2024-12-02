from pymongo import MongoClient

# Create a database connection object using pymongo
DB_NAME = "cs4250_project"
DB_HOST = "localhost"
DB_PORT = 27017
try:
    client = MongoClient(host=DB_HOST, port=DB_PORT)
    db = client[DB_NAME]
    vocabulary_collection = db['vocabulary']
    documents_collection = db['documents']
    inverted_index_collection = db['invertedIndex']
    vectorizer_collection = db['vectorizer']
except:
    print("Database not connected successfully")