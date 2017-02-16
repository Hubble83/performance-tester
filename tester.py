#import matplotlib
import itertools, sys, subprocess, os
from datetime import datetime

def kbest (k, values):
	error=(1,values[0])
	values.sort()
	for i in range(len(values)-k):
		maximum = values[i+k-1]
		minimum = values[i]
		e = (maximum - minimum) / float(maximum) 
		if e < 0.05:
			return sum(values[i:i+k]) / float(k)
		if e < error[0]:
			error=(e,sum(values[error[1]:error[1]+k]) / float(k))
	return error[1]

if len(sys.argv) != 2:
	print "Wrong program call"
	sys.exit(0)

if "tester.config.py" not in sys.argv[1]:
	print "Couldn't find tester.config.py"
	sys.exit(0)

try:args=open(sys.argv[1],"r").read()
except:
	print "Couldn't find tester.config.py"
	sys.exit(0)
try:args=eval(args)
except:
	print "Wrong argument format, check tester.config.py"
	sys.exit(0)

if type(args) is list and len(args)>=3: pass
else:
	print "Wrong argument format, check tester.config.py"
	sys.exit(0)

kbest=args.pop()
if type(kbest) is not list or len(kbest)!=2 or kbest[0]<1 or kbest[1]<kbest[0]:
	print "Verify kbest arguments"
	sys.exit(0)

ylabel=args.pop() 

xlabel,xaxe = args.pop().items()[0]
xaxe=map(str,xaxe)

curvelabel,curves = args.pop().items()[0]
curves=map(str,curves)

args[0]=map(lambda x: [str(x)], args[0])
while len(args)>1:
	args[0]=list(itertools.chain.from_iterable( map(lambda x:map(lambda v:x+[str(v)], args[1]), args[0]) ))
	args=[args[0]]+args[2:]
args=args[0]

count=0
total=len(args)*len(curves)*len(xaxe)*kbest[1]

try:os.makedirs("results")
except:pass
try:os.makedirs("results/csv")
except:pass
#try:os.makedirs("results/graph")
#except:pass
now=str(datetime.now())
now=now[11:19].replace(":","-") + "_" + now[:10]
try:os.makedirs("results/csv/"+now)
except:pass
#try:os.makedirs("results/graph/"+now)
#except:pass

for combination in args:
	name="_".join(combination)
	
	csv = open("results/csv/"+now+"/"+name+".csv", "w")
	#graphPath = "results/graph/"+now+"/"+name+".png"
	for point in xaxe:
		csv.write(","+point)
	for curve in curves:
		csv.write("\n"+curve)
		for point in xaxe:
			sp=[]
			tmp=[]
			for repetition in range(kbest[1]):
				print count,"of",total
				s=datetime.now()
				count+=1
				try:			
					execution = subprocess.Popen(
						["./"+combination[0] ]+combination[1:]+[curve, point],
						stdout=subprocess.PIPE,
						stderr=subprocess.PIPE
					) 
					execution.wait()
					try:
						c_printf = execution.stdout.read().decode("ascii").strip()
						tmp.append(float(c_printf))
					except:
						print "Wrong program output, must be a single integer!"
				except:
					print "Execution error: check if",combination[0],"exists"
				e=datetime.now()
				print "Test total time:",e-s,"\n"
			try:
				v=kbest(kbest[0],tmp)
				csv.write("," + str(v) )
				sp.append(v)
			except:
				csv.write(",")
				print "Failed to calculate the kbest of the result values"
	csv.close()