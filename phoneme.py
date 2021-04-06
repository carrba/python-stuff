#!/usr/bin/env python3.6

ph=input("Enter phoneme\n")

print(ph)

# grep /usr/share/words

with open('/usr/share/dict/words') as f:
  for line in f:
    if ph in line:
      if "'" not in line:
        print(line.strip())
