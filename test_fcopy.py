import fcopy

def check_content_equality():
    message = ""
    with open("data/input1.txt",'rt') as myFile:
        line = myFile.readline()

    fcopy_message = fcopy.read_source()
    if line == fcopy_message:
        return True
    else:
        return False

print("testing check_content_equality, expected True, got: " + str(check_content_equality()))