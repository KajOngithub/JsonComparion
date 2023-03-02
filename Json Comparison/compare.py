import difflib
import glob, os
import re

rootDirectory = 'C:/Users/dared/Desktop/Marauders Folder Test/New Version'

outputFileName = input("Enter your output file name: ")
for subdir, dirs, files in os.walk(rootDirectory):
    for file in files:
        
        outFile = open(outputFileName, "a")
        missingfiles = open(outputFileName+" missingfiles", "a")
        print(os.path.join(subdir, file))
        print(os.path.join(subdir.replace("New Version", "Old Version"), file))
        
        if os.path.isfile(os.path.join(subdir, file)):
            match = re.search("\.json$", file)
            if match:           
                try:
                    with open(os.path.join(subdir, file)) as newFile:
                        newFile_text = newFile.readlines()

                
                    with open(os.path.join(subdir.replace("New Version", "Old Version"),file)) as oldFile:
                        oldFile_text = oldFile.readlines()
                

                
        
                    index = 0    
                    for line in difflib.unified_diff(
                            oldFile_text, newFile_text, fromfile=os.path.join(subdir.replace("New Version", "Old Version"),file),
                            tofile=os.path.join(subdir, file), lineterm='\n',n=0):
                        if line.startswith('---'):
                            outFile.write('\n')
                        outFile.write(line)
                except:
                    missingfiles.write(os.path.join(subdir.replace("New Version", "Old Version"),file) + " Does not exist\n")
                    print(os.path.join(subdir.replace("New Version", "Old Version"),file) + " Does not exist")
            
missingfiles.close()
newFile.close()
oldFile.close()
outFile.close()


