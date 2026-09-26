def display():
    print("I am ayesha javed!")

# if __name__ == "__main__":
#     display()
    #printing bcz the name of this file is __main__
display() #running this by commenting above, the chapter 1 file automatically runs and print ayesha without calling in that file so to prevent that we use if __name__

#now i imported it in a chapt1 file and run with commenting the if in this file, maximum recursion limit reached, hence this is necessary
# print(__name__)