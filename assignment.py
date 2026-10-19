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
        if not line:
            parts=line.split(',')
            score=int(parts[1])
            total_score+=score
            student_count+=1
    file.close()
    if student_count==0:
        return 0

    average = total_score / student_count
    return f"Average score: {average:.1f}"
# Exercise 3
def filter_passed(source, destination, pass_mark):
    # Write your code here
    pass

# Exercise 4
def replace_word(filename, old_word, new_word):
    # Write your code here
    pass

# Exercise 5
def remove_line(filename, line_number):
    # Write your code here
    pass
