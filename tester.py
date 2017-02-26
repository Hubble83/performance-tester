'''''''''''''''''''''''''''''''''''''''''''''''''''
	 '										 '
	 '		 (_)	| |						 '
	 '  _ __  _  ___| | ____ ___  _____		 '
	 ' | '_ \| |/ __| |/ / _` \ \/ / _ \	 '
	 ' | |_) | | (__|   < (_| |>  <  __/  ^	 '
	 ' | .__/|_|\___|_|\_\__,_/_/\_\___| / \ '
	 ' | |		_________________________| | '
	 ' |_|	   |_________________________  O '
	 '									 | | '
	 '									 \ / '
	 '									  v  '
	 '										 '
'''''''''''''''''''''''''''''''''''''''''''''''''''

import itertools, sys, os
from datetime import datetime
from subprocess import *

def getkbest (k, values):
	error=(1,values[0])
	values.sort()
	for i in range(len(values)-k):
		maximum = values[i+k-1]
		minimum = values[i]
		if maximum == 0:
			e=0
		else:
			e = (maximum - minimum) / float(maximum) 
		if e < 0.05:
			return sum(values[i:i+k]) / float(k)
		if e < error[0]:
			error=(e,sum(values[i:i+k]) / float(k))
	return error[1]

def getConfig():
	if len(sys.argv) != 2:
		print "Wrong program call"
		sys.exit(0)

	if "tester.config.py" != sys.argv[1]:
		print "Couldn't find tester.config.py"
		sys.exit(0)

	try:args=open(sys.argv[1],"r").read()
	except:
		print "Couldn't open tester.config.py"
		sys.exit(0)
	return filecontent

def replaceInvalidChars(string, new):
	string.replace("bin/", "")
	string.replace("src/", "")
	string.replace("../","")
	invalid="<\|/>:?*\""
	for i in range(32):
		invalid+=chr(i)
	for c in invalid:
		string = string.replace(c, new)
	return string

try:args=eval(getConfig())
except:
	print "Wrong argument format, check tester.config.py"
	sys.exit(0)

if type(args) is list and len(args)>=4: pass
else:
	print "Wrong argument format, check tester.config.py"
	sys.exit(0)

run = args.pop()
if type(run) is tuple and len(run)==2 and run[0]=="custom":
	pass
elif run in ["serial", "omp", "mpi"]:
	pass
else:
	print "Verify run method, should be:"
	print "'serial', 'omp', 'mpi' or ('custom','<ex: ./>')"
	sys.exit(0)

kbest=args.pop()
if type(kbest) is not tuple or len(kbest)!=2 or kbest[0]<1 or kbest[1]<kbest[0]:
	print "Verify kbest arguments"
	sys.exit(0)

ylabel=args.pop() 

xlabel,xaxe = args.pop()
xaxe=map(str,xaxe)

curvelabel,curves = args.pop()
curves=map(str,curves)

pipes=""
if type(args[-1]) is tuple and args[-1][0]=="pipes":
	pipes=args.pop()[1]

#args[-1]=replaceInvalidChars(args[-1], "_")

args[0]=map(lambda x: [replaceInvalidChars(str(x),"_")], args[0])
while len(args)>1:
	args[0]=list(itertools.chain.from_iterable( map(lambda x:map(lambda v:x+[str(v)], args[1]), args[0]) ))
	args=[args[0]]+args[2:]
args=args[0]

count=1
total=len(args)*len(curves)*len(xaxe)*kbest[1]

try:os.makedirs("results")
except:pass

now=str(datetime.now())
now=now[11:19].replace(":","-") + "_" + now[:10]

try:os.makedirs("results/"+now)
except:pass

try:os.makedirs("results/"+now+"/csv")
except:pass
#try:os.makedirs("results/"+now+"/graph")
#except:pass
for combination in args:
	name="_".join(combination)
	
	csv = open("results/"+now+"/csv/"+name+".csv", "w")
	#graphPath = "results/"+now+"/graph/"+name+".png"
	for point in xaxe:
		csv.write(","+point)
	for curve in curves:
		csv.write("\n"+curvelabel+curve)
		for point in xaxe:'''''''''''''''''''''''''''''''''''''''''''''''''''
	 '										 '
	 '		 (_)	| |						 '
	 '  _ __  _  ___| | ____ ___  _____		 '
	 ' | '_ \| |/ __| |/ / _` \ \/ / _ \	 '
	 ' | |_) | | (__|   < (_| |>  <  __/  ^	 '
	 ' | .__/|_|\___|_|\_\__,_/_/\_\___| / \ '
	 ' | |		_________________________| | '
	 ' |_|	   |_________________________  O '
	 '									 | | '
	 '									 \ / '
	 '									  v  '
	 '										 '
'''''''''''''''''''''''''''''''''''''''''''''''''''

import itertools, sys, os
from datetime import datetime
from subprocess import *

def getkbest (k, values):
	error=(1,values[0])
	values.sort()
	for i in range(len(values)-k):
		maximum = values[i+k-1]
		minimum = values[i]
		if maximum == 0:
			e=0
		else:
			e = (maximum - minimum) / float(maximum) 
		if e < 0.05:
			return sum(values[i:i+k]) / float(k)
		if e < error[0]:
			error=(e,sum(values[i:i+k]) / float(k))
	return error[1]

def getConfig():
	if len(sys.argv) != 2:
		print "Wrong program call"
		sys.exit(0)

	if "tester.config.py" != sys.argv[1]:
		print "Couldn't find tester.config.py"
		sys.exit(0)

	try:args=open(sys.argv[1],"r").read()
	except:
		print "Couldn't open tester.config.py"
		sys.exit(0)
	return args

def replaceInvalidChars(string, new):
	string=string.replace("bin/", "").replace("src/", "").replace("../","")
	invalid="<\|/>:?*\""
	for i in range(32):
		invalid+=chr(i)
	for c in invalid:
		string = string.replace(c, new)
	return string

try:
args=eval(getConfig())
except:
	print "Wrong argument format, check tester.config.py"
	sys.exit(0)

if type(args) is list and len(args)>=6: pass
else:
	print "Wrong argument format, maybe there are elements missing, check tester.config.py"
	sys.exit(0)

run = args.pop()
if type(run) is tuple and len(run)==2 and run[0]=="custom":
	pass
elif run in ["serial", "omp", "mpi"]:
	pass
else:
	print "Verify run method, should be:"
	print "'serial', 'omp', 'mpi' or ('custom','<ex: ./>')"
	sys.exit(0)

kbest=args.pop()
if type(kbest) is not tuple or len(kbest)!=2 or kbest[0]<1 or kbest[1]<kbest[0]:
	print "Verify kbest arguments"
	sys.exit(0)

ylabel=args.pop() 

xdata = args.pop()
if type(xdata) is not tuple or len(xdata)!=3:
	print "Wrong x parameters"
	sys.exit(0)

xlabel,xaxe,xuse = xdata
xaxe=map(str,xaxe)
xuse=bool(xuse)

curve_data = args.pop()
if type(curve_data) is not tuple or len(curve_data)!=3:
	print "Wrong curve parameters"
	sys.exit(0)
curvelabel,curves,curveuse = curve_data
curves=map(str,curves)
curveuse=bool(curveuse)

pipes=""
if type(args[-1]) is tuple and args[-1][0]=="pipes":
	pipes=args.pop()[1]



#args[-1]=replaceInvalidChars(args[-1], "_")

args[0]=map(lambda x: [str(x)], args[0])
while len(args)>1:
	args[0]=list(itertools.chain.from_iterable( map(lambda x:map(lambda v:x+[str(v)], args[1]), args[0]) ))
	args=[args[0]]+args[2:]
args=args[0]

count=1
total=len(args)*len(curves)*len(xaxe)*kbest[1]

try:os.makedirs("results")
except:pass

now=str(datetime.now())
now=now[11:19].replace(":","-") + "_" + now[:10]

try:os.makedirs("results/"+now)
except:pass

try:os.makedirs("results/"+now+"/csv")
except:pass
#try:os.makedirs("results/"+now+"/graph")
#except:pass
for combination in args:
	name=replaceInvalidChars("_".join(combination),"_")
	
	csv = open("results/"+now+"/csv/"+name+".csv", "w")
	#graphPath = "results/"+now+"/graph/"+name+".png"
	for point in xaxe:
		csv.write(","+point)
	for curve in curves:
		csv.write("\n"+curvelabel+curve)
		for point in xaxe:
			tmp=[]
			for repetition in range(kbest[1]):
				if pipes!="": pstr = " | "+pipes
				else: pstr=""
				tempstr=""
				if combination[1:]!=[]: tempstr+=" ".join(combination[1:])
				if curveuse: tempstr+=" "+curve
				if xuse: tempstr+=" "+point
				print count,"of",total, "["+" ".join(["./"+combination[0] ]) + tempstr +pstr+"]"

				s=datetime.now()
				count+=1
				if run=="mpi" or run[0]=="custom":
					print "Run method:",str(run),", not yet supported"
					sys.exit(0)
				if run=="seq" or run=="omp":
					try:
						try:
							if run=="omp": os.environ["OMP_NUM_THREADS"]=point
						except: pass	

						executions = ["./"+combination[0] ]
						if combination[1:]!=[]: executions+=combination[1:]
						if curveuse: executions.append(curve)
						if xuse: executions.append(point)
						executions=[executions]
						if pipes!="": executions+=map(lambda x: x.strip().split(" "),pipes.split("|"))

						cmd=[]
						cmd.append (
							Popen ( executions[0], stdout=PIPE), stderr=PIPE )
						)
						for i in range (len(executions)-1):
							#cmd[i].wait()
							cmd.append (
								Popen ( executions[i+1], stdin=cmd[i].stdout, stdout=PIPE), stderr=PIPE )
							)
							cmd[i].stdout.close()
						cmd[-1].wait()
						try:
							c_printf = cmd[-1].communicate()[0]
							tmp.append(float(c_printf))
						except:
							print "Wrong program output. Expected float, got:"
							print c_printf
					except:
						print "Execution error: check if",combination[0],"exists"
				e=datetime.now()
				print "Total execution time:",e-s,"\n"
			try:
				v=getkbest(kbest[0],tmp)
				csv.write("," + str(v) )
			except:
				csv.write(",")
				print "Failed to calculate the kbest of the result values"
				print "Values:",tmp
	csv.close()
			tmp=[]
			for repetition in range(kbest[1]):
				if pipes!="": pipes = " | "+pipes
				print count,"of",total, "["+" ".join(["./"+combination[0] ]+combination[1:]+[curve, point])+pipes"]"
				s=datetime.now()
				count+=1
				if run=="mpi" or run[0]=="custom":
					print "Run method:",str(run),", not yet supported"
					sys.exit(0)
				if run=="seq" or run=="omp":
					try:
						try:
							if run=="omp": os.environ["OMP_NUM_THREADS"]=point
						except: pass	
						executions = [cmd]+ map(lambda x: x.strip().split(" "),pipes.split("|"))
						cmd=[]
						cmd.append (
							Popen ( executions[0], stdout=PIPE, stderr=PIPE )
						)
						for i in range (len(executions)-1):
							cmd.append (
								Popen ( executions[i+1], stdin=cmd[i].stdout, stdout=PIPE, stderr=PIPE )
							)
							cmd[i].stdout.close()
						cmd[-1].wait()
						try:
							c_printf = cmd[-1].communicate()[0]
							tmp.append(float(c_printf))
						except:
							print "Wrong program output. Expected float, got:"
							print c_printf
					except:
						print "Execution error: check if",combination[0],"exists"
				e=datetime.now()
				print "Total execution time:",e-s,"\n"
			try:
				v=getkbest(kbest[0],tmp)
				csv.write("," + str(v) )
			except:
				csv.write(",")
				print "Failed to calculate the kbest of the result values"
				print "Values:",tmp
	csv.close()