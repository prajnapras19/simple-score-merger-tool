"""
Created by:
Prajna Prasetya 
linkedin.com/in/prajna-prasetya-574a65178
github.com/prajnapras19
"""
#import the libraries
import os
import csv

#get csv file(s) that we will work on
directory = os.getcwd()
file_name_list = list()

for file_name in os.listdir(directory):
	if (file_name.endswith(".csv") and file_name!="sorted.csv"):
		file_name_list.append(file_name)
		
file_name_list = sorted(file_name_list)
if (len(file_name_list)==0):
	print("No csv file found! Program exited.".format(directory))
else:
	score_list = dict() #the dictionary of the score,key=NIS,value=dictionary(key=course name,value=score)
	
	#iterate through the file(s)
	for file_name in file_name_list:
		with open(file_name) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			courses = list()
			for row in csv_reader:
				if row[0] == "NIS":
					courses = []
					for course_name in row[1:]:
						courses.append(course_name)
				else:
					if (row[0] not in score_list.keys()):
						score_list[row[0]] = dict()
					i = 0
					for score in row[1:]:
						score_list[row[0]][courses[i]] = score
						i += 1
	
	#merge the score, sort by NIS in sorted.csv file
	try:
		result = list()
		with open("sorted.csv") as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			items = list()
			for row in csv_reader:
				if row[0] == "NIS":
					items = []
					for item_name in row[2:]:
						items.append(item_name)
					result.append(",".join(row))
				else:
					result_string = "{},{}".format(row[0],row[1])
					NIS = row[0]
					result_tmp = list()
					if (NIS in score_list.keys()):
						for item_name in items:
							if (item_name in score_list[NIS].keys()):
								result_tmp.append(score_list[NIS][item_name])
							else:
								result_tmp.append("")
						if (len(result_tmp)>0):
							result_string += "," + ",".join(result_tmp)
					result.append(result_string)

		result_file = open("result.csv","w")
		result_file.write("\n".join(result))
		result_file.close()
		print("Scores merged successfully!")
		print("View results in result.csv")
	except FileNotFoundError:
		print("sorted.csv file not found! Program exited.")
