class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for dir in path.split("/"):
            if dir == "" or dir == ".": continue
            if dir == "..":
                if stack: stack.pop()
            else:
                stack.append(dir)
        
        return "/" + "/".join(stack)


# # path = "/home/"
# path = "/home//foo/"
# # path = "/home/user/Documents/../Pictures"
# # path = "/.../a/../b/c/../d/./"
# # path = "/../"
# res = []
# element = ""
# if path.endswith("/"):
#     path = path[:-1]
# print(path)
# l = 0
# for r in range(1, len(path)):
#     if path[r] == "/":
#         if path[l:r] == "/..":
#             res.pop(-1)
#             l = r+1
#             continue
#         elif path[l:r] == "/":
#             continue
#         res.append(path[l:r])
#         l = r
# if l != len(path)-1:
#     res.append(f"/{path[l:len(path)]}")
# print(res)
        
            
        

# # for i in range(len(path)):
# #     if element:
# #         if len(element) > 1 and path[i] == "/":
# #             res.append(element)
# #             element = "/"
# #         elif len(element) == 1 and path[i] == "/":
# #             continue
# #         elif path[i] == "." and path[i+1] == ".":
# #             if not res:
# #                 continue
# #             res.pop(-1)
# #             element = ""
# #         elif path[i].isalpha():
# #             element += path[i]            
# #     elif path[i] == "/":
# #         element += "/"
# # if element:    
# #     res.append(element)
# # print(res)
        
      
        
#     # if element:
#     #     if path[i].isalpha():
#     #         element += path[i]
#     #     else:
#     #         res.append(element)
    
