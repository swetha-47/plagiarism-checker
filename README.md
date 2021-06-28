# ***Plagiarism Checker***
<p align="center">
<img width ="333" height="250"
 src="https://user-images.githubusercontent.com/85957181/123552312-35572500-d793-11eb-936f-33f9e6242c8c.png">
 </p>
  
  ## ***Desiners***👧👩🧑
        a. M.Deepika (Branch👨‍🎓 : CSE, roll no:201000027)
        b. k.Priyanka (Branch👨‍🎓 : DSAI,roll no:201020422)
        c. K.Sai Swetha (Branch👨‍🎓: ECE,roll no:201010228)
  ## ***Description***📝
  
     The plagiarism checker  has been implemented by using languages such as 🔺Python,📍html.
     
     
   ## ***Procedure***🧾
 First we have created a class and defined
the objects which are the inputs given 
from the textarea.Then wwe have defined a
variable sk which intializes the percentage,
path,file,myfiles to 0.

The main function is called, if the request
is equal to the post method used in html then the code is runned i.e, we get the data from the 
frontend the percentage, path and the file we input.And then we will be assigning to the variable which have been initialised to zero before.
The path which we are giving as an input is of the files to be checked so the call function 
is called which takes the names of the files using glob which retrieves the files so as to print them in the results page.
The num variable calls the datas function which gives the percentage of plagiarism through the levensteins algorithm.
All the plagiarised files are printed in a list using a for loop it opens the files one by one in read mode removes the newlines and spaces and checks
if the length of the file to be checked and the master file,it takes the length of the big string.
The percentage of plagiarism is calculated by subtarcting the similarities which is ginven by the variable 'n'.
So if the value of n is greater than the minimum percentage of plagiarism it prints the value plagiarised and gets added to the list.And similarly it checks for the next files
and calculated the percent plagiarised and appends it into the list.Finally it prints the list of the files and corressponding plagiarism percentages list.
     
     
    

     
     
     
     
     
  ## ***levenshtein algorithm*** 📈
     The Levenshtein algorithm (also called Edit-Distance) calculates the least number of edit operations that are necessary to modify one string to obtain another string.
     The pictorial representation of the example matrix used in Levenshtein algorithm is
   <p align="center">
  <img width ="333" height="250"
  src="https://user-images.githubusercontent.com/81485191/123628952-4b1b2780-d831-11eb-8d0d-d5fc7df635ee.jpeg">
  </p>





  
     
