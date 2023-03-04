from rembg import remove

input = 'cat.jpg'
output = 'cat_nobg.jpg'

with open(input, 'rb') as i:
    with open(output,'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)