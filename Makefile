# This is a testing file for the OSFTA dev. team
# This shows example usages of the OSFTA program

# Intended usage:
# [python] OSFTA.py [path_to_source_tree] [configFilename]


all: buildingManagerDev

buildingManagerDev:
	python OSFTA.py /Source/Inputs/BuildingController/ config.txt