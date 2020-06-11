# oh soldier pretiffy my folder
# input path as a input , file having the words that are not to be changed , format
# captilize the first letter of all the folders
# if the word is in the text file don't rename them
# change the name of the files from the format then rename it with numbers
import os
def soldier(path,text_file,format):
    os.chdir(path)
    folders = os.listdir()
    count = 1
    with open(text_file) as f:
        list_of_words = f.read().split(" ")
    for files in folders:
        if files in list_of_words:
            pass
        elif files.endswith(format):
            os.rename(files,f'{count}{format}')
            count = count + 1
        else:
            os.rename(files,files.capitalize())


soldier("C:\\Users\\User\\Desktop\\Prac","g.txt",".jpg")












