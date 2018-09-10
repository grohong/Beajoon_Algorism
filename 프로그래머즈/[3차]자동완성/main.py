# # Node 구현
# class Node():
#     def __init__(self, key, data=None):
#         self.key = key
#         self.data = data
#         self.children = {}
#
# # Trie tree 구현
# class Trie():
#     def __init__(self):
#         self.head = Node(None)
#
#     def insert(self, string):
#         curr_node = self.head
#
#         for char in string:
#             if char not in curr_node.children.keys():
#                 curr_node.children[char] = Node(char)
#
#             curr_node = curr_node.children[char]
#
#         curr_node.data = string
#
#     def starts_with(self, prefix):
#         curr_node = self.head
#         result = []
#         subtrie = None
#
#         for char in prefix:
#             if char in curr_node.children.keys():
#                 curr_node = curr_node.children[char]
#                 subtrie = curr_node
#             else:
#                 return None
#
#         # bfs을 이용하여 탐색
#         queue = list(subtrie.children.values())
#
#         while queue:
#             curr = queue.pop()
#             if curr.data != None:
#                 result.append(curr.data)
#                 # 해당 문제에서 시간을 최소화 하기 위해 2개 이상의 경우가 나왔을때는 return // 시간은 5110.11ms -> 3684.36ms 만큼 감
#                 if len(result) > 1:
#                     return result
#
#             queue += list(curr.children.values())
#
#         return result
#
#     def starts_with_index(self, prefix):
#         curr_node = self.head
#         result = []
#         subtrie = None
#
#         for char in prefix:
#             if char in curr_node.children.keys():
#                 curr_node = curr_node.children[char]
#                 subtrie = curr_node
#             else:
#                 return None
#
#         queue = list(subtrie.children.values())
#
#         while queue:
#             curr = queue.pop()
#             if curr.data != None:
#                 result.append(curr.data)
#                 if len(result) > 1:
#                     return result
#
#             queue += list(curr.children.values())
#
#         return result
#
# def solution(words):
#     answer = 0
#
#     trie = Trie()
#
#     # tree 완성
#     presearch = []
#     for word in words:
#         trie.insert(word)
#
#     words = sorted(words, key=len, reverse= True)
#
#     for word in words:
#         if word in presearch:
#             break
#
#         # word의 부분
#         tmp = ''
#         for string in word:
#             tmp += string
#
#             if tmp in words:
#                 answer += len(tmp)
#                 presearch.append(tmp)
#                 print(tmp)
#                 print(len(tmp))
#
#             prefix = trie.starts_with(tmp)
#             if len(prefix) == 1 and tmp in presearch:
#                 # "warrior", "war" 경우에 tmp = war일 경우 warr가 정답이기 때문에 len(tmp)+1 추가
#                 answer += len(tmp)+1
#                 print(tmp)
#                 print(len(tmp)+1)
#                 break
#             elif len(prefix) == 1 and tmp not in presearch:
#                 # "word", "world" 경우 tmp = worl이기 때문에 +1을 생략한것이 정답
#                 answer += len(tmp)
#                 print(tmp)
#                 print(len(tmp))
#                 break
#
#
#     return answer

from collections import deque

def solution(words):
    answer = 0

    
    sort_words = sorted(words)
    print(sort_words)

    return answer


# print(solution(["go","gone","guild"]))
print(solution(["warrior", "war", "word", "world"]))