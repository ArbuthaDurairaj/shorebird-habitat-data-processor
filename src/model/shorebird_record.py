# File: shorebird_record.py
# Author: Arbutha Durairaj
# Course: CST8002 – Programming Language Research
# Professor: Stanley Pieda
# Due date: 29 March 2026
#
# Description:
# Defines the ShorebirdRecord class, which represents a single record
# from the Migratory Shorebird Habitat Use dataset.
# 
# Architecture:
# Part of a closed N-layered architecture.
# The Model layer defines the data structure representing a
# single ShorebirdRecord and contains no dependencies on other layers.
#
# References:
# [8] Parks Canada, “Migratory Shorebird Habitat Use – Pacific Rim National Park,”
# Government of Canada Open Data Portal, 2017. [Online]. Available:
# https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697
# [Accessed: 26-Jan-2026].

class ShorebirdRecord:
    """
    Represents one row (record) from the shorebird CSV dataset.
    """

    def __init__(self, site_id, area, visit_date, start_time, species_code, count):
        """
        Initializes a ShorebirdRecord object using dataset column values.
        """
        self.site_id = site_id
        self.area = area
        self.visit_date = visit_date
        self.start_time = start_time
        self.species_code = species_code
        self.count = int(count)
      


    def __str__(self):
        return (
            f"{self.site_id:<8}"
            f"{self.area:<6}"
            f"{self.visit_date:<12}"
            f"{self.start_time:<12}"
            f"{self.species_code:<15}"
            f"{self.count:>6}"
        )
    