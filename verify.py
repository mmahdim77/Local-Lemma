import sys

if len(sys.argv) != 3:
  print("Usage: python3 verify.py sat_instance.txt solution.txt")
  quit()

# read the instance
print("Reading SAT instance from file")
with open(sys.argv[1], "r") as sat_file:
  n, m = map(int, sat_file.readline().split())
  clauses = [tuple(map(int, sat_file.readline().split()))[1:] for _ in range(m)]

# read the instance
print("Reading proposed satisfying assignment")
with open(sys.argv[2], "r") as sol_file:
  solution = sol_file.readline().strip()
  assert len(solution) == n and all(x in "TF" for x in solution)

  # convert T / F values to +1 / -1
  x = [0]+[1 if v == "T" else -1 for v in solution]

# check all clauses
unsat = 0
for i in range(m):
  # get the -1 / +1 values for the variables in the clause
  xvals = [x[abs(l)] for l in clauses[i]]

  # check that the clause is satisfied, if so then "continue"
  if not all(clauses[i][j]*xvals[j] < 0 for j in range(len(clauses[i]))): continue

  # if we get here, the clause was unsatisfied
  if unsat == 0:
    print("First unsatisfied clause location:", i+1)
    print("Unsatisfied clause:", *clauses[i])
    print("Corresponding variables:", *xvals)
    unsat += 1

if unsat:
  print("Unsatisfied Clauses:", unsat)
else:
  print("Satisfied!")
