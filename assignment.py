# You can remove 'pass' if you written code in the function
# Exercise 1

def save_scores(names, scores, filename):
    file = open(filename,"w")
    for i in range(len(names)):
        file.write(f"{names[i]},{scores[i]}\n")
    file.close()
# Exercise 2
def average_score(filename):
    total_score = 0
    student_count = 0
    file = open(filename, 'r')
    for line in file:
        line = line.strip()
        if line:
            parts = line.split(',')
            score = int(parts[1])
            total_score += score
            student_count += 1
    file.close()
    if student_count == 0:
        return 0
    average = total_score / student_count
    return round(average,1)
# Exercise 3
def filter_passing_students(source,destination,pass_mark):
    src = open(source, 'r')
    lines = src.readlines()
    src.close()
    passing_students = []
    pass_count = 0
    for line in lines:
        if line.strip():
            continue
        name, score_str = line.strip().split(',')
        score = int(score_str)
        if score >= pass_mark:
            pass_count += 1
    return pass_count

# Exercise 4
def replace_word(filename, old_word, new_word):
    # Write your code here
    pass

# Exercise 5
def remove_line(filename, line_number):
    # Write your code here
    pass
