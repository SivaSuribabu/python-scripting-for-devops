# python-scripting-for-devops
This repository cotains the python scripting notes and exampls.


bash vs python

bash :
1. uses command line interfcae
2. environment variables configuration
3. text processing
4. system administration
5. rapid prototype : for immediate tasts execution

python:
1. cross platform compatability.
2. api integration
3. error handiling
4. reusabel code
5. advanced data processing
6. complex logic


DATA TYPES 

numerical data types : 
1. integer
2. float
3. complex

sequemce and mapping : 
1. list  my_list = [1,2,3,4,5]
2. dict  my_dict = (1,2,3,4,5)
3. sets  my_set = {1,2,3,4,5}
4. boolean my_boolean = true or false


inbuilt functions

name.split()
length = len(name)
upper = name.upper()
lower = name.lower()

regular expressions (regex) :
Regular expressions are use for anyalysing the particular pattern in log files such as errors.log


NAMING CONVENTIONS OF VARIABLES 

1. always declare the variable names in the lower case only
2. use seperators like (ec2_instance_name = "project_xyz")  -- this is snakcaing format
3. using camle casr ( Ec2InstanceName = "ProjectAbc")  -- this is camle casing format
4. make variables as Descriptive as possible.


List & Tuples :

Lists are started with []
Lists are mutable 
we can perform the append and remove the actions on lists
example : we can list-out the s3 buckets in the aws region 


tuples are startedwith ()
tuples are immutable 
we cannot perform the append and remove action on tuples as they are immutable
example : Listing the number of aws admins