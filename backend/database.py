from psycopg2 import connect
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection


def get_db_connection() -> connection:
    ...


def create_habit(name: str, description: str, target_frequency: int, frequency_unit: str) -> dict:
    query = sql.SQL("""
        INSERT INTO habit (name, description, target_frequency, frequency_unit)
        VALUES (%s, %s, %s, %s)
        RETURNING habit_id, name, description, target_frequency, frequency_unit;
    """)

    with get_db_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                query,
                (name, description, target_frequency, frequency_unit)
            )
            habit = cursor.fetchone()
            conn.commit()

    return habit
