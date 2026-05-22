# Practical Project 4 – CST8002

File: README.md
Author: Arbutha Durairaj
Course: CST8002 – Programming Language Research
Professor: Stanley Pieda
Due date: 12 April 2026

----------------------------------------------------------------------

# Project Overview

This project implements a console-based Shorebird Habitat Use data management system using Python. 
The application follows a closed N-layered architecture and supports CRUD operations, dataset reloading, 
and SQLite database persistence using structured SQL-based storage through the Persistence layer.

As part of Practical Project Part 4, the system was enhanced with dynamic multi-column sorting functionality 
using the SQL ORDER BY clause. This feature allows users to select two dataset columns and specify the sorting 
direction (ASC or DESC) at runtime through the console interface. The sorting functionality is implemented across 
the Presentation, Business, and Persistence layers, demonstrating integration of database query processing within 
a layered Python application architecture.
 
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
including execution of multi-column ORDER BY sorting queries introduced in Practical Project Part 4.

This structure maintains separation of concerns and follows a closed N-layered architecture 
that improves maintainability and modularity.

----------------------------------------------------------------------

# Features

- Initialize SQLite database from CSV dataset
- Display records from database
- Add new records to database
- Update existing database records
- Delete records from database
- Reload database from CSV dataset
- Multi-column sorting using SQL ORDER BY clause
- Runtime selection of dataset columns for sorting
- Runtime selection of sorting direction (ASC / DESC)
- Input validation for sorting parameters
- Structured separation of Presentation, Business, Persistence, and Model layers 
- SQLite persistence implemented using Python sqlite3 DB-API interface

----------------------------------------------------------------------

# Database Implementation

SQLite is used as the persistence mechanism for this project.

The application:

- creates the database automatically if it does not exist
- creates the shorebirds table if missing
- loads dataset records from CSV into the database
- performs CRUD operations using SQL queries
- retrieves sorted records dynamically using multi-column ORDER BY queries

----------------------------------------------------------------------

# Running the Program

From the project root directory:  

python -m src.main

----------------------------------------------------------------------

# Running Unit Tests

From the project root directory: 

python -m unittest src.tests.test_shorebird_manager

----------------------------------------------------------------------

# Version Control

The project was developed incrementally using Git.
Commit history reflects architectural implementation, database integration, 
multi-column sorting enhancement, feature development, and documentation updates.

----------------------------------------------------------------------

# Advanced Feature Implemented (Practical Project Part 4)

Dynamic multi-column sorting functionality was implemented using SQL ORDER BY
with two user-selected dataset columns and configurable sorting direction (ASC or DESC).
This enhancement demonstrates integration across the Presentation, Business,
and Persistence layers within a closed N-layer architecture.

