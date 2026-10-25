# Exercise 1
def save_scores(names, scores, filename):
    file = open(filename,"w")
    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
    file.close()
    pass

# Exercise 2
def average_score(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    
    total = 0
    count = 0
    for i in range(len(lines)):
        line = lines[i].strip()
        if line != "":
            parts = line.split(",")
            total += int(parts[1])
            count += 1
            
    if count == 0:
        return 0
        
    return round(total / count, 1)
    pass

# Exercise 3
def filter_passed(source, destination, pass_mark):
    file = open(source, "r")
    lines = file.readlines()
    file.close()
    
    passed_lines = []
    count = 0
    for i in range(len(lines)):
        line = lines[i].strip()
        if line != "":
            parts = line.split(",")
            score = int(parts[1])
            if score >= pass_mark:
                passed_lines.append(line)
                count += 1
                
    dest_file = open(destination, "w")
    for i in range(len(passed_lines)):
        dest_file.write(passed_lines[i] + "\n")
    dest_file.close()
    
    return count
    pass

# Exercise 4
def replace_word(filename, old_word, new_word):
    file = open(filename, "r")
    content = file.read()
    file.close()
    
    count = content.count(old_word)
    new_content = content.replace(old_word, new_word)
    
    file = open(filename, "w")
    file.write(new_content)
    file.close()
    
    return count
    pass

# Exercise 5
def remove_line(filename, line_number):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    
    if line_number < 1:
        return False
    if line_number > len(lines):
        return False
        
    file = open(filename, "w")
    for i in range(len(lines)):
        if i != line_number - 1:
            file.write(lines[i])
    file.close()
    
    return True
    pass
