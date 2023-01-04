"""
Module with a function to write CSV files (using data in a 2D list)

This function will be used in the main project.  You should hold on to it.

Author: Andy Nash
Date: 2022-12-29
"""
import csv


def write_csv(data,filename):
    """
    Writes the given data out as a CSV file filename.

    To be a proper CSV file, data must be a 2-dimensional list with the first row
    containing only strings.  All other rows may be any Python value.  Dates are
    converted using ISO formatting. All other objects are converted to their string
    representation.

    Parameter data: The Python value to encode as a CSV file
    Precondition: data is a  2-dimensional list

    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .csv or .CSV.  The file may or may not exist.
    """

    #Pay attention to the precondition, particularly the restriction that only
    #nested lists may be written to the file.

    #open file from filepath
    file = open(filename,'w')
    #create a second object
    wrapper = csv.writer(file)
    #for loop to
    for row in data:
        #print(row)
        wrapper.writerow(row)
        #print(wrapper.writerow(row))

    file.close()
#write_csv('files/writecsv1.csv')
