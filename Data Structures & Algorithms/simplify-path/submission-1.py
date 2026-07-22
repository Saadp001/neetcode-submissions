class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()        # go up one directory
            elif part == "." or part == "":
                continue               # skip current dir and empty strings
            else:
                stack.append(part)    # valid directory name, push

        return "/" + "/".join(stack)