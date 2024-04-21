import re

# Example Python code block with a comment
code = 
'''
@id SatelliteController
@failure-probability 0.07
@dependencies [GyroscopeController AND ThrusterController]
'''



# Python regular expression pattern to match block comments enclosed by triple single quotes
pythonCommentPattern = r"'''(.*?)'''"

# Applying the re.DOTALL flag to capture multiline strings
blockComments = re.findall(pythonCommentPattern, code, re.DOTALL)

if not blockComments:
    print("No Python-style block comments found.")
else:
    for comment in blockComments:
        print("Found Python block comment:", comment.strip())

# Return the block comments or None if not found
print(blockComments) if blockComments else None
