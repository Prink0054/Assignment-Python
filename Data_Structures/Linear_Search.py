# def linearSearch(myItem,myList):
#     found = False
#     position = 0
#     while position < len(myList) and not found:
#         if myList[position] == myItem:
#             found = True
#         position = position + 1
#     return found
#
# if __name__ == "__main__":
#     shopping = ["apples" , "bananas" , "chocolate" , "pasta"]
#     item = input("Enter item to search")
#     isitfound =  linearSearch(item,shopping)
#     if isitfound:
#         print("found")
#     else:
# #         print("not found")
#
# l = ["apple" , "orange" , "mango"]
# item = input("Enter item to search")
# for i in l :
#      if i == item:
#          print("found")
#          break
#      elif i = i+1:
#          print("not found")
#          break
#
# f = open("text.txt" ,"r")
# # print(f)
# # print(f.read())
# # print(f.readline())
# # print(f.readline())
# print(f.readlines())
# l = ["a\n", "b\n", "c\t"]
# f = open("text.txt" , "a")
# f.writelines(l)
#



f = open("text.txt" ,"r")
print(f.read(5))
print(f.tell())
f.seek(1,2)
print(f)



print("hiiiii")





# with open("text.txt","r") as f:
#         print(f.read())