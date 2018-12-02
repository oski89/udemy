import io

# Arbitrary string
message = 'This is just a normal string'

# Use StringIO method to set as file object
f = io.StringIO(message)
f.read()
f.write(' Second line written to file like object')

# Reset cursor just like you would in a file
f.seek(0)

# Read again
f.read()

# Close the ovject when contents are no longer needed
f.close()
