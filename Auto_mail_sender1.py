from packages import *
from delete_duplicates import *
import urllib.request
start="\""*40
head="--" *45
gap="\n"*5

def is_connected():
	try:
		urllib.request.urlopen('http://216.58.192.142',timeout=2)
		return True
	except Exception as e:
		raise e
		return False

def MailSender(log_file,time):
	sender="sachin.kulawade18@vit.edu"
	receiver="sachin23698@gmail.com"
	try:
		msg=MIMEMultipart()
		msg['From']=sender
		msg['To']=receiver
		body="""
			Hello %s ,
			Welcome
			Please find attached documents which contains Log of running processes.
			Log file is created at  %s
			This is Auto generated file. 
			Do not try to reply
			Thanks and regards,
			Sachin Kulawade """%(receiver,time)

		subject=""" Log File records created using Automation at : %s """%(time)
		msg['Subject']=subject
		
		#Body is attached using MIMEText
		msg.attach(MIMEText(body,'plain'))
		


		filename = log_file
		f = open(filename)
		p = MIMEText(f.read())
		p.add_header('content-Disposition',"attachment ; Filename = %s " %filename)
		msg.attach(p)

		server=smtplib.SMTP_SSL('smtp.gmail.com',465)
		server.ehlo()
		server.login(sender,'vit1234$')
		text=msg.as_string()
		server.sendmail(sender,receiver,text)
		server.close()

		print("Mail Sent successfully to %s"%receiver)

	except Exception as e:
		print("ERROR is :- ",e)



def ProcessLog():

	connected=is_connected()
	if connected:
		print("==  ==  ==  ==  ==  connected successfully  ==  ==  ==  ==")
		#start_time=time.time()
		MailSender("log.txt",time.ctime())
	#	end_time=time.time()

	#	print("Took %s time"%(end_time-start_time))
	else:
		print("Not connected")


def main():

	print("Application Name : = " + sys.argv[0])

	if(len(sys.argv)!=2):
		print("Invalid number of arguments \n")
		exit()

	if(sys.argv[1]=='u' or sys.argv[1]=='U'):
		print("Application Sends Mail automatically after specific period of time with attached log file of running processes \n")
		exit()

	if(sys.argv[1]=='-h' or sys.argv[1]=='-H'):
		print("Applicationname time filename")
		exit()

	try:
		start_time=time.time()
		print(gap)
		print(start)
		print(gap)
		start_time=time.time()
		arr={}
		arr=displaychecksum(sys.argv[1])
		print(gap)
		print(head)
		
		printdups(arr)
		
		ProcessLog()
		end_time=time.time()
		print(gap)
		print(" Execution Time is  ::  %s"%(end_time - start_time))
		print("\n\n")
		print(start)

	except ValueError:
		print("Error : Invalid Datatype of input\n")



if __name__=="__main__":
	main()