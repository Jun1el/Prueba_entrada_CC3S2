from databases import Database

DATABASE_URL = "postgresql://postgres:postgres@db:5432/trivia_db"

database = Database(DATABASE_URL)
