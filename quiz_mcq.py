import json
jsonobject = json.load(open("quiz.json"))
print("\n")
n = input("Enter your name : ")
print("\n")
def read_json(filename):
    jsonobject = json.load(open(filename))
def print_question():
  score = 0
  for i in jsonobject['quiz']:
    for j in jsonobject['quiz'][i]:
      print(jsonobject['quiz'][i][j]['question'])
      received_answer=receive_answer(jsonobject['quiz'][i][j]['question'],jsonobject['quiz'][i][j]['options'])
      score+=validate_answer(jsonobject['quiz'][i][j]['answer'],received_answer)
  print_final_result(score) 
def receive_answer(question,options):
    answers = {}
    index = ['a','b','c','d']
    count = 0; 
    for i in options:
        print(index[count]+"." + i)
        count = count + 1
    answer =input("\nType your answer here: ")
    print("\n")
    if answer=="a":
      return options[0]
    elif answer=="b":
      return options[1]
    elif answer=="c":
      return options[2]
    elif answer=="d":
      return options[3]
    else:
      receive_answer(question,options)
def validate_answer(correct_answer,given_answer):
  if correct_answer == given_answer:
    return 1
  else:
    return 0  
def print_final_result(score):
    print("You got " + str(score) + "/3" + " correct.")
    print("\n")
    if score == 3:
        print('***Your all answers are correct!!!***\n')
j_obj = read_json("/home/akhil/Downloads/my/quiz.json")
print_question()
