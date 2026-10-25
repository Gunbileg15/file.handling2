# Exercise 1
def save_scores(names, scores, filename):
    file = open(filename, "w")
    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
    file.close()
# Exercise 2
def calculate_average(filename):
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
# Exercise 3
def filter_passing_students(source,destination,pass_mark):
    src = open(source, 'r')
    lines = src.readlines()
    src.close()
    
    passing_students = []
    pass_count = 0
    
    for line in lines:
        if not line.strip():
            continue
            
        name, score_str = line.strip().split(',')
        score = int(score_str)
        
        if score >= pass_mark:
            pass_count += 1
            passing_students.append(f"{name},{score}\n")
            
    file = open(destination, 'w')
    file.writelines(passing_students)
    file.close()
    
    return pass_count

# Exercise 4
def replace_word(filename, old_word, new_word):
    # Write your code here
    pass

# Exercise 5
def remove_line(filename, line_number):
    # Write your code here
    pass
