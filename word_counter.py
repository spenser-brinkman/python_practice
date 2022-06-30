import sys
import re

def count_words(input_file):
  word_set = set(input_file.split())
  counts = {}
  for word in word_set:
    counts[word] = input_file.count(word)

  sorted_counts = {}
  sorted_keys = sorted(counts, key=counts.get, reverse=True)

  for w in sorted_keys:
      sorted_counts[w] = counts[w]

  return sorted_counts

# Validate that only one argument is provided,
# and that the argument is a .txt file with a name at least one character long
if len(sys.argv) > 2 or not re.search("^.+\.(txt)$", sys.argv[1]):
  print("Invalid options. Please provide an input .txt file to read from.")
  quit()

input_filename = sys.argv[1]
txt_index = input_filename.find('.txt')
output_filename = input_filename[:txt_index] + "-count.txt"

input_file = open(input_filename, 'r').read()
input_str = input_file.split()

word_counts = count_words(input_file)
print(word_counts)

output_file = open(output_filename, 'w')

