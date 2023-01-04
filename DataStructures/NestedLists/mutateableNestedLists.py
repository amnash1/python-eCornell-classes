"""
Module demonstrating mutable functions on nested lists.

All of these functions modify their list arguments.

Author: Andy Nash
Date: 2022-12-17
"""


def crossout(table,row,col):
    """
    Modifies the table to remove the given row and column.

    Examples:
        If a = [[1,3,5],[6,2,7],[5,8,4]], crossout(a,1,2) changes a to [[1,3],[5,8]]
        If a = [[1,3,5],[6,2,7],[5,8,4]], crossout(a,0,0) changes a to [[2,7],[8,4]]
        If a = [[1,3],[6,2]], crossout(a,0,0) changes a to [[2]]
        If a = [[6]], crossout(a,0,0) changes a to []

    Parameter table: the nested list to modify
    Precondition: table is a table of numbers.  In other words,
        (1) table is a nested 2D list in row-major order,
        (2) each row contains only numbers, and
        (3) each row is the same length.

    Parameter row: the row to remove
    Precondition: row is an index (int) for a row of table

    Parameter col: the colummn to remove
    Precondition: col is an index (int) for a column of table
    """
    table.remove(table[row])
    #print(table)
    for ro in table:
        #print('row being reviewed is ' +str(ro))
        #r = rows in the table
        #break out the table records
        pos = 0
        for cl in ro:
            #print('column being reviewed is ' + str(cl))
            if pos == col:
                #print('column to remove is ' + str(pos))
                ro.remove(cl)
            pos = pos +1
    #rint(table)




def place_sums(table):
    """
    Modifies the table to add a column summing the previous elements in the row.

    This function assumes that the table has a header, which means the first row
    only has strings in it.  The later rows are only numbers.  This function
    adds the string 'Sum' to the first row.  For each later row, it appends the
    sum of that row.

    Example: Suppose that a is

        [['First','Second','Third'], [0.1,0.3,0.5], [0.6,0.2,0.7], [0.5,1.1,0.1]]

    then place_sums(a) modifies the table a so that it is now

        [['First', 'Second', 'Third', 'Sum'],
         [0.1, 0.3, 0.5, 0.8], [0.6, 0.2, 0.7, 1.5], [0.5, 1.1, 0.1, 1.7]]

    Parameter table: the nested list to process
    Precondition: table is a table of numbers with a header.  In other words,
    (1) table is a nested 2D list in row-major order, (2) the first row only
    contains strings (the headers) (3) each row after the first contains only
    numbers, and (4) each row is the same length.
    """
    #However, in addition to modifying the table, this function requires that
    #the table have a header row too.
    #skip first row


    for row in table[1:]:
        #print ('row being reviewed is '+str(row))
        row.append(sum(row))
    table[0].append('Sum')
    #print(table)



a=[['P1','P3','P5','P7','P9'], [0.7, 0.0, -0.7, 1.0, -0.9]]
place_sums(a)
