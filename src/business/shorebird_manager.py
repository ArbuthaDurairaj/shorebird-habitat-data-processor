# File: shorebird_manager.py
# Author: Arbutha Durairaj
# Course: CST8002 – Programming Language Research
# Professor: Stanley Pieda
# Term: Winter 2026
# Due date: 12 April 2026
#
# Description:
# Business layer component responsible for managing ShorebirdRecord
# objects in memory. Provides functionality to add, update, delete,
# retrieve, and reload records using SQLite database persistence. 
# Supports coordination of multi-column sorting requests between the
# Presentation and Persistence layers as part of Practical Project Part 4.
#
# Architecture:
# Part of a closed N-layered architecture.
# The Business layer contains application logic and coordinates
# interactions between the Presentation and Persistence layers.
# It also manages domain model objects.
#
# References:
# [7] Python Software Foundation, "Data Structures — Lists," Python 3 Documentation, 2026. [Online].
#  Available: https://docs.python.org/3/tutorial/datastructures.html. [Accessed 10 February 2026].
#
# [1] Python Software Foundation, "sqlite3 — DB-API 2.0 interface for SQLite databases," docs.python.org, 2026. [Online]. 
# Available: https://docs.python.org/3/library/sqlite3.html. [Accessed 27 March 2026].
#
#
"""
Business logic for managing shorebird records.
"""

# from src.persistence.csv_repository import load_records, save_records
from src.model.shorebird_record import ShorebirdRecord
from src.persistence.sqlite_repository import (
    create_table,
    populate_from_csv,
    load_records_db,
    insert_record,
    update_record_db,
    delete_record_db,
    sort_records_db
)

class ShorebirdManager:
    """
    Manages in-memory ShorebirdRecord objects and
    coordinates persistence operations.
    """
    def __init__(self):
         """
        Initializes manager and ensures database table exists.
        """

        # Ensure database table exists
         create_table()
         
        # Database is now primary data source
         self.records = load_records_db()
    
    
    def load_data(self, dataset_path):
         """
        Loads records into the database from the CSV dataset
        and refreshes the in-memory list.
        """

         populate_from_csv(dataset_path)


        # Always reload from DB after population

         self.records = load_records_db()
    
    

    def get_all(self):
        """
        Returns all ShorebirdRecord objects stored in memory.
        """
        return self.records
    
    
    def create_record(self, site_id, area, visit_date,
                      start_time, species_code, count):
        """
    Creates a new ShorebirdRecord and adds it to the record list.
    """
        record = ShorebirdRecord(
            site_id, area, visit_date,
            start_time, species_code, count
        )
        insert_record(record)
        
        # Sync memory with database
        self.records.append(record)
    

    
    def build_record(self, site_id, area, visit_date,
                     start_time, species_code, count):
        """
    Builds and returns a ShorebirdRecord object without
    automatically inserting it into the list.
    """
        return ShorebirdRecord(
            site_id, area, visit_date,
            start_time, species_code, count
        )
    

    def update_record(self, index, new_record):
        """
        Updates a record in the database.
        """

        update_record_db(index, new_record)

        # Sync memory with database
        self.records = load_records_db()
    
 
    def delete_record(self, index):
        """
        Deletes a record from the database.
        """

        delete_record_db(index)

        #  Refresh memory from database
        self.records = load_records_db()
    
    
    def sort_records(self, column1, column2, order):
        """
        Sorts records using two selected dataset columns
        and updates in-memory list from database.
        """

        self.records = sort_records_db(column1, column2, order)
    


   
    
    