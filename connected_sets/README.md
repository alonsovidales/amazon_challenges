Given a 2–d matrix , which has only 1’s and 0’s in it. Find the total number of connected sets in that matrix.<br />
<br />
<br />
Explanation:<br />
Connected set can be defined as group of cell(s) which has 1 mentioned on it and have at least one other cell in that set with which they share the neighbor relationship. A cell with 1 in it and no surrounding neighbor having 1 in it can be considered as a set with one cell in it. Neighbors can be defined as all the cells adjacent to the given cell in 8 possible directions ( i.e N , W , E , S , NE , NW , SE , SW direction ). A cell is not a neighbor of itself.<br />
<br />
<br />
Input format :<br />
<br />
First line of the input contains T , number of test-cases.<br />
Then follow T testcases. Each testcase has given format.<br />
N [ representing the dimension of the matrix N X N ].<br />
Followed by N lines , with N numbers on each line.<br />
<br />
<br />
<br />
Ouput format :<br />
<br />
For each test case print one line ,  number of connected component it has.<br />
<br />
Sample Input :<br />
<br />
4<br />
4<br />
0 0 1 0<br />
1 0 1 0<br />
0 1 0 0<br />
1 1 1 1<br />
4<br />
1 0 0 1<br />
0 0 0 0<br />
0 1 1 0<br />
1 0 0 1<br />
5<br />
1 0 0 1 1<br />
0 0 1 0 0<br />
0 0 0 0 0<br />
1 1 1 1 1<br />
0 0 0 0 0<br />
8<br />
0 0 1 0 0 1 0 0<br />
1 0 0 0 0 0 0 1<br />
0 0 1 0 0 1 0 1<br />
0 1 0 0 0 1 0 0<br />
1 0 0 0 0 0 0 0<br />
0 0 1 1 0 1 1 0<br />
1 0 1 1 0 1 1 0<br />
0 0 0 0 0 0 0 0<br />
<br />
Sample output :<br />
<br />
1<br />
3<br />
3<br />
9<br />
<br />
Constraint :<br />
<br />
0 < T < 6 <br />
0 < N < 1009 <br />
