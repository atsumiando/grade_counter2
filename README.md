# grade_counter2
Calculate total scores, return grades(A, B, C etc...), and provide distribution histogram of grades with functions of removing minimum score of quizzes.

It is python codes and use "python grade_counter2.py -i input_file -o output_file -r 5 -c 7 -t 300 -q yes -s 3 -e 8'" to run!

# File format
Example of input_file is provided as grades.txt. 

	Name	ID	quiz1	quiz2	quiz3	quiz4	exam1	exam2	journal_club	attendance	assignment	
	Points	total	10	10	10	10	100	100	20	20	20	
	NAME1	id1	5	6	7	8	99	80	20	20	10	
	NAME2	id2	5	7	7	9	96	78	12	17	5	

# Description of file format
Quizzes should locate first part of scores. 

grade_counter.py requires -i input_file -o output_file -r row_number -c column_number -t total_maximum_score -q quiz_removal_selection <optional> -s quiz_start_column -e quiz_end_column 
 
 -h, --hele   show this help message and exit
 
 -i INPUT, --input INPUT    input file name
 
 -o OUTPUT, --output OUTPUT    output file name
 
 -r ROW, --row ROW     row number; start position of grading in input file
 
 -c COLUMN, --column COLUMN   column number; start position of score in input file
 
 -t TOTAL, --total TOTAL    maximum score of total grade
 
 -q QUIZ, --quiz QUIZ    remove minimum score of quiz or not(answer; yes or no)
 
 -s START, --start START    column number; first quiz in input file, requires for "--quiz yes" function
 
 -e END, --end END    column number; last quiz in input file, requires for "--quiz yes" function


# Outcome

Total scores and grades for each students is provided as output_file.txt as followings.

Example of out_file is provided as finalgrades.txt. 

	NAME1	id1 250	B #from 2nd_line(students total scores and grade)
	NAME2	id2 231	C #from 2nd_line(students total scores and grade)

Setting of grades are A>=92%, 92%>A->88%, 88%>B+>=84%, 84%>B>=80%, 80%>B->=76%, 76%>C+>=72%, 72%>C>=68%, 68%>C->=64%, 64%>D+>=60, 60%>D>=56%, 56%>D->=52%, and F<52%.

Distribution of grades and count of students (by histogram) is provided as output_file.pdf. Example of out_file is provided as finalgrades.pdf. 


