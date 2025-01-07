words = ["mass","as","hero","superhero"]

r=' '.join(words)
print([i for i in words if r.count(i)>1])


# normal_pointer = 0
# substring_pointer = 1
# substring_indexes = []

# while normal_pointer <= len(words)-1:
#     if substring_pointer not in substring_indexes and substring_pointer != normal_pointer:
#         if words[substring_pointer] in words[normal_pointer]:
#             substring_indexes.append(substring_pointer)
#     substring_pointer += 1
#     if substring_pointer >= len(words):
#         normal_pointer += 1
#         while normal_pointer in substring_indexes:
#             normal_pointer += 1
#         substring_pointer = 1
            
    
# print([words[i] for i in substring_indexes])
      
