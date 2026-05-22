# File: sqlite_repository.py
# Author: Arbutha Durairaj
# Course: CST8002 – Programming Language Research
# Professor: Stanley Pieda
# Term: Winter 2026
# Due date: 12 April 2026
#
# Description:
# Persistence layer component responsible for database connectivity
# using SQLite. Provides CRUD operations and supports dynamic
# multi-column sorting using SQL ORDER BY queries as part of the
# advanced enhancement implemented in Practical Project Part 4.
#
# Architecture:
# Part of a closed N-layered architecture.
# The Persistence layer handles database interactions and returns
# model objects to the Business layer.
#
# References:
# [1] Python Software Foundation, "sqlite3 — DB-API 2.0 interface for SQLite databases,"
# Python 3 Documentation, 2026. [Online].
# Available: https://docs.python.org/3/library/sqlite3.html
# 
# [2] SQLite Consortium, "SELECT," sqlite.org, 2025. [Online]. 
# Available: https://www.sqlite.org/lang_select.html. [Accessed 27 March 2026].
# 
# [3] GeeksforGeeks, "SQL Multiple Column Ordering," geeksforgeeks.org, 23 July 2025. [Online]. 
# Available: https://www.geeksforgeeks.org/sql/sql-multiple-column-ordering/. [Accessed 27 March 2026].
#
# [4] SQLPey, "SQL Multiple Column Sorting Techniques," sqlpey.com, n.d.. [Online]. 
# Available: https://sqlpey.com/sql/sql-multiple-column-sorting-techniques/. [Accessed 27 March 2026].
# 
# [5] TutorialsTeacher, "ORDER BY Clause - SQL Server," tutorialsteacher.com, n.d. [Online].
# Available: https://www.tutorialsteacher.com/sqlserver/orderby. [Accessed 27 March 2026].

import sqlite3
from src.model.shorebird_record import ShorebirdRecord
from src.persistence.csv_repository import load_records

DB_NAME = "shorebirds.db"

def get_connection():
    """
    Creates and returns a database connection.
    """
    return sqlite3.connect(DB_NAME)

def create_table():
    """
    Creates the shorebirds table if it does not already exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS shorebirds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        "Site identification" TEXT,
        "Area" TEXT,
        "Visit date" TEXT,
        "Start time" TEXT,
        "Species code" TEXT,
        "Count" INTEGER
    )
    """)

    conn.commit()
    conn.close()



def populate_from_csv(dataset_path):
    """
    Populates the database table with records from the CSV dataset.
    """

    # records = load_records(dataset_path, limit=100)
    records = load_records(dataset_path)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM shorebirds")

    for record in records:
        cursor.execute("""
        INSERT INTO shorebirds
        ("Site identification","Area","Visit date","Start time","Species code","Count")
        VALUES (?,?,?,?,?,?)
        """, (
            record.site_id,
            record.area,
            record.visit_date,
            record.start_time,
            record.species_code,
            record.count
        ))

    conn.commit()
    conn.close()

def load_records_db():
    """
    Retrieves all shorebird records from the database.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
    "Site identification",
    "Area",
    "Visit date",
    "Start time",
    "Species code",
    "Count"
    FROM shorebirds
    ORDER BY id               
    
    """)

    rows = cursor.fetchall()
    conn.close()

    records = []

    for row in rows:
        record = ShorebirdRecord(
            row[0], # site_id
            row[1], # area
            row[2], # visit_date
            row[3], # start_time
            row[4], # species_code
            row[5]  # count

        )
        records.append(record)

    return records

def insert_record(record):
    """
    Inserts a new record into the database.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO shorebirds
    ("Site identification", "Area", "Visit date", "Start time", "Species code", "Count")
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        record.site_id,
        record.area,
        record.visit_date,
        record.start_time,
        record.species_code,
        record.count
    ))

    conn.commit()
    conn.close()

    
def update_record_db(index, record):
    """
    Updates a record in the database using its row position.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # Find actual database ID using index
    cursor.execute(
        "SELECT id FROM shorebirds LIMIT 1 OFFSET ?",
        (index,)
    )

    result = cursor.fetchone()

    if result:
        record_id = result[0]

        cursor.execute("""
        UPDATE shorebirds
        SET
            "Site identification"=?,
            "Area"=?,
            "Visit date"=?,
            "Start time"=?,
            "Species code"=?,
            "Count"=?
        WHERE id=?
        """, (
            record.site_id,
            record.area,
            record.visit_date,
            record.start_time,
            record.species_code,
            record.count,
            record_id
        ))

        conn.commit()

    conn.close()

def delete_record_db(index):
    """
    Deletes a record from the database using its displayed index position.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # Convert displayed index to actual database id
    cursor.execute(
        "SELECT id FROM shorebirds LIMIT 1 OFFSET ?",
        (index,)
    )

    result = cursor.fetchone()

    if result:
        record_id = result[0]

        cursor.execute(
            "DELETE FROM shorebirds WHERE id=?",
            (record_id,)
        )

        conn.commit()

    conn.close()


def sort_records_db(column1, column2, order):
    """
    Retrieves sorted shorebird records using two selected columns.
    """

    conn = get_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT
        "Site identification",
        "Area",
        "Visit date",
        "Start time",
        "Species code",
        "Count"
    FROM shorebirds
    ORDER BY "{column1}" {order},
             "{column2}" {order}
    """

    cursor.execute(query)

    rows = cursor.fetchall()
    conn.close()

    records = []

    for row in rows:
        record = ShorebirdRecord(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5]
        )
        records.append(record)

    return records