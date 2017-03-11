#############################################################################################
#																							#
#	Usage:																					#
#	[																						#
#		[executables],													!					#
#		[variations],													OPTIONAL			#
#		...,															OPTIONAL			#
#		("dstat", True/False)											OPTIONAL			#
#		("pipes", "pipeline to process executable stdout")				OPTIONAL			#
#		("curve label", [curves], pass_as_exec_arg? ),					!					#
#		("x label" :[curve points], pass_as_exec_arg? ),				!					#
#		"y label",														!					#
#		(k, repetitions)												!					#
#		"execution_method": omp | mpi | (custom,"<ex: mpirun -np 8>")	!					#
#	]																						#
#																							#
#############################################################################################

[
	[
		"bin/omp/gnu/cg.C.x",
		"bin/omp/gnu/is.C.x",
		"bin/omp/gnu/ep.C.x",

		"bin/omp/intel/cg.C.x",
		"bin/omp/intel/is.C.x",
		"bin/omp/intel/ep.C.x"
	],
	( "dstat", True ),
	( "pipes", "awk {for(i=1;i<NF;i++){if($i==\"seconds\"){print$5}}}"),
	( "-----", [0], False),
	( "Number of threads", [8,16,24,32,40,48], False ),
	"Speedup",
	( 1, 1 ),
	("omp")
]