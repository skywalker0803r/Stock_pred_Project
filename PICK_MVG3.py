import stockfunction3 as st3
import time

errors=0
times=0
Match_list=[]
Error_list=[]
print('Loading...')

sids=st3.GetAllSid()

for sid in sids:
	try:
		times+=1
		n=st3.GetmvgSignal(sid)
		#print(n)
		print(sid,'5dmvg',str(n[0]).split('.')[0][0:-2]+'.'+str(n[0]).split('.')[0][-2:])
		print(sid,'10dmvg',str(n[1]).split('.')[0][0:-2]+'.'+str(n[1]).split('.')[0][-2:])
		print(sid,'20dmvg',str(n[2]).split('.')[0][0:-2]+'.'+str(n[2]).split('.')[0][-2:])
		print(sid,'old_5mvg',str(n[3]).split('.')[0][0:-2]+'.'+str(n[3]).split('.')[0][-2:])
		print(sid,'old_10dmvg',str(n[4]).split('.')[0][0:-2]+'.'+str(n[4]).split('.')[0][-2:])
		print(sid,'old_20dmvg',str(n[5]).split('.')[0][0:-2]+'.'+str(n[5]).split('.')[0][-2:])
		print('Number of errors:',errors)
		print('number of times:',times)
		if n[0]>n[1] and n[1]>n[2] and n[3]<n[4] and n[4]<n[5]:
			Match_list.append(sid)
			print(sid,'Target match!')
			print('The match List:',Match_list)
		else:
			print(sid,'Target NOT match!')		
	except Exception as e:
	#except FileNotFoundError as e:
	#except IndexError as e: 
		print(e,type(e))
		errors+=1
		Error_list.append([sid,type(e)])
		print('The match List:',Match_list)
		print('Number of errors:',errors)
		print('number of times:',times)
		continue		
print('-------------result--------------')
print('Total-check:',times)
print('File-NOT-Found-errors:',errors)
print('File-NOT-Found-errors:',Error_list)		
print('success-Match:',Match_list)
time.sleep(30)


