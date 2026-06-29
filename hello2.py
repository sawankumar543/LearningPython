b = "Hello, World!"
print(b[-5:-2]) # mean, print(b[8:11])

print(len(b)) # Output => 13
print(len(b)-5) # Output => 8
print(len(b)-2) # Output => 11

b = "   Hello,       World!    "
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(b.strip()) # Remove whitespace

print(a.replace("H", "J")) # The replace() method replaces a string with another string;

print(a.split(","))