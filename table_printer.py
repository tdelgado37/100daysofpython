#! python3
# table_printer.py - prints a list of lists of strings in
# a well-organized table with each column right-justified.
tableData = [['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
 ]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    numRows = len(tableData[0])
    for column_num, column in enumerate(tableData):
        for element in column:
            if(len(element)>colWidths[column_num]):
                colWidths[column_num] = len(element)


    for row_index in range(numRows):
        line = ''
        for column_num, column in enumerate(tableData):
            column_width = colWidths[column_num]
            line += column[row_index].rjust(column_width) + ' '
        print(line)



printTable(tableData)
