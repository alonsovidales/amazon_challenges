Given a paragraph of text, and a list of k words, write a program to find the first shortest sub-segment that contains each of the given k words at least once. The length of a segment is the number of words included; a segment is said to be shorter than another if it contains less words than the other structure. <br />
* Ignore characters other than [a-z][A-Z] in the text. <br />
* Comparison between the strings should be case-insensitive.<br />
Input format :<br />
The first line of the input contains the text. <br />
The next line contains k, the number of  words given to be searched.<br />
Each of the next k lines contains a word.<br />
<br />
Output format :<br />
Print first shortest sub-segment that contains given k words , ignore special characters, numbers. <br />
If no sub-segment is found it should return “NO SUBSEGMENT FOUND”<br />
<br />
Sample Input :<br />
This is a test. This is a programming test. This is a programming test in any language.<br />
4<br />
this<br />
a<br />
test<br />
programming<br />
Sample Output :<br />
a programming test This<br />
Explanation :<br />
In this test case segment "a programming test. This" contains given four words. You have to print without special characters, numbers so output is "a programming test This".  Another segment "This is a programming test." also contains given  four words but have more number of words. <br />
<br />
Constraints: <br />
Total number of characters in a paragraph will not be more than 200,000.<br />
0 < k <= no. of words in paragraph.<br />
0 < Each word length < 15<br />
