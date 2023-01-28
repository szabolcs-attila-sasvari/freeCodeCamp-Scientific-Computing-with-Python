# Define the commonly used symbols as global variables
plus_symbol = '+'
minus_symbol = '-'
space_symbol = ' '


# Arithmetic arranger function
def arithmetic_arranger(problems, solution=False):
  # Attributes
  problems_with_components = []
  problem = ""

  # Check the number of problems
  if 5 < len(problems):
    return "Error: Too many problems."

  # Split the problems into components and check the digits' validity
  for element in problems:
    operation = minus_symbol
    if not element.__contains__('+') and not element.__contains__('-'):
      return "Error: Operator must be '+' or '-'."
    if element.__contains__('+'):
      operation = plus_symbol
    current = [e.strip() for e in element.split(operation)]
    for number in current:
      if 4 < len(number):
        return "Error: Numbers cannot be more than four digits."
      elif number.isdigit():
        continue
      else:
        return "Error: Numbers must only contain digits."
    current.append(operation)
    problems_with_components.append(current)

  # Return the solution
  limit = lambda x: 4 if solution else 3
  for i in range(0, limit(solution)):
    if i != 0:
      problem += '\n'
    for j in range(0, problems_with_components.__len__()):
      spaces = lambda x: 4 if x < problems_with_components.__len__() - 1 else 0
      if len(str(problems_with_components[j][0])) > len(
          str(problems_with_components[j][1])):
        maximum_length = len(str(problems_with_components[j][0])) + 2
      else:
        maximum_length = len(str(problems_with_components[j][1])) + 2
      if i == 0:
        problem += f"{space_symbol * (maximum_length - len(str(problems_with_components[j][0])))}"
        problem += f"{problems_with_components[j][0]}{space_symbol * spaces(j)}"
      if i == 1:
        problem += f"{problems_with_components[j][2]}"
        problem += f"{space_symbol * (maximum_length - 1 - len(str(problems_with_components[j][1])))}"
        problem += f"{problems_with_components[j][1]}{space_symbol * spaces(j)}"
      if i == 2:
        problem += f"{minus_symbol * maximum_length}{space_symbol * spaces(j)}"
      if solution and i == 3:
        if problems_with_components[j][2] == '+':
          problem += f"{space_symbol * (maximum_length - (len(str(int(problems_with_components[j][0]) + int(problems_with_components[j][1])))))}"
          problem += f"{int(problems_with_components[j][0]) + int(problems_with_components[j][1])}"
          problem += f"{space_symbol * spaces(j)}"
        else:
          problem += f"{space_symbol * (maximum_length - (len(str(int(problems_with_components[j][0]) - int(problems_with_components[j][1])))))}"
          problem += f"{int(problems_with_components[j][0]) - int(problems_with_components[j][1])}"
          problem += f"{space_symbol * spaces(j)}"
  return problem
