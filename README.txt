All SAT instances are 9-SAT(10) instances: each clause contains exactly 9 literals (variables or their negations), no variable appears twice in the same clause (i.e. all 9 variables involved in a clause are distinct), and each variable appears in at most 10 clauses. In fact, in these instances each variable appears in exactly 10 clauses.

Files:
1) small.txt - a small 9-SAT(10) instance (9 variables, 10 clauses)
2) medium.txt - a medium 9-SAT(10) instance (9,000 variables, 10,000 clauses)
3) large.txt - a large 9-SAT(10) instance (900,000 variables, 1,000,000 clauses)
4) small_answer.txt - a solution for the SAT instance small.txt, this is the expected output format from your code
5) verify.py - a Python script that will verify an answer file for a sat instance.

SAT instance file specification
1st line contains two numbers n, m, which are the number of variables and clauses
Then m lines follow, each describing a clause. The first number on a line describes the length L of the clause (# of literals) and the rest of the line contains L values, each between 1 and n or between -1 and -n. A number 1 <= k <= n indicates the variable x_k appears in the clause in its positive (not negated) form. A number -n <= k <= -1 indicates that variable x_{|k|} appears in the clause in its negated form.

NOTE: In this assignment, L will always be 9 since each clause depends on exactly 9 variables.

For example, if a clause (of length 3) is x_1 V ~x_2 V x_4 (i.e. the middle is "not x_2" but the others are not negated), the corresponding line would be:
3 1 -2 4

Answer file specification
Just a single line containing n characters T or F without spaces in between.

Verification Program
Usage:
python3 verify.py satfile.txt ansfile.txt

For example, to use this with the given answer for small.txt you should run:
python3 verify.py small.txt small_answer.txt

Read the problem statement carefully to see what you should do!
