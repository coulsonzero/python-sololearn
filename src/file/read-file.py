filename = "test.txt"

# write file
file = open(filename, "w")
file.write("""hello \
this is a text
you could change it
in here""")
file.close()

# read file
with open(filename) as f:
    text = f.read()
print(text)

'''
hello this is a text
you could change it
in here
'''