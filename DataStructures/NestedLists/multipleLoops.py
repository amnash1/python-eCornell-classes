"""
Module demonstrating immutable functions on nested lists.

All of these functions make use of accumulators that make new lists.

Author: Andy Nash
Date: 2022-12-17
"""


def row_sums(table):
    """
    Returns a list that is the sum of each row in a table.

    This function assumes that table has no header, so each row has only numbers in it.

    Examples:
        row_sums([[0.1,0.3,0.5],[0.6,0.2,0.7],[0.5,1.1,0.1]]) returns [0.8, 1.5, 1.7]
        row_sums([[0.2,0.1],[-0.2,0.1],[0.2,-0.1],[-0.2,-0.1]]) returns [0.3, -0.1, 0.1, -0.3]

    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words,
        (1) table is a nested 2D list in row-major order,
        (2) each row contains only numbers, and
        (3) each row is the same length.
    """
    #Returns a list that is the sum of each row in a table.
    final_result = []

    for row in table:
        #row is full table row
        #print (row)

        result = 0
        for value in row:
            #value is value in a row
            #print(value)
            result = result + value
            #print (result)
        #immutable so the result needs to appar in "final-result"
        final_result.append(result)

    return final_result

        #l = []
        #a = 1+1
        #l.append(a)
        #l
        #[2]

def crossout(table,row,col):
    """
    Returns a copy of the table, missing the given row and column.

    Examples:
        crossout([[1,3,5],[6,2,7],[5,8,4]],1,2) returns [[1,3],[5,8]]
        crossout([[1,3,5],[6,2,7],[5,8,4]],0,0) returns [[2,7],[8,4]]
        crossout([[1,3],[6,2]],0,0) returns [[2]]
        crossout([[6]],0,0) returns []

    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words,
        (1) table is a nested 2D list in row-major order,
        (2) each row contains only numbers, and
        (3) each row is the same length.

    Parameter row: the row to remove
    Precondition: row is an index (int) for a row of table

    Parameter col: the colummn to remove
    Precondition: col is an index (int) for a column of table
    """
    final_result = []

    for r in table:
        #r = rows in the table
        #break out the table records
        #print (r)
        #second for loop with new accumulators
        result = []
        pos = 0

        for value in r:
            #print(r)
            #find the values that are not crossed out out
            #find position of the
            if table.index(r) != row:
                #find position of the col value that doesn't match
                if pos != col:
                    result.append(value)
            pos = pos +1

        if len(result) > 0:
            final_result.append(result)
            #final_result
    return final_result

#table = [[0.1,0.3,0.5],[0.6,0.2,0.7],[0.5,1.1,0.1]]
#crossout([[1,3,5],[6,2,7],[5,8,4]],0,0)
