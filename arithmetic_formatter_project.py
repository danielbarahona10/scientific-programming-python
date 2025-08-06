def arithmetic_arranger(problems, display_answers=False):
  
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = ''
  
  first_line = ''
  second_line = ''
  third_line = ''
  fourth_line = ''
  
  for problem in problems:
    problem = problem.split()
    if problem[1] == '*' or problem[1] == '/':
      return "Error: Operator must be '+' or '-'."
    if len(problem[0]) > 4 or len(problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    try:
      int(problem[0])
      int(problem[2])
    except Exception:
      return "Error: Numbers must only contain digits."
    
    length = max(len(problem[0]), len(problem[2]))+2
    spaces_first_line = length - len(problem[0])
    spaces_second_line = length - len(problem[2])-1

    first_line += ' '*spaces_first_line+problem[0]+' '*4
    second_line += problem[1]+' '*spaces_second_line+problem[2]+' '*4
    third_line += '-'*length+' '*4
    
    if display_answers:
      result = 0
      if problem[1] == '+':
        result = int(problem[0]) + int(problem[2])
      elif problem[1] == '-':
        result = int(problem[0]) - int(problem[2])
      fourth_line += ' '*(length-len(str(result)))+str(result)+' '*4

  first_line = first_line.rstrip()
  second_line = second_line.rstrip()
  third_line = third_line.rstrip()
  fourth_line = fourth_line.rstrip()
  
  if display_answers:
    arranged_problems = first_line+'\n'+second_line+'\n'+third_line+'\n'+fourth_line
  else:
    arranged_problems = first_line+'\n'+second_line+'\n'+third_line
  
  return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')