def arithmetic_arranger(problems, solve=False):

  rowA = ""
  rowB = ""
  lines = ""
  solutions = ""

  if len(problems) > 5:
    return "Error: Too many problems."
  
  for i in problems:
    x, o, y = i.split(" ")

    if len(x) > 4 or len(y) > 4:
      return "Error: Numbers cannot be more than four digits."
      
    if o != "+" and  o != "-":
      return "Error: Operator must be '+' or '-'."
      
    if not x.isdecimal() or not y.isdecimal():
      return "Error: Numbers must only contain digits."
      
    sum = ""
    if o == "+":
      sum = str(int(x) + int(y))
    elif o == "-":
      sum = str(int(x) - int(y))

    width = max(len(x), len(y)) + 2
    elementA = x.rjust(width)
    elementB = o + y.rjust(width - 1)
    line = ""
    solution = sum.rjust(width)

    for r in range(width):
      line += "-"

    if i != problems[-1]:
      rowA += elementA + " "*4
      rowB += elementB + " "*4
      lines += line + " "*4
      solutions += solution + " "*4
    else:
      rowA += elementA
      rowB += elementB
      lines += line
      solutions += solution
    
    if solve:
      arranged_problems = rowA + "\n" + rowB + "\n" + lines + "\n" + solutions
    else:
      arranged_problems = rowA + "\n" + rowB + "\n" + lines
  
  return arranged_problems
