import math

path = './tools/trainermoney_orig.c'
mod = 2

output = []

with open(path) as f:
    with open('./src/trainermoney.c','w') as newf:
        for l in f:
            if '.class' in l:
                elems = l.strip().split(' ')
                num = math.floor(int(elems[6]) * mod)
                elems[6] = str(num)
                new_line = ''
                for s in elems:
                    new_line = new_line + ' ' + s
                new_line += '\n'
                output.append(new_line)
            else:
                output.append(l)
        newf.writelines(output)
        