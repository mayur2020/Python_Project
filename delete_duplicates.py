import os
import hashlib
import time
import sys
from collections import defaultdict

start="\""*40
head="--" *45
gap="\n"*5

def hashfile(path,blocksize=1024):
	afile=open(path,'rb')
	hasher=hashlib.md5()
	buf=afile.read(blocksize)
	while (len(buf)>0):
		hasher.update(buf)
		buf=afile.read(blocksize)
	afile.close()
	return hasher.hexdigest()


def displaychecksum(path):
	print(" - - - - - - - - - - -  FILES INFO WITH HASH VALUES - - - - - - - - - - - \n\n")
	flag=os.path.isabs(path)
	if flag==False:
		path=os.path.abspath(path)
	exists=os.path.isdir(path)
	filenames=list()
	dups=defaultdict(list)
	if exists:
		for dirs,subdirs,files in os.walk(path):
			print(head,"\n\n")
			print("Current Folder is :- "+ dirs)
			print("\n")
			print("\tFILE_NAME \t\t  HASH VALUE \n")
			for file in files:
				path=os.path.join(dirs,file)
				file_hash=hashfile(path)
				print("\t"+file + "\t\t"+ file_hash)
				#print(file_hash)
				filenames.append((file_hash,path))

		#print(filenames)
		for f_hash,name in filenames:
			dups[f_hash].append(name)
		#print(dups)				
		return dups;
	else:
		print("Path doesn't Exists")

def printdups(dict1):
	results= list(filter(lambda x:len(x)>1 , dict1.values()))
	if(len(results)>0):
		print(head)
		print("\n\n")
		print("/========  Duplicates found  ========/\n\n")
		file = open("log.txt",'w')

		icnt=0
		for result in results:
			for dup in result:
				icnt+=1
				if icnt>=2:
					print('\t%s'%dup,end="\n")
					file.write("\t\t"+dup+"\n")
			icnt=0
			print("\n\n")

		file.close()
	else:
		print("``````````````  No Duplicates found   `````````````` \n")

def deletedups(dict1):
	results= list(filter(lambda x:len(x)>1 , dict1.values()))

	if(len(results)>0):
		icnt=0
		for result in results:
			for dup in result:
				icnt+=1
				if icnt>=2:
					os.remove(dup)
			icnt=0
		print("`````````````````  Duplicates deleted successfully  ``````````````````` \n")
	else:
		print("`````````````````   No duplicates found  ```````````````````\n")




def main():

	try:
		print(gap)
		print(start)
		print(gap)
		start_time=time.time()
		arr={}
		arr=displaychecksum(sys.argv[1])
		print(gap)
		print(head)
		printdups(arr)
		print(gap)
		deletedups(arr)
		print(gap)
		end_time=time.time()
		print(" Execution Time is :-%s"%(end_time-start_time))

	except Exception as e:
		print("Marvellous Error Is :-  "+e)



if __name__=="__main__":
	main()