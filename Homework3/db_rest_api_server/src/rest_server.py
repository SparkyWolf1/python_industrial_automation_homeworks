import flask
import pymongo
import logging
import os

API_HOST = "0.0.0.0"
API_PORT = 7878

DB_URL = (
    "mongodb://"
    + os.getenv("DB_HOST", "hw-db") + ":27017/")
DB_NAME = os.getenv("DB_NAME", "robot_db")

app = flask.Flask(__name__)


def connect_to_db(
        connection_url: str,
        db_name: str
) -> pymongo.database.Database:
    '''Connects to MongoDB and return the database instance.

     Args:
        connection_url (str): MongoDB connection URL.
        db_name (str): Name of the database to connect to.

        Returns:
        pymongo.database.Database: Database instance.
    '''
    try:
        client = pymongo.MongoClient(
            connection_url,
            serverSelectionTimeoutMS=5000
        )
        return client[db_name]
    except pymongo.errors.ConnectionError as error:
        logging.error(f"Could not connect to MongoDB: {error}")


def get_row_by_num(
        collection: pymongo.collection.Collection,
        row_num: int
) -> dict:
    '''Retrieve a document from the collection by row number.

    Args:
        collection (pymongo.collection.Collection): MongoDB collection.
        row_num (int): Row number to retrieve.

    Returns:
        dict: Document corresponding to the row number.
    '''
    try:
        result = collection.find_one({'Num': row_num}, {'_id': 0})
        print(result)
        return result
    except pymongo.errors.PyMongoError as error:
        logging.error(f"Could not retrieve data: {error}")
        return None


def get_all_rows(
        collection: pymongo.collection.Collection
) -> list:
    '''Retrieve all documents from the collection.

    Args:
        collection (pymongo.collection.Collection): MongoDB collection.

    Returns:
        list: List of all documents in the collection.
    '''
    try:
        results = collection.find({}, {'_id': 0})
        return list(results)
    except pymongo.errors.PyMongoError as error:
        logging.error(f"Could not retrieve data: {error}")
        return []


# Define API endpoints
# Base endpoint
@app.route('/')
def hello_world():
    return 'Application is running'


# Status endpoint
@app.route('/status')
def status():
    return flask.jsonify({"status": "OK"}), 200


# Database status endpoint
@app.route('/status/db')
def db_status():
    logging.info("Checking database status...")
    database = connect_to_db(DB_URL, DB_NAME)
    if database is None:
        logging.error("Database connection failed.")
        return flask.jsonify({"status": "DB connection failed"}), 500
    logging.info("Database connection successful.")
    return flask.jsonify(
        {
            "status": "DB connection successful",
            "db_address": DB_URL,
            "db_name": DB_NAME,
            "collections": database.list_collection_names()
            }), 200


# Robot data retrieval endpoint
@app.route('/robot_data/row=<int:row_num>', methods=['GET'])
def get_robot_data(row_num):
    logging.info(f"Fetching data for row number: {row_num}")
    databse = connect_to_db(DB_URL, DB_NAME)
    logging.info("Connecting to database...")
    if databse is None:
        return flask.jsonify({'error': 'Database connection failed'}), 500
    logging.info("Connected to database.")
    collection = databse['robot_db']
    row = get_row_by_num(collection, row_num)
    if row is None:
        return flask.jsonify({'error': 'Data not found'}), 404
    return flask.jsonify(row), 200


@app.route('/robot_data/all', methods=['GET'])
def get_all_robot_data():
    logging.info("Fetching all robot data...")
    database = connect_to_db(DB_URL, DB_NAME)
    logging.info("Connecting to database...")
    if database is None:
        return flask.jsonify({'error': 'Database connection failed'}), 500
    logging.info("Connected to database.")
    collection = database['robot_db']
    rows = get_all_rows(collection)
    return flask.jsonify(rows), 200


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    app.run(host=API_HOST, port=API_PORT, debug=True)


if __name__ == '__main__':
    main()
