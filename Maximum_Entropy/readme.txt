1.) Run Megam_Extract.py to extract data for One vs Rest Approach as follows:
	
	python3 Megam_Extract.py /path/to/tarin_data/

2.) To extract data for Multi class approach run Megam_Extract_Multi.py

	python3 Megam_Extract_Multi.py /path/to/tarin_data/

3.) To generate the weights use the following command:

	for binary: ./megam.opt -fvals binary small2 > weights

	for multiclass: ./megam.opt -fvals multiclass small2 > weights

	for multitron: ./megam.opt -fvals multitron small2 > weights

4.) To predict use the commands:

	for binary: ./megam.opt predict binary small2 > result

	for multiclass: ./megam.opt predict multiclass small2 > result

	for multitron: ./megam.opt predict multitron small2 > result

---------------------------------------------------------------------------------------------

Sample Output folder has samples of 
1.) weights
2.) Predicted Results
3.) Processed Data