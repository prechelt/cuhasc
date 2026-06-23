
List open issues.
Pick the **lowest-numbered issue labeled 'ready-for-agent'** and solve it.
If there is no such issue, output "<promise>COMPLETE!</promise>" (precisely!) and stop.

If the "blocked by" section mentions issues in the same state, solve those first:
Switch to an issue that does not have such entries.

Print number and title of the issue you picked.

When adding/changing code, proceed using /tdd and output the name of each test each time it turns from red to green.
If the issue only **modifies existing functionality slightly**, prefer adapting existing tests over adding new ones,
but still follow a test-first approach.
When no code changes are involved, produce tests only if requested explicitly.

If you hit genuine design ambiguity mid-implementation, 
explain the problem (and your suggestion) in a new comment in the issue,
set the issue label to 'ready-for-human', and stop.

Run the full test suite at the end, but prefer smaller runs before if the risk of breaking something appears low.

When done, commit your work results (but do not push), then change the issue label to 'ready-for-review'.
Add a comment to the issue that summarizes your work as a short itemized list of the files changed (and how).
In addition, print the summary.

Split complex changes into several **commits**, keep simple changes in a single commit, even if it consists
of multiple (smaller) file changes.
Commit only your own current changes, not others.
Commit msg format: "mainfilename: #issue; short content description".
Rarely two or three main files. 
Expand content description to several lines only in rare critical cases.

