# File: csv_repository.py
# Author: Arbutha Durairaj
# Course: CST8002 – Programming Language Research
# Professor: Stanley Pieda
# Due date: 22 February 2026
#
# Description:
# Persistence layer component responsible for reading and writing
# ShorebirdRecord data to and from CSV files. Implements file input/output
# operations and generates a unique output filename using UUID.
#
# Architecture:
# Part of a closed N-layered architecture.
# The Persistence layer handles file input/output operations and
# interacts with the Model layer for data representation.
#
# References:
# [10] Python Software Foundation, "uuid — UUID objects according to RFC 9562," Python 3 Documentation, 2026. [Online]. 
# Available: https://docs.python.org/3/library/uuid.html. [Accessed 10 February 2026].
#
# [4] Python Software Foundation, "csv — CSV File Reading and Writing," Python 3 Documentation, 2026. [Online]. 
# Available: https://docs.python.org/3/library/csv.html. [Accessed 10 February 2026].
#
#
#
#
"""
Handles CSV file reading and writing.
"""

import csv
import uuid
from src.model.shorebird_record import ShorebirdRecord


# def load_records(file_path, limit=100):
def load_records(file_path, limit=None):
    """
    Reads the shorebird CSV dataset and returns a list of ShorebirdRecord objects.

    Parameters:
        file_path (str): Path to the CSV file
        limit (int): Maximum number of records to load 

    Returns:
        list: A list of ShorebirdRecord objects
    """
    records = []

    try:
        with open(file_path, mode="r", encoding="latin-1") as file:
            reader = csv.DictReader(file)
            next(reader)  # skip French header row

            for i, row in enumerate(reader):
                # if i >= limit:
                if limit is not None and i >= limit:
                    break

                record = ShorebirdRecord(
                    site_id=row["Site identification"],
                    area=row["Area"],
                    visit_date=row["Visit date"],
                    start_time=row["Start time"],
                    species_code=row["Species code"],
                    count=row["Count"]
                )
                records.append(record)

    except FileNotFoundError:
        print("Dataset file not found.")

    return records



def save_records(records):
    """
    Saves a list of ShorebirdRecord objects to a new
    CSV file with a UUID-generated filename.

    Parameters:
        records (list): List of ShorebirdRecord objects.

    Returns:
        str: Generated filename.
    """
    filename = f"shorebird_output_{uuid.uuid4()}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Site identification",
            "Area",
            "Visit date",
            "Start time",
            "Species code",
            "Count"
        ])

        for record in records:
            writer.writerow([
                record.site_id,
                record.area,
                record.visit_date,
                record.start_time,
                record.species_code,
                record.count
            ])

    return filename
