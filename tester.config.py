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
	[
		"sequential",
		"omp_active_wait",
		"omp_mutex",
		"pthreads_active_wait",
		"pthreads_mutex"
	],
	[4096,65536],
	{ "Chunk size = " : [2,8,32,128,512,2048] },
	{ "Number of threads" : range(2,41,2) },
	"Speedup",
	[3,5]
]

#############################################################################################
#																							#
#	Generates all combinations of elements from each list (program output must be integer)	#
#																							#
#	First call: ./sequential 4096 2 2														#
#																							#
#############################################################################################