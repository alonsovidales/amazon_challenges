Given M busy-time slots of the team members in the Kindle team, can you print all the available time slots when all of them can schedule a meeting for a duration of K minutes.<br />
The event time will be of the form HH MM (where 0 <= HH <= 23 and 0 <= MM <= 59). K will be in the form minutes.<br />
 <br />
Input Format:<br />
 <br />
M K [M number of busy time slots , K is the duration in minutes]<br />
This is followed by M lines with 4 numbers on each line.<br />
Each line will be of the form StartHH StartMM EndHH EndMM  [Eg: 9am-11am time slot will be given as 9 00 11 00]<br />
An event time slot is of the form [Start Time, End Time) which means the start time is inclusive but not the end time;<br />
So, an event of the form 10 00  11 00 => implies that the meeting starts at 10:00 and ends at 11:00. Hence, another meeting can start at 11:00.<br />
 <br />
Sample Input:<br />
5 120<br />
16 00 17 00<br />
10 30 14 30<br />
20 45 22 15<br />
10 00 13 15<br />
09 00 11 00<br />
 <br />
Sample Output:<br />
00 00 09 00<br />
17 00 20 45<br />
 <br />
Sample Input:<br />
8 60<br />
08 00 10 15<br />
22 00 23 15<br />
17 00 19 00<br />
07 00 09 45<br />
09 00 13 00<br />
16 00 17 45<br />
12 00 13 30<br />
11 30 12 30<br />
 <br />
Sample Output:<br />
00 00 07 00<br />
13 30 16 00<br />
19 00 22 00<br />
 <br />
Constraints :<br />
1 <= M <= 100<br />
 <br />
Note: 24 00 has to be presented as 00 00.<br />
