# This is a testing file for the OSFTA dev. team
# This shows example usages of the OSFTA program

# Intended usage:
# [python] OSFTA.py [path_to_source_tree] [configFilename]


all: buildingManagerDev

buildingManagerDev:
	python OSFTA.py Inputs/BuildingController/ config.txt



# Makefile to invoke the test suite
# The default target, which will be run when you just type 'make'
# From ChatGPT
# Makefile to invoke the test suite

test:
	@echo "Running tests..."
	python -m unittest discover -s Tests -t . -p "Test*.py" -v
