
from fastapi import FastAPI
import psycopg

app = FastAPI()


# GET path /api/categories
# id, title, canon
# categories
# /api/categories?<int:page>
# example:   /api/categories?page=17
conn_str = "postgresql://trivia-game:trivia-game@db/trivia-game"

@app.get("/api/categories")
def list_categories(page: int=0):
	#                        username   :password   @ database"
	with psycopg.connect(conn_str) as conn:
		with conn.cursor() as cur:
			cur.execute("""
				SELECT id, title, canon
				FROM categories
				LIMIT 100 OFFSET %s
			""", [page * 100])
			records = cur.fetchall()
			results = []
			#to make it a pretty dictionary
			for record in records:
				# record = [1, ""!"", true]
				results.append({
					"id": record[0],
					"title": record[1],
					"canon": record[2],
				})
			return results


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


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