
List issues.
Pick the **lowest-numbered issue labeled 'good first issue'** and solve it.
If there is no such issue, output "<promise>COMPLETE!</promise>" (precisely!) and stop.

If the issue involves adding **new functionality**, proceed using /tdd and output the name
of each new test each time it turns from red to green.
If the issue only **modifies existing functionality slightly**, prefer adapting existing tests over adding new ones,
but still follow a test-first approach.

If you hit genuine design ambiguity mid-implementation, 
explain the problem (and your suggestion) in a new comment in the issue,
set the issue label to 'ready-for-human', and stop.

Run the full test suite at the end, but prefer smaller runs before if the risk of breaking something appears low.

When done, commit your work results (but do not push), then change the issue label to 'ready-for-review'.
Add a comment to the issue that summarizes your work as a short itemized list of the files changed (and how).
Print the summary.

Split complex changes into several **commits**, keep simple changes in a single commit, even if it consists
of multiple (smaller) file changes.
Commit msg format: "mainfilename: #issue; short content description".
Issue number can be missing. Rarely two or three main files. 
Expand content description to several lines only in rare critical cases.

