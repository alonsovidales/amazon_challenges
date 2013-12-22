Given a number K, find the smallest Fibonacci number that shares a common factor( other than 1 ) with it. A number is said to be a common factor of two numbers if it exactly divides both of them.<br />
<br />
Output two separate numbers, F and D, where F is the smallest fibonacci number and D is the smallest number other than 1 which divides K and F.<br />
<br />
Input Format <br />
<br />
First line of the input contains an integer T, the number of testcases.<br />
Then follows T lines, each containing an integer K.<br />
<br />
Output Format<br />
<br />
Output T lines, each containing the required answer for each corresponding testcase.<br />
 <br />
 <br />
<br />
 <br />
<br />
Sample Input <br />
 <br />
3<br />
3<br />
5<br />
161<br />
 <br />
Sample Output<br />
 <br />
3 3<br />
5 5<br />
21 7<br />
 <br />
Explanation<br />
 <br />
There are three testcases. The first test case is 3, the smallest required fibonacci number  3. The second testcase is 5 and the third is 161. For 161 the smallest fibonacci numer sharing a common divisor with it is 21 and the smallest number other than 1 dividing 161 and 7 is 7.<br />
 <br />
Constraints :<br />
 <br />
1 <= T <= 5<br />
2 <= K <= 1000,000<br />
The required fibonacci number is guaranteed to be less than 10^18.<br />
