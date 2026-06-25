def readlines(filename: str):
    '''
    This function takes a filname (str) as input and returns a list of 
    strings representing the data stored within that file.
    '''
    with open(filename, 'r') as file:
        return file.readlines()
    

def writelines(filename: str, content: str):
    '''
    This function takes a filename (str) and some content (str) as
    input and write the content to that file.
    '''
    with open(filename, 'w') as file:
        file.writelines(content)