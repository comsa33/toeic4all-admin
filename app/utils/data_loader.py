from typing import List, Union

from app.utils.db import db, part5_collection, part6_collection, part7_collection
from app.utils.logger import logger
from app.utils.models.part5_question import Part5Question
from app.utils.models.part6_question import Part6Set
from app.utils.models.part7_question import Part7Set

# 컬렉션 매핑
COLLECTION_MAPPING = {
    "part5_questions": part5_collection,
    "part6_sets": part6_collection,
    "part7_sets": part7_collection,
}


async def insert_questions(
    sets: Union[List[Part5Question], List[Part6Set], List[Part7Set]],
    collection_name: str,
):
    """
    Insert a list of TOEIC questions into the corresponding MongoDB collection.
    """
    try:
        collection = COLLECTION_MAPPING.get(collection_name, db[collection_name])
        # Insert the questions into the collection
        docs = [s.model_dump(mode="json") for s in sets]
        result = await collection.insert_many(docs)
        logger.info(
            f"Inserted {len(result.inserted_ids)} documents into the {collection_name} collection."
        )
        return result.inserted_ids
    except Exception as e:
        logger.error(f"An error occurred during database insertion: {e}")
        return None
