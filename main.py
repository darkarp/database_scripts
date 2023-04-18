from database import Database
from queries import Queries
from config import DB_CONFIG

if __name__ == "__main__":
    # Initialize the database connection and queries
    db = Database(DB_CONFIG)
    queries = Queries(db)

    # Fetch and print data dictionary
    data_dict = queries.generate_data_dict()
    # print(data_dict)

    # Close the connection when finished
    db.close()
