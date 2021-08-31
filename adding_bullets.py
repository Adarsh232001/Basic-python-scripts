import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')

# loop through all indexes for "lines" list
for i in range(len(lines)): 
    # add star to each string in "lines" list
    lines[i] = '* ' + lines[i] 
    text = '\n'.join(lines)
    
pyperclip.copy(text)
