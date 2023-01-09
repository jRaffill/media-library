import os
import hashlib

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

for i in os.walk(newpath):
  root = i[0]
  files = i[2]
  for file in files:
    if (file != ".DS_Store"):
      print("Copied file " + root + "/" + file)
      newfiles += [file]
      newroots += [root]

print("------------------------")

newindex = 0
missingfiles = []

for file in oldfiles:
  root = oldroots[oldfiles.index(file)]
  newfile = newfiles[newindex]
  filepath = os.path.join(root, file)
  if (file == newfile):
    print("Found a match between original file " + file + " and new file " + newfile)
    newindex += 1
  elif (file in newfile):
    newfilepath = os.path.join(newroots[newindex], newfile)
    oldfilehash = hashlib.md5(open(filepath, "rb").read()).hexdigest()
    newfilehash = hashlib.md5(open(newfilepath, "rb").read()).hexdigest()
    if (oldfilehash == newfilehash):  
      print("Found a match between original file " + file + " and new file " + newfile)
      newindex += 1
    else:
      print("****Found missing file " + filepath + "****")
  else:
    print("****Found missing file " + filepath + "****")
    missingfiles += [filepath]

print("All missing files:")
print(missingfiles)
