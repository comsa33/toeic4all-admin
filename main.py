import asyncio

from data_loader import insert_part5_questions
from part5_generation import generate_part5_questions

from logger import logger


async def main(num: int, diff: str, cat: str, sub: str):
    """
    Main function to generate and insert Part 5 questions.
    """
    part5_sets = generate_part5_questions(num, diff, cat, sub)
    logger.info(f"Generated Part 5 sets: {part5_sets}")
    await insert_part5_questions(part5_sets)


if __name__ == "__main__":
    # ---- 사용자 파라미터 ------------------------------------
    NUM = 3
    DIFF = "Medium"
    CAT = "문법"
    SUB = "시제"
    # ---------------------------------------------------------
    # Run the main function
    asyncio.run(main(NUM, DIFF, CAT, SUB))
