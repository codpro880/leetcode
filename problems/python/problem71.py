class Solution:
    def simplifyPath(self, path):
        path = self.remove_double_slash(path)
        path = self.remove_single_dirs(path)
        path = self.go_back_dirs(path)
        path = self.remove_trailing_slash(path)
        return path
    
    def remove_double_slash(self, path):
        return path.replace("//", "/")
    
    def remove_single_dirs(self, path):
        if len(path) > 2:
            return path.replace("/./", "/")
        else:
            return path
        
    def go_back_dirs(self, path):
        if ".." not in path:
            return path
        else:
            dirs = path.split("/")
            for i in range(len(dirs)):
                if dirs[i] == "..":
                    dirs[i-1] = ""
                    dirs[i] = ""
                    break
            dirs = [dirs[0]] + [d for d in dirs[1:] if d]
            return self.go_back_dirs("/".join(dirs))
        
    def remove_trailing_slash(self, path):
        if len(path) > 1:
            result = path[:-1] if path[-1] == "/" else path
            return result
        else:
            return path
