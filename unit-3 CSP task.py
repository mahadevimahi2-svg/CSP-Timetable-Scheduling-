variables = ["Maths", "Python", "DBMS", "AI"]
slots = ["9:00 AM", "11:00 AM", "2:00 PM"]
domains = {v: slots[:] for v in variables}

# Pairs of subjects that cannot share a slot
constraints = [("Maths", "Python"), ("DBMS", "AI")]

def is_consistent(var, value, assignment):
    for a, b in constraints:
        if var in (a, b):
            other = b if var == a else a
            if assignment.get(other) == value:
                return False
    return True

def backtrack(assignment):
    if len(assignment) == len(variables):      # every subject has a slot
        return assignment
    var = next(v for v in variables if v not in assignment)
    for value in domains[var]:
        if is_consistent(var, value, assignment):
            assignment[var] = value
            result = backtrack(assignment)
            if result:
                return result
            del assignment[var]                # backtrack
    return None

solution = backtrack({})
print("Final Timetable")
print("-" * 25)
for subject, slot in solution.items():
    print(f"{subject:<8} -> {slot}")