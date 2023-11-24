import os
import hashlib

oldpath = "test-dir/"
newpath = "test-dir-copy/"

oldfiles = []
oldroots = []
newfiles = []
newroots = []

# Go through the old directory and save file locations and roots to corresponding directories
# (They are linked by their shared index position which is bad or whatever but I'm too lazy
# to make an object just for this)
for i in os.walk(oldpath):
  root = i[0]
  files = i[2]
  for file in files:
    if (file != ".DS_Store"):
      print("Original file " + root + "/" + file)
      oldfiles += [file]
      oldroots += [root]

# Go through the new directory and save file locations and roots
for i in os.walk(newpath):
  root = i[0]
  files = i[2]
  for file in files:
    if (file != ".DS_Store"):
      print("Copied file " + root + "/" + file)
      newfiles += [file]
      newroots += [root]

print("------------------------")

missingfiles = []

# Loop through both old files and new files to find matches
for file in oldfiles:
  foundmatch = False
  root = oldroots[oldfiles.index(file)]
  filepath = os.path.join(root, file)
  oldfilehash = hashlib.md5(open(filepath, "rb").read()).hexdigest()
  for newfile in newfiles:
    newroot = newroots[newfiles.index(newfile)]
    newfilepath = os.path.join(newroot, newfile)
    newfilehash = hashlib.md5(open(newfilepath, "rb").read()).hexdigest()
    if (oldfilehash == newfilehash):
      print("Found a match between original file " + file + " and new file " + newfile)
      foundmatch = True
      break
  if (not foundmatch):
    print("****Found missing file " + filepath + "****")
    missingfiles += [filepath]

print("All missing files:")
print(missingfiles)
