import os

oldpath = "test-dir/"
newpath = "test-dir-copy/"

oldfiles = []
oldroots = []
newfiles = []
newroots = []

for i in os.walk(oldpath):
  root = i[0]
  files = i[2]
  for file in files:
    if (file != ".DS_Store"):
      print("Original file " + root + "/" + file)
      oldfiles += [file]
      oldroots += [root]
print(oldfiles)
print(oldroots)

for i in os.walk(newpath):
  root = i[0]
  files = i[2]
  for file in files:
    if (file != ".DS_Store"):
      print("Copied file " + root + "/" + file)
      newfiles += [file]
      newroots += [root]
print(newfiles)
print(newroots)

print("------------------------")

newindex = 0
missingfiles = []
missingroots = []
for file in oldfiles:
  root = oldroots[oldfiles.index(file)]
  newfile = newfiles[newindex]
  if (file == newfile):
    print("Found a match between original file " + file + " and new file " + newfile)
    newindex += 1
  elif (file in newfile):
    print("Found a possible match between original file " + file + " and new file " + newfile)
    newindex += 1
  else:
    print("****Found missing file " + root + "/" + file + "****")
    missingfiles += [file]
    missingroots += [root]

