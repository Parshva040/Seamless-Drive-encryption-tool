import os

file = ".secret.txt"
open(file, "+wb")
os.system(f' attrib +h "{file}"')