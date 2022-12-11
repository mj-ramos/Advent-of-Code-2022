import re
import sys

def parse_input():
    fs = {'/': {'files': [], 'size' : 0}}
    accessed_dirs = []

    with open('inputs/input7.txt') as f:
        for line in f.readlines():
            if m:=re.match('\$ cd ([a-zA-Z1-9-_./]+)',line):
                current_dir = m.group(1)
                if current_dir == '..':
                    accessed_dirs.pop()
                else:
                    accessed_dirs.append(current_dir)
                
                if current_dir:='/'.join(accessed_dirs)[1:] not in fs:
                    fs[current_dir] = {'files': [], 'size':0}
                
            elif m:=re.match('dir ([a-zA-Z1-9-_./]+)',line):
                dir = current_dir + '/' + m.group(1) if current_dir!='/' else current_dir + m.group(1)
                if dir not in fs:
                    fs[dir] = {'files': [], 'size':0}

            elif m:=re.match('(\d+) ([a-zA-Z1-9-_./]+)',line):
                size = int(m.group(1))
                file = m.group(2) 
                if (size,file) not in fs[current_dir]['files']:
                    fs[current_dir]['files'].append((file,size))
                    fs[current_dir]['size'] += size

    return fs

def part_one(fs):
    dirs_size_under = []
    for dir,_ in fs.items():
        size_dir = 0      
        for dir1,info1 in fs.items():
            if dir1.startswith(dir):
                size_dir += info1['size']
                if size_dir>100000:
                    break
        if size_dir<100000:
            dirs_size_under.append(size_dir)

    return sum(dirs_size_under)

        
def part_two(fs):
    total_space = sum([dir['size'] for dir in fs.values()])
    space_to_free = 30000000 - (70000000 - total_space)
    min_space = sys.maxsize
    
    for dir,_ in fs.items():
        size_dir = 0
        for dir1,info1 in fs.items():
            if dir1.startswith(dir):
                size_dir += info1['size']
        
        if size_dir>=space_to_free and size_dir<min_space:
            min_space = size_dir
    
    return min_space

#--------------------------------------------------

fs = parse_input()
print(part_one(fs),part_two(fs)) #Right answers : 1886043 3842121