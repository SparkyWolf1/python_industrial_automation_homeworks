import csv
import pathlib
import typing
import logging
import pymongo
import os


CSV_FILE = pathlib.Path(__file__).parent / "data" / "robot_data.csv"
DB_URL = (
    "mongodb://"
    + os.getenv("DB_HOST", "hw-db") + ":27017/")
DB_NAME = os.getenv("DB_NAME", "robot_db")


def read_csv(filename: pathlib.Path) -> typing.Iterator[dict]:
    '''Reads a CSV file and yields each row as a dictionary.

    Args:
        filename (pathlib.Path): Path to the CSV file.

    Yields:
        dict: Row data as a dictionary.
   '''
    try:
        logging.info(f"Reading CSV file: {filename}")
        with open(filename, "r") as file:
            file_reader = csv.DictReader(file, delimiter=";")
            yield from file_reader
    except FileNotFoundError:
        logging.error(f"File {filename} not found.")


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
        client.server_info()
        return client[db_name]
    except pymongo.errors.ConfigurationError as e:
        logging.error(f"Could not connect to MongoDB: {e}")


def create_collection(
        db: pymongo.database.Database,
        collection_name: str
) -> pymongo.collection.Collection:
    '''Creates a collection in the database.
    Args:
        db (pymongo.database.Database): Database instance.
        collection_name (str): Name of the collection to create.

    Returns:
        pymongo.collection.Collection: Created collection instance.
    '''
    try:
        collection = db[collection_name]
        return collection
    except pymongo.errors.PyMongoError as e:
        logging.error(f"Could not create collection: {e}")


def insert_data(
        collection: pymongo.collection.Collection,
        data: typing.List[dict]
) -> None:
    '''Inserts data into the collection.

    Args:
        collection (pymongo.collection.Collection): MongoDB collection.
        data (list of dict): Data to insert.

    Returns:
        None
    '''
    try:
        collection.insert_one(data)
        logging.info("Data inserted successfully.")
    except pymongo.errors.PyMongoError as error:
        logging.error(f"Could not insert data: {error}")


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    database = connect_to_db(DB_URL, DB_NAME)
    logging.info("Connecting to database...")
    if database is None:
        logging.error("Database connection failed.")
        return
    collection = create_collection(database, "robot_data")
    if collection is None:
        logging.error("Collection creation failed.")
        return
    data = list(read_csv(CSV_FILE))
    logging.info(f"Read {len(data)} rows from CSV.")
    for row in data:
        insert_data(collection, row)
    logging.info("Data insertion completed.")


if __name__ == '__main__':
    main()
