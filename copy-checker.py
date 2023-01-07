import os

oldpath = "test-dir/"
newpath = "test-dir-copy/"

for i in os.walk(oldpath):
  root = i[0]
  files = i[2]
  for file in files:
    if (file != ".DS_Store"):
      print("Original file " + root + "/" + file)

for i in os.walk(newpath):
  root = i[0]
  files = i[2]
  for file in files:
    if (file != ".DS_Store"):
      print("Copied file " + root + "/" + file)
