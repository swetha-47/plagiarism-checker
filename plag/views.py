from django.http import request,HttpResponse, response
from django.shortcuts import redirect, render
import numpy as np
import os
import glob

# Create your views here.
class Check():
    def __init__(self,percentage,path,file,myfiles):
        self.percentage=percentage
        self.path=path
        self.file=file
        self.myfiles=myfiles

sk=Check(0,0,0,0)
def main(request):
    if request.method=="POST":
        percentage=request.POST.get('percentage', '')
        path=request.POST.get('path', '')
        file=request.POST.get('file', '')
        sk.percentage=percentage
        sk.path=path
        sk.file=file
        sk.myfiles=call()
        num=datas()
        print(sk.myfiles)
        dir={'percentage':sk.percentage,'files':sk.myfiles,'l':num}
        return render(request,'result.html',dir)
    else:
        return render(request,'index.html')

########################################################################################################
def call():
    os.chdir(sk.path)
#opening all text files within the folder and stores them in an array
    myFiles = glob.glob('*.txt')
    print("\nThe text files available are :\n")
    print(myFiles)
    return myFiles

    

def datas():

# defining a function to compare the strings using levenshtein's algorithm
    def levenshtein(seq1, seq2):
        size_x = len(seq1) + 1
        size_y = len(seq2) + 1
 
  # defining a zero matrix of size of first string * second string
        matrix = np.zeros ((size_x, size_y)) 
 
        for x in range(size_x):
            matrix [x, 0] = x # row array with elements of x
        for y in range(size_y):
            matrix [0, y] = y # column array with elements of y
        for x in range(1, size_x):
            for y in range(1, size_y):
                if seq1[x-1] == seq2[y-1]: # if the alphabets at the postion is same
                    matrix [x,y] = min(
                        matrix[x-1, y] + 1,
                        matrix[x-1, y-1],
                        matrix[x, y-1] + 1
                    )
 
                else:         # if the alphabbets at the position are different
                    matrix [x,y] = min(
                        matrix[x-1,y] + 1,
                        matrix[x-1,y-1] + 1,
                        matrix[x,y-1] + 1
                    )
 
    # returning the levenshtein distance i.e last element of the matrix
        return (matrix[size_x - 1, size_y - 1])

    data=sk.file.replace('\n','')
    str1=data.replace(' ','')
    print("\nPlagiarised files are :")  
    l=[]
    for i in range (0,len(sk.myfiles)) :
        with open(sk.myfiles[i], 'r') as file:
            data = file.read().replace('\n', '')
            str2=data.replace(' ', '')
        if(len(str1)>len(str2)):
            length=len(str1)
        else:
            length=len(str2)
    
        n = 100-round((levenshtein(str1,str2)/length)*100,2)
        
        if (n>int(sk.percentage)):
            print(sk.myfiles[i],n,"% plagiarised")
        n=str(n)+'%'
        l.append(n)
    os.chdir(r'C:\Users\Sudheer\OneDrive\Desktop\PLAG.checker project\plag-check')
    return l
    
