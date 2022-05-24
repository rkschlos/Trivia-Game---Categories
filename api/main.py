import psycopg
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/api/categories")
# def list_categories():
#     with psycopg.connect("dbname=trivia-game user=trivia-game") as conn:
#         with conn.cursor() as cur:
#             cur.execute("SELECT * FROM categories")
#             records = cur.fetchall()
#             results = []
#             for record in records:
#                 results.append(record)
#             return results