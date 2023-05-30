
import random 
import subprocess
import re
import argparse
import sys



try:
		#random mac address generator
		oneList=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
		macNew = ""
		point=""
		for i in range(10): 
			macNew = macNew + random.choice(oneList)
			
			if (i < 9):
				for i in range(1):
					point = point + random.choice(oneList)
					len1=len(point)
					if(len1%2==0):
						macNew = macNew + ":"
						break;

		#first two mac address assignments
		fistwo_mac = ""
		twoList=["0","2","4","6","8"]
		for i in range(2):
			fistwo_mac = fistwo_mac + random.choice(twoList)
			if (i < 2 ):
				for i in range(1):
					point = point + random.choice(twoList)
					len2=len(point)
					if(len2%2==0):
						break;
					else:
						fistwo_mac = fistwo_mac + ":"	
						break;

		#İNTERFACE FİND and OLD MAC FİND
		interface_input=input("interface name ? = ")
		macold_interface = subprocess.check_output("ifconfig "+interface_input,shell=True).decode()
		macOld = re.search("ether(.*?)txqueuelen",macold_interface).group(1)
		


		#change mac address
		macfinsh=fistwo_mac+macNew
		subprocess.check_output("sudo ifconfig " +interface_input+ " down " , shell=True)
		subprocess.check_output("sudo ifconfig " +interface_input+ " hw ether " +macfinsh, shell=True)
		subprocess.check_output("sudo ifconfig " +interface_input+ " up", shell=True)

		#screen outputs (interface , old mac , new mac names)
		print("Old Mac = " + macOld)
		print("New Mac =  " +  macfinsh)
		print("successfully changed. TR ")

except subprocess.CalledProcessError :
		#print("You entered the wrong interface name")
	    print('\n'+ '\t' + '\t'"YOUR NETWORK" + '\n'+ '\t' + '\n'+ subprocess.check_output('ifconfig ',shell=True).decode())
	    
