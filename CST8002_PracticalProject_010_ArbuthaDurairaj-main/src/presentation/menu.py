# File: menu.py
# Author: Arbutha Durairaj
# Course: CST8002 – Programming Language Research
# Professor: Stanley Pieda
# Due date: 12 April 2026
#
# Description:
# Presentation layer component responsible for handling user interaction
# through a console-based menu system. Provides interactive options to
# display, reload,  create, update, sort and delete ShorebirdRecord objects by delegating
# operations to the Business and Persistence layers. Includes runtime validation for dataset 
# column selection and sorting order as part of the Practical Project Part 4 enhancement.
#
# Architecture:
# Part of a closed N-layered architecture.
# This Presentation layer communicates only with the Business layer
# and does not directly access persistence or model components.
#
# References:
# [6] Microsoft, "N-tier architecture style," Microsoft Learn, 19 September 2025. [Online]. 
# Available: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/n-tier. [Accessed 5 February 2026].
# 
# [5] TutorialsTeacher, "ORDER BY Clause - SQL Server," tutorialsteacher.com, n.d. [Online]. 
# Available: https://www.tutorialsteacher.com/sqlserver/orderby. [Accessed 27 March 2026].
#




"""
Presentation layer: Console-based user interface.
"""


from src.business.shorebird_manager import ShorebirdManager


def run_menu(dataset_path):
    """
    Starts the console-based user interface.

    Parameters:
        dataset_path (str): Path to the CSV dataset file.

    The function initializes the Business layer, loads dataset
    records, and provides menu-driven CRUD operations.
   """
    
    print("==============================================")
    print("CST8002 Programming Language Research")
    print("Practical Project 4")
    print("Program by Arbutha Durairaj")
    print("==============================================")
    
   
    manager = ShorebirdManager()
    # manager.load_data(dataset_path)

    while True:
        print("Author: Arbutha Durairaj")
        print("\nMenu Options:")
        print("1. Display records")
        print("2. Reload data from dataset")
        
        print("3. Add record")
        print("4. Edit record")
        print("5. Delete record")
        print("6. Sort records by two columns")
        print("7. Exit")

        choice = input("Enter your choice: ")
        

        if choice == "1":
            print(
        f"{'Site ID':<8} {'Area':<6} {'Visit Date':<12} "
        f"{'Start Time':<12} {'Species Code':<15} {'Count':>6}"
                 )
            print("-" * 75)
            
            for record in manager.get_all():
            # print("\nDisplaying first 20 sorted records:\n")
            # for record in manager.get_all()[:20]:
    
                print(record)

        elif choice == "2":
            manager.load_data(dataset_path)
            # print("Data reloaded from file successfully.")
            print("Database initialized from CSV successfully.")

        elif choice == "3":
          site_id = input("Enter Site ID: ")
          area = input("Enter Area: ")
          visit_date = input("Enter Visit Date: ")
          start_time = input("Enter Start Time: ")
          species_code = input("Enter Species Code: ")
          count = input("Enter Count: ")

          manager.create_record(
            site_id, area, visit_date,
            start_time, species_code, count
          )

          print("Record added successfully.")

        elif choice == "4":
            try:
                index = int(input("Enter record index to edit (starting from 0): "))

                site_id = input("Enter new Site ID: ")
                area = input("Enter new Area: ")
                visit_date = input("Enter new Visit Date: ")
                start_time = input("Enter new Start Time: ")
                species_code = input("Enter new Species Code: ")
                count = input("Enter new Count: ")

                updated_record = manager.build_record(
                    site_id, area, visit_date,
                    start_time, species_code, count
        

                )

                manager.update_record(index, updated_record)
                print("Record updated successfully.")

            except ValueError:
                print("Invalid input. Please enter numeric index.")

        elif choice == "5":
            try:
                index = int(input("Enter record index to delete (starting from 0): "))
                manager.delete_record(index)
                print("Record deleted successfully.")

            except ValueError:
                print("Invalid input. Please enter numeric index.")

        elif choice == "6":

            
            valid_columns = [
                "Site identification",
                "Area",
                "Visit date",
                "Start time",
                "Species code",
                "Count"
            ]
            
            print("\nAvailable columns:")

            for i, col in enumerate(valid_columns, start=1):
                print(f"{i}. {col}")

            column1 = input("Enter first column name: ")
            column2 = input("Enter second column name: ")
            order = input("Enter sort order (ASC or DESC): ").upper()

            if column1 not in valid_columns or column2 not in valid_columns:
               print("Invalid column name entered.")
               continue

            if order not in ["ASC", "DESC"]:
               print("Invalid sorting order. Enter ASC or DESC only.")
               continue

            manager.sort_records(column1, column2, order)

            print("Records sorted successfully.")
        
        elif choice == "7":
            print("Exiting program.")
            break
        
        else:
            print("Invalid option. Please try again.")