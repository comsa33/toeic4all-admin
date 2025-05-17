import os

from dotenv import load_dotenv
from pymongo import AsyncMongoClient

from logger import logger
from models.part5_question import Part5Question

# Load environment variables from .env file
load_dotenv()

uri = os.getenv("MONGODB_URI")
client = AsyncMongoClient(uri)

collection = client["toeic4all"]["part5_questions"]


async def insert_part5_questions(sets: list[Part5Question]):
    """
    Insert a list of Part 5 questions into the MongoDB collection.
    """
    try:
        # Insert the questions into the collection
        docs = [s.model_dump(mode="json") for s in sets]
        result = await collection.insert_many(docs)
        logger.info(
            f"Inserted {len(result.inserted_ids)} documents into the collection."
        )
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        await client.close()
