def bracket_matcher(input):
  open_brackets = ['[', '(', '{']
  close_brackets = [']', ')', '}']
  bracket_stack = []
  for char in input:
    if char in open_brackets:
      bracket_stack.append(char)
    if char in close_brackets:
      index = close_brackets.index(char)
      if len(bracket_stack) == 0:
        return False
      elif bracket_stack[-1]== open_brackets[index]:
        bracket_stack.pop()
      else: 
        return False
  if len(bracket_stack) == 0: 
    return True
  else: 
    return False








# print(bracket_matcher('abc(123)'))
# # returns true

# print(bracket_matcher('a[b]c(123'))
# # returns false -- missing closing parens

# print(bracket_matcher('a[bc(123)]'))
# # returns true

# print(bracket_matcher('a[bc(12]3)'))
# # returns false -- improperly nested

# print(bracket_matcher('a{b}{c(1[2]3)}'))
# # returns true

# print(bracket_matcher('a{b}{c(1}[2]3)'))
# # returns false -- improperly nested

# print(bracket_matcher('()'))
# # returns true

# print(bracket_matcher('[]]'))
# # returns false - no opening bracket to correspond with last character

# print(bracket_matcher('abc123yay'))
# # returns true -- no brackets = correctly matched



from solution import bracket_matcher

print("it should be True",  bracket_matcher('abc(123)'))

# returns true

print("it should be False", bracket_matcher('a[b]c(123'))
# returns false -- missing closing parens

print("it should be True", bracket_matcher('a[bc(123)]'))
# returns true

print("it should be False", bracket_matcher('a[bc(12]3)'))
# returns false -- improperly nested

print("it should be True", bracket_matcher('a{b}{c(1[2]3)}'))
# returns true

print("it should be False", bracket_matcher('a{b}{c(1}[2]3)'))
# returns false -- improperly nested

print("it should be True", bracket_matcher('()'))
# returns true

print("it should be False", bracket_matcher('[]]'))
# returns false - no opening bracket to correspond with last character

print("it should be True", bracket_matcher('abc123yay'))
# returns true -- no brackets = correctly matched