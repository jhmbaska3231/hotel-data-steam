from pymongo import MongoClient

def main():

    # Connect to MongoDB (Local)
    client = MongoClient("mongodb://localhost:27017")

    # OR Connect to MongoDB Atlas (Replace the URI with your Atlas URI)
    # client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority")

    # Create a database
    db = client["hotel_booking_db"]

    # Create a collection (table equivalent)
    bookings = db["bookings"]

    # Insert a sample document
    sample_booking = {
        "hotel_name": "Marina Bay Sands",
        "room_type": "Deluxe",
        "price": 350,
        "availability": True,
        "check_in_date": "2024-01-01",
        "check_out_date": "2024-01-05"
    }

    # Insert the document into the collection
    booking_id = bookings.insert_one(sample_booking).inserted_id

    print(f"Inserted booking with ID: {booking_id}")

if __name__ == '__main__':
    main()