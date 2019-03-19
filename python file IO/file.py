print("Masuk")
filepath  ='read.txt'
# opens file and make it sure to be close()-ed 
with open(filepath) as fp:
    for count, line in enumerate(fp):
        print("Line {}: {}".format(count, line.strip()))
