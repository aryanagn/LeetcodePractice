#LeetCode 71 -- MEDIUM Difficulty

#Approach
'''Empty list to store files or directories'''
'''split path string into list of directories and file names at each occurrence of'/' '''
'''iterate over each element in path, also each elem represents directory name or file name'''
'''check if dirOrFiles not empty and if curr elem is equal to '..'(parent directory) if both true, remove or pop last(dirOrFile) '''
'''elseif curr element 'elem' not equal to '.' , "", or ".." if true, elem represents valid dirOrFile, so append it'''

#Complexity: 
'''Time Complexity: O(n)'''
'''Space Complexity: O(n)'''


def simplifyPath(self, path: str) -> str:
    dirOrFiles = []
    path = path.split("/")
    for elem in path:
        if dirOrFiles and elem == "..":
            dirOrFiles.pop()
        elif elem not in [".", "", ".."]:
            dirOrFiles.append(elem)
    return "/" + "/".join(dirOrFiles)