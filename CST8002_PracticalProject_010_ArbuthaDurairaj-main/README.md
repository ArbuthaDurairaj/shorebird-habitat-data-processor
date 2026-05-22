# Shorebird Habitat Data Processor

A Python-based console application for processing and managing migratory shorebird habitat data using SQLite database persistence, layered software architecture, CRUD operations, and dynamic SQL-based sorting functionality.

----------------------------------------------------------------------

# Project Overview

This project implements a console-based Shorebird Habitat Use data management system using Python and SQLite. 
The application follows a closed N-layered architecture and supports CRUD operations, dataset reloading, 
and structured database persistence through the Persistence layer.

The system includes dynamic multi-column sorting functionality implemented using the SQL ORDER BY clause. 
Users can select two dataset columns and specify the sorting direction (ASC or DESC) at runtime through the console interface. 
The sorting functionality is integrated across the Presentation, Business, and Persistence layers, demonstrating 
database query processing within a layered software architecture.
 
----------------------------------------------------------------------

# Architecture

The application is structured into the following layers:

- Presentation Layer – menu.py
- Business Layer – shorebird_manager.py
- Persistence Layer – sqlite_repository.py
- Model Layer – shorebird_record.py
- Entry Point – main.py

The Presentation layer communicates only with the Business layer.  
The Business layer coordinates interactions with the Persistence and Model layers.  
The Persistence layer manages database connectivity and SQL operations using SQLite, 
including execution of dynamic multi-column ORDER BY queries through SQLite.

This architecture improves maintainability, modularity, scalability, and separation of concerns 
across the application layers.

----------------------------------------------------------------------

# Features

- Initialize SQLite database from CSV dataset
- Display records stored in the database
- Add new records dynamically
- Update existing database records
- Delete records from the database
- Reload database records from CSV dataset
- Dynamic multi-column sorting using SQL ORDER BY
- Runtime selection of sorting columns
- Runtime selection of sorting direction (ASC / DESC)
- Input validation for sorting parameters
- Closed N-layered architecture implementation
- Structured separation of Presentation, Business, Persistence, and Model layers
- SQLite persistence implemented using Python sqlite3 DB-API interface

----------------------------------------------------------------------
# Technologies Used

- Python
- SQLite
- SQL
- CSV Processing
- Git & GitHub
- Visual Studio Code
- unittest

------------------------------------------------------------------

# Database Implementation

SQLite is used as the persistence mechanism for this application.

The system:

- automatically creates the database if it does not exist
- initializes the shorebirds table when required
- loads dataset records from CSV into SQLite
- performs CRUD operations using SQL queries
- retrieves sorted records dynamically using multi-column ORDER BY queries
- maintains persistent storage using Python sqlite3 database connectivity

----------------------------------------------------------------------

# Running the Program

Run the application from the project root directory using Visual Studio Code terminal or command prompt:

python -m src.main

----------------------------------------------------------------------

# Running Unit Tests

Run unit tests from the project root directory: 

python -m unittest src.tests.test_shorebird_manager

----------------------------------------------------------------------

# Version Control

The project was developed incrementally using Git and GitHub.  
Commit history reflects architectural implementation, SQLite database integration, 
dynamic sorting functionality, feature enhancements, testing, and documentation updates.

----------------------------------------------------------------------

# Advanced Sorting Functionality

Dynamic multi-column sorting functionality was implemented using the SQL ORDER BY clause 
with two user-selected dataset columns and configurable sorting direction (ASC or DESC). 
This feature demonstrates integration between the Presentation, Business, and Persistence layers 
within a closed N-layered architecture while utilizing SQLite-based query processing.

