import argparse
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from collections import Counter
from collections import defaultdict

parser = argparse.ArgumentParser(usage='grade_counter2.py -i input_file -o output_file -r 5 -c 7 -t 300 -q yes -s 3 -e 8', add_help=True,formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-i','--input',help = 'input file name', required=True)
parser.add_argument('-o', '--output', help = 'output file name',required=True)
parser.add_argument('-r', '--row',help = 'row number; start position of grading in input file', type=int,required=True)
parser.add_argument('-c', '--column',help = 'column number; start position of score in input file', type=int,required=True)
parser.add_argument('-t', '--total',help = 'maximum score of total grade', type=float,required=True)
parser.add_argument('-q', '--quiz',help = 'remove minimum score of quiz or not(answer; yes or no)',required=True)
parser.add_argument('-s', '--start',help = 'column number; first quiz in input file, requires for "--quiz yes" function', type=int)
parser.add_argument('-e', '--end',help = 'column number; last quiz in input file, requires for "--quiz yes" function', type=int)
args = parser.parse_args()

total = args.total
header = args.row
grading_scores = args.column
input_file_name = args.input
output_file_name = args.output
start = args.start
end = args.end

def grade(score):#define grades
        if score >= 0.92*total:
                letter = 'A'
        elif score >= 0.88*total:
                letter = 'A-'
        elif score >= 0.84*total:
                letter = 'B+'
        elif score >= 0.80*total:
                letter = 'B'
        elif score >= 0.76*total:
                letter = 'B-'
        elif score >= 0.72*total:
                letter = 'C+'
        elif score >= 0.68*total:
                letter = 'C'
        elif score >= 0.64*total:
                letter = 'C-'
        elif score >= 0.60*total:
                letter = 'D+'
        elif score >= 0.56*total:
                letter = 'D'
        elif score >= 0.52*total:
                letter = 'D-'
        else:
                letter = 'F'
        return letter 

def filename():
        with open(input_file_name, 'r') as sourcefile:#add your file name and separate data in lines
                list = sourcefile.read().splitlines()
                inputs, record = [], []
                for index in range(len(list)):
                        record = list[index].split('\t')
                        inputs.append(record)
        with open('exchange_to_numerical_data' , 'w' ) as sinkfile: #make new file
                for index in range(header-1,len(list)): #run lines from second to last (first = header)
                        data = inputs[index][grading_scores-1::]
                        data = [x.replace('', 'a') for x in data]
                        data = [x.replace('a1', '1') for x in data]
                        data = [x.replace('a2', '2') for x in data]
                        data = [x.replace('a3', '3') for x in data]
                        data = [x.replace('a4', '4') for x in data]
                        data = [x.replace('a5', '5') for x in data]
                        data = [x.replace('a6', '6') for x in data]
                        data = [x.replace('a7', '7') for x in data]
                        data = [x.replace('a8', '8') for x in data]
                        data = [x.replace('a9', '9') for x in data]
                        data = [x.replace('a0', '0') for x in data]
                        data = [x.replace('1a', '1') for x in data]
                        data = [x.replace('2a', '2') for x in data]
                        data = [x.replace('3a', '3') for x in data]
                        data = [x.replace('4a', '4') for x in data]
                        data = [x.replace('5a', '5') for x in data]
                        data = [x.replace('6a', '6') for x in data]
                        data = [x.replace('7a', '7') for x in data]
                        data = [x.replace('8a', '8') for x in data]
                        data = [x.replace('9a', '9') for x in data]
                        data = [x.replace('0a', '0') for x in data]
                        data = [x.replace('a', '0') for x in data]
                        data = [float(x) for x in data]#replace '' to '0'
                        number ='\t'.join(str(e) for e in data)
                        id = inputs[index][:grading_scores-1]
                        id_str= [str(x) for x in id]
                        ID ='\t'.join(str(e) for e in id_str)
                        sinkfile.write(ID +"\t"+number+"\n")

def finalgrade_rm_min():
        with open('exchange_to_numerical_data', 'r') as sourcefile:#add your file name and separate data in lines
                list = sourcefile.read().splitlines()
                inputs, record = [], []
                for index in range(len(list)):
                        record = list[index].split('\t')
                        inputs.append(record)
        with open(output_file_name, 'w' ) as sinkfile: #make new file
                for index in range(len(list)):
                        data = inputs[index][int(grading_scores)-1::]
                        data = [float(x) for x in data]
                        starts = int(start -int(grading_scores))
                        ends = int(end -int(grading_scores)+1)
                        quiz = data[starts:ends]#identify quiz collumns
                        others = data[ends::]#identify other scores
                        quiz.remove(min(quiz))#remove minimum quiz score
                        final = quiz + others#add all scores
                        sum = np.sum(final)#sum all scores 
                        score = float(sum)
                        id = inputs[index][:grading_scores-1]
                        id_str= [str(x) for x in id]
                        ID ='\t'.join(str(e) for e in id_str)
                        sinkfile.write(ID +"\t"+str(sum)+"\t"+grade(score) +"\n")
	with open('hist_making_file', 'w' ) as sinkfile: #make new file
                for index in range(len(list)):
                        data = inputs[index][int(grading_scores)-1::]
                        data = [float(x) for x in data]
                        starts = int(start -int(grading_scores))
                        ends = int(end -int(grading_scores)+1)
                        quiz = data[starts:ends]#identify quiz collumns
                        others = data[ends::]#identify other scores
                        quiz.remove(min(quiz))#remove minimum quiz score
                        final = quiz + others#add all scores
                        sum = np.sum(final)#sum all scores 
                        score = float(sum)
                        sinkfile.write(grade(score) +"\n")
	list_data = [line.strip() for line in open("hist_making_file", 'r')]
	int_data = defaultdict(int)
	for k in list_data:
		int_data[k]+=1
	bar_data = int_data.items()
	bar_data.sort()
	for i in range(len(bar_data)):
		x = bar_data[i][0]
		y = bar_data[i][1]
		plt.bar(x,y, color='blue')
		plt.grid(axis='y', alpha=0.75)
		plt.ylabel('Count')
		plt.xlabel('Grades')
		plt.savefig(output_file_name+".pdf")

        
def finalgrade():
        with open('exchange_to_numerical_data', 'r') as sourcefile:#add your file name and separate data in lines
                list = sourcefile.read().splitlines()
                inputs, record = [], []
                for index in range(len(list)):
                        record = list[index].split('\t')
                        inputs.append(record)
        with open(output_file_name+".txt", 'w' ) as sinkfile: #make new file
                for index in range(len(list)):
                        data = inputs[index][int(grading_scores)-1::]
                        final = [float(x) for x in data]
                        sum = np.sum(final)#sum all scores 
                        score = float(sum)
                        id = inputs[index][:grading_scores-1]
                        id_str= [str(x) for x in id]
                        ID ='\t'.join(str(e) for e in id_str)
                        sinkfile.write(ID +"\t"+str(sum)+"\t"+grade(score) +"\n")
	with open('hist_making_file', 'w' ) as sinkfile: #make new file
                for index in range(len(list)):
                        data = inputs[index][int(grading_scores)-1::]
                        final = [float(x) for x in data]
                        sum = np.sum(final)#sum all scores 
                        score = float(sum)
                        sinkfile.write(grade(score) +"\n")
	list_data = [line.strip() for line in open("hist_making_file", 'r')]
	int_data = defaultdict(int)
	for k in list_data:
		int_data[k]+=1
	bar_data = int_data.items()
	bar_data.sort()
	for i in range(len(bar_data)):
		x = bar_data[i][0]
		y = bar_data[i][1]
		plt.bar(x,y, color='blue')
		plt.grid(axis='y', alpha=0.75)
		plt.ylabel('Count')
		plt.xlabel('Grades')
		plt.savefig(output_file_name+".pdf")


def yes_or_no():
        if args.quiz == 'no':
                return finalgrade()
        if args.quiz == 'yes':
                return finalgrade_rm_min()




filename()
yes_or_no()

import os
os.remove('exchange_to_numerical_data')
os.remove('hist_making_file')
