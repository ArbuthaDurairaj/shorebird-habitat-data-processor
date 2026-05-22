# File: main.py
# Author: Arbutha Durairaj
# Course: CST8002 – Programming Language Research
# Professor: Stanley Pieda
# Due date: 12 April 2026
# 
# Description:
# Main entry point for Practical Project 4.
# Launches the presentation layer (menu system).
#
# Architecture:
# Application entry point for a closed N-layered architecture.
# Initializes the Presentation layer and does not contain business
# or database persistence operations.
#
# References:
# [8] Parks Canada, “Migratory Shorebird Habitat Use – Pacific Rim National Park,”
# Government of Canada Open Data Portal, 2017. [Online]. Available:
# https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697
# [Accessed: 26-Jan-2026].
#
#


from src.presentation.menu import run_menu

DATASET_PATH = "data/pacific_rim_npr_coastalmarine_migratory_shorebird_habitat_use_2011-2017_data.csv"

def main():
    """
    Program entry point that starts the presentation layer.
    """
    run_menu(DATASET_PATH)

if __name__ == "__main__":
    main()





