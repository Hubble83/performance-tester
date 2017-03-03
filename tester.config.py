#############################################################################################
#																							#
#	Usage:																					#
#	[																						#
#		[executables],											!							#
#		[variations],											OPTIONAL					#
#		...,													OPTIONAL					#
#		("tests", "tests with other tools")						OPTIONAL					#
#		("pipes", "pipeline to process executable stdout")		OPTIONAL					#
#		("curve label", [curves], pass_as_exec_arg? ),			!							#
#		("x label" :[curve points], pass_as_exec_arg? ),		!							#
#		"y label",												!							#
#		(k, repetitions)										!							#
#		"execution_method"										!							#
#	]																						#
#																							#
#############################################################################################

[
	# [executable_files]
	[
		#"bin/omp/gnu_4.9.0_O2/cg.C.x",
		"bin/mpi/openmpi_eth_1.8.4_O2/cg.C.x"
	],
	
	# optional: adicional tests, may need multiple tools
	# use dstat to get cpu / mem / net... ?
	( "dstat", True ),
	# optional: pipe the stdout to...(CAUTION, NOT SAME AS BASH)
	# use | for more pipes, use space ONLY to separate argumens (can't use even inside strings) 
	( "pipes", "awk {for(i=1;i<NF;i++){if($i==\"seconds\"){print$5}}}"),
	# (line_label, [line_values], pass_as_argument?)
	( "-", [1], False),
	# (x_label, [x_values], pass_as_argument?) -> in openMP/MPI must be threads/processes
	( "Number of processes", [8,16,32,48], False ),
	# "y_label"
	"Speedup",
	# kbest (k,tests)
	( 3, 8 ),
	# run type ( "serial", "omp", "mpi", ("custom",["./test", "-flag", ...]) )
	#"omp"
	("custom",["mpirun", "-np", "48", "--map-by", "node"])
]