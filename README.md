# tame_of_thrones
A command line app to show the working of tame of thrones.  

This command line app was developed and tested in the below environment:  

OS: macOs Catalina    

Python Version: 3.6.4 

__________________________  

How to run the test cases:  
	cd into the parent folder of this project (i.e, 'tame_of_thrones') and run the below command.   
		python3.6 -B -m unittest discover -s tests -t .    
	To check test coverage, run the below commands in parent foler (needs 'coverage' to be installed):
	    coverage run -m unittest discover
		coverage report -m
	Current test coverage is 97%
__________________________  

How to run the program:  
	Run the geektrust.py file in tame_of_thrones folder (tame_of_thrones/geektrust.py)
	Example:
        pip3 install -r ../requirements.txt  
		python3.6 -m geektrust <absolute_path_to_input_file>

__________________________  

Continuous Integration:  
	CircleCi along with GitHub are used to handle dependencies, build, test and deploy the changes.  
	When a change is made and pushed, it automatically triggers the test and build processes.  

	You can find this project in GitHub here: https://github.com/sh3ll3y/tame_of_thrones   
	Recent build and test jobs in CircleCI have been successful and they can be seen here: https://circleci.com/gh/sh3ll3y/tame_of_thrones