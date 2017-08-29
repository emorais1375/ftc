class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def top(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

try:
    str = input().replace(" ", "")
    stack = Stack()

    result = True
    for ch in str:
        if(ch == '(' or ch == '[' or ch == '{'):        
            stack.push(ch)
            continue

        if stack.size() == 0:
            result = False
            break
        elif(stack.top() == '(' and ch == ')'):
            stack.pop()        
        elif(stack.top() == '[' and ch == ']'):
            stack.pop()        
        elif(stack.top() == '{' and ch == '}'):
            stack.pop()        
        else:
            result = False
            break

    if result and stack.size() == 0 and len(str) > 0:        
        print(True)
    else:
        print(False)

except:
    print(True)

