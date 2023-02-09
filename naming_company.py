# You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

# Choose 2 distinct names from ideas, call them ideaA and ideaB.
# Swap the first letters of ideaA and ideaB with each other.
# If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
# Otherwise, it is not a valid name.
# Return the number of distinct valid names for the company.
from collections import defaultdict

ideas = ["coffee","donuts","time","toffee"]

def get_valid_ideas(ideas):
  idea_dict = defaultdict(set)
  for idea in ideas:
    idea_dict[idea[0]].add(idea)

  keys = list(idea_dict.keys())
  result = []
  for i in range(len(keys)):
    for j in range(i+1, len(keys)):
      for word1 in idea_dict[keys[i]]:
        word1 = keys[j] + word1[1:] 
        if word1 in idea_dict[keys[j]]: continue
        for word2 in idea_dict[keys[j]]:
          word2 = keys[i] + word2[1:] 
          if word2 in idea_dict[keys[i]]: continue 
          result.append(word1 + ' '+ word2)
          result.append(word2 + ' '+ word1)
  return result

res = get_valid_ideas(ideas)
print(ideas)
print(len(res), res)

def count_valid_names(ideas):
  idea_dict = defaultdict(set)
  for idea in ideas:
    idea_dict[idea[0]].add(idea[1:])

  keys = list(idea_dict.keys())
  result = 0
  for i in range(len(keys)):
    for j in range(i+1, len(keys)):
      mutuals = len(idea_dict[keys[i]] & idea_dict[keys[j]])
      l1 = len(idea_dict[keys[i]]) - mutuals
      l2 = len(idea_dict[keys[j]]) - mutuals
      result += l1 * l2 * 2
  return result
  

print(count_valid_names(ideas))

