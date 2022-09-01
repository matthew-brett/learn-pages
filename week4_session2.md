## Recording

[Week 4 session
2](https://us06web.zoom.us/rec/share/zSUlLCP2mW2D18zyCV3e-h0a3SN_agKBOa5FWHjBtX0QCIyZx1zEWwktpNOqwOeS.X4YoDtxaktmAkcsd)

## Schedule and plan

* Github workflow and the final project.

### On the benefits of searching for the right solution

We discussed the phenomenon that scientific programmers often stall at
a certain level, and do not continue learning.

The key to learning is *deliberative practice*, as [Peter
Norvig](https://en.wikipedia.org/wiki/Peter_Norvig) discusses in his page
[Teach Yourself Programming in 10 years](https://www.norvig.com/21-days.html).

On the other hand, being good at programming *quickly* has some costs. [Peter
Norvig notes that Google employees do slightly less well if they have
previously won a programming
competition](https://www.youtube.com/watch?v=DdmyUZCl75s), and speculates this
is because the best programmers think hard and for a long time about the right
solution.  We recommend this course to you, of taking time to reflect on the
right way to solve each problem.

### Working with the template repo

Diagram of the workflow:

![](https://nipraxis.org/fall-2022/assets/images/github_workflow.svg)


Team leader:

0. Before you start, agree a team name with your team, and get your team
   members' Github usernames — e.g. `matthew-brett`.
1. Go to <https://github.com/nipraxis/diagnostics-template>
2. Open the Issues tab.  You can get there directly by appending `issues` to
   the URL, like this:
   <https://github.com/nipraxis/diagnostics-template/issues>
3. Make a "New Issue".
4. In the issue, ask for a new diagnostics repository for your team.  Specify
   a *name* for your team.
5. Wait for our response, on that issue.
6. You will get an email inviting you to a new repository named
   `nipraxis-fall-2022/diagnostics-<teamname>` where `<teamname>` is the
   name you specified in your issue.
7. Go to the link for your repository.  It will be of form
   `https://github.com/nipraxis-fall-2022/diagnostics-<teamname>`.
8. Make sure you know the Github usernames of your team members.
9. Go to the Settings tab.
10. Click on "Collaborators and Teams" on the left.
11. Click on "Add people".  Add the team members with whatever permissions you
    agree.  Maybe "maintain" is a good default.
12. Wait for your team members to accept their invitations.

Everyone (including the team leader):

1. You should get an invitation to your team repository.
2. Click on the link, that should be of form
   `https://github.com/nipraxis-fall-2022/diagnostics-<teamname>`, where `<teamname>` is your agreed team name.
3. Click on the "Fork" button near the top right of the screen.
4. Accept the defaults, click "Create Fork".
5. Now you should be at a new page, with URL of form:
   `https://github.com/<your-gh-user>/diagnostics-<teamname>` where `<your-gh-user>` is your Github username.
6. Click on the green "Code" button, select the "HTTPS" tab.  Copy the link
   there, which will be of form:
   `https://github.com/<your-gh-user>/diagnostics-<teamname>`.  If you have got
   SSH keys set up, you might instead consider using the "SSH" tab, and link.
7. Open a terminal on your computer.  Change to a suitable directory to store
   your code.  Consider `cd $HOME/Documents/nipraxis-work` if you don't have
   a strong alternative preference.
8. Type a suitably modified version of this command: `git clone
   https://github.com/<your-gh-user>/diagnostics-<teamname>`, replacing the
   relevant parts with your username and your team name.  (If you used
   SSH above, modify the clone command to something of form `git clone
   git@github.com:<your-gh-user>/diagnostics-<teamname>`
9. You should now have a local *clone* of your *fork*.
10. Change directory to the new cloned repository, with command of form `cd
    diagnostics-<teamname>`.
11. Add a new *remote* that points to the main "upstream" version of your team
    code, using a command of form: `git remote add upstream https://github.com/nipraxis-fall-2022/diagnostics-<teamname>`.
12. Check your remote worked with the command `git fetch upstream`.
13. Make a new feature branch `editing-readme`, with the command `git branch
    editing-readme`.
14. Checkout this branch with `git checkout editing-readme`.
15. Make sure you are up to date with the latest code from upstream with `git
    merge upstream/main`.  This may do nothing, if there are no new changes in
    the upstream `main` branch.
16. Use your text editor to make a change to the `README.md` file.
17. Confirm Git agrees that you have changed the file with  `git status`
18. Add the file to the staging area with `git add README.md`
19. Confirm Git agrees that you have added the file with  `git status`
20. `git commit` (if you have your text editor set up correctly to work with
    Git) or `git commit -m 'Edit to README'` (if you do not).
21. Push up your changes to your *fork* with `git push origin editing-readme
    --set-upstream`.
22. Go to your fork URL (of form
    `https://github.com/<your-gh-user>/diagnostics-<teamname>`)
23. You should see a new green "Compare and pull request" button for your
    `editing-readme` branch. Click on that, fill in the description and submit the pull request.

The team leader should:

1. Go to the main repository page — of form
   `https://github.com/nipraxis-fall-2022/diagnostics-<teamname>`.
2. Select one or more of the Pull requests to merge, and merge it / them.

## Modules and testing

* [sys.path](https://textbook.nipraxis.org/sys_path)
* [assert](https://textbook.nipraxis.org/assert)
* [docstrings](https://textbook.nipraxis.org/docstrings)
* [validating data](https://textbook.nipraxis.org/validating_data)

### Reading and homework for next week

You should (on Thursday) have received a pull request into your upstream
repository.  Please check there for the homework.

If you do not see a pull request, please email [Matthew](mailto:matthew.brett@gmail.com).

The pull request has instructions, and some more pages to read.

Your task:

* Merge the pull request.
* Go to your local clone of your fork.
* `git fetch upstream`
* `git branch fix-detectors upstream/main`
* `git checkout fix-detectors`

For instructions, look in the files:

* `scripts/validate_data.py`
* `findoutlie/detectors.py`

And then work on the code to run the given commands and fix the errors, until
you get `Tests passed` from both given commands (see instructions in the PR).

Now push, and make a pull request.   Work together to find the best solution, review the pull request, and merge it.

## That's it.

That's it for this session.
