import shutil
import os
'''
The shutil module in Python is part of the standard library and provides a number of high-level operations on files and collections of files. Its main use is for copying and removal of files and directories.
shutil.copy(src, dst): Copies the file from src to dst. The destination can be a directory or a file.
shutil.copy2(src, dst): Similar to shutil.copy, but it also attempts to preserve file metadata.
shutil.copyfile(src, dst): Copies the contents of the file from src to dst. The destination must be a file.
shutil.copytree(src, dst): Recursively copies an entire directory tree rooted at src to a directory named dst.
shutil.rmtree(path): Recursively deletes a directory tree.
shutil.remove(path): Deletes a file.
'''
os.chdir("D:/PROGRAMMING/python")
# shutil.copy("text.py", "text1.py")
# shutil.copytree("libraries", "library")
shutil.rmtree("library")
