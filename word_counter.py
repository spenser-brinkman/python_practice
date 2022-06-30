import sys
import re

# Validate that only one argument is provided,
# and that the argument is a .txt file with a name at least one character long
if len(sys.argv) > 2 or not re.search("^.+\.(txt)$", sys.argv[1]):
  print("Invalid options. Please provide an input .txt file to read from.")
  quit()

input_filename = sys.argv[1]
dottxt_index = input_filename.find('.txt')
output_filename = input_filename[:dottxt_index] + "-count.txt"

input_file = open(input_filename, 'r').read()
output_file = open(output_filename, 'w')

word_list = input_file.split()
word_set = set(word_list)
output_file.write(f"Total words: {len(word_list)}\n")
output_file.write(f"Unique words: {len(word_set)}\n\n")
word_counts = {}
for word in word_set:
  word_counts[word] = input_file.count(word)

sorted_word_counts = {}
sorted_keys = sorted(word_counts, key=word_counts.get, reverse=True)

for w in sorted_keys:
    sorted_word_counts[w] = word_counts[w]

for word_count in sorted_word_counts.items():
  output_file.write(f"{word_count[0]} - {word_count[1]}\n")