
#def grade_sort(student_grades):
#  sorted_students = sorted(student_grades.items(), key=lambda student: student[1], reverse=True)
 # return sorted_students[0]

#student_grades = {}

# Adding student names and grades
#student_grades = {
 #   'Elon Musk': 45,
  #  'Alexander the Great': 60,
 #   'Atilla the Hun': 95,
 #   'Mao Xe Dong': 75,
  #  'Charlemagne': 100,
 #   'Napolean Bonaparte': 98,
#}

# Adding students
#new_students = {'Queen Victoria': 105, 'Genghis Khan': 102}
#student_grades.update(new_students)


#print(grade_sort(student_grades))

def group_words_by_length(words):
  word_dict = {}
  for word in words:
      word_len = len(word)
      if word_len not in word_dict:
        word_dict[word_len] = []
      word_dict[word_len].append(word)
  return word_dict

sentence = "how much wood would a woodchuck chuck if a woodchuck could chuck wood?"
words = sentence.split()
result = group_words_by_length(words)
print(result)

