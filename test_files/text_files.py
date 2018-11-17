# Open, read and write to text files. mode:
#   r = read only
#   w = write only (overwrite or create new)
#   a = append (will add to file)
#   r+ = read and write
#   w+ = write and read (overwrite or create new)
with open('text.txt', 'r') as file:
    # Print file object
    print(file)

    # PRINT AS STRING
    # Print file.read() --> string
    print(file.read())
    # Try to print file.read() again
    print(file.read())
    # Put the cursor to the BOF
    file.seek(0)
    # Print file.read()
    print(file.read())

    # PRINT AS LIST - Alt 1
    # Put the cursor to the BOF
    file.seek(0)
    # Print file.read()
    print(file.read().split('\n'))

    # PRINT AS LIST - Alt 2
    # Put the cursor to the BOF
    file.seek(0)
    # Print file.readlines() --> list
    print(file.readlines())
