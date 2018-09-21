rows = 8
pyramid_row = []
def pyramid():
    for i in range(rows):
        i = i + 1
        pyramid_row.append( (" " * (rows-i)) +  ("*" * ((i*2) - 1)) + (" " * (rows-i)))
        
    return "\n".join(pyramid_row)

print(pyramid())