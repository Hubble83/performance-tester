#############################################################################################
#																							#
#	Usage:																					#
#	[																						#
#		[executables],																		#
#		[optional variations],																#
#		...,																				#
#		{"curve label" :[curves]},															#
#		{"x label" :[curve points]},														#
#		"y label",																			#
#		[k, repetitions]																	#
#		["flags"]																			#
#	]																						#
#																							#
#############################################################################################

[
	# [executable_files]
	[
		"bin/omp/gnu_4.9.0_02/ep.B.x",
	],
	
	# optional: pipe the output (CAUTION, NOT SAME AS BASH)
	# use | for pipes, use space ONLY to separate argumens (not even inside strings) 
	("pipes", "awk {for(i=1;i<NF;i++){if($i==\"CPU\"){print$4}}}")
	# {line_label: [line_values]}
	( "-" : [1] ),
	# {x_label: [x_values]} -> in openMP must be threads
	( "Number of threads" : [48]),
	# "y_label"
	"Speedup",
	# kbest (k,tests)
	(1,1),
	# run type ( "serial", "omp", "mpi", ("custom",["./test", "-flag", ...]) )
	"omp"
]

#############################################################################################
#																							#
#	Generates all combinations of elements from each list (program output must be integer)	#
#																							#
#	First call: ./sequential 4096 2 2														#
#																							#
#############################################################################################