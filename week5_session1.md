## Recording

[Week5 session
1 recording](https://numfocus-org.zoom.us/rec/share/oevqvp1VMEJ_DJCTZZMYxSoa-6s5LAkhJJ1d_OYzfNgB5mew2FnG0We_510WPtKH.gEgEwVbLXUehYVXd)

## Schedule and plan

### Github walkthrough

Diagram of the workflow:

![](https://nipraxis.org/summer-2023/assets/images/github_workflow.svg)

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
6. You will see URL to your new repository named
   `nipraxis-summer-2023/diagnostics-<teamname>` where `<teamname>` is the name
   you specified in your issue.  You may also get an email telling you about
   the repository.
7. Go to the link for your repository.  It will be of form
   `https://github.com/nipraxis-summer-2023/diagnostics-<teamname>`.
8. Make sure you know the Github usernames of your team members.
9. Go to the Settings tab.
10. Click on "Collaborators and Teams" on the left.
11. Click on "Add people".  Add the team members with whatever permissions you
    agree.  Maybe "maintain" is a good default.
12. Wait for your team members to accept their invitations.

Everyone (including the team leader):

1. You should get an invitation to your team repository.
2. Click on the link, that should be of form
   `https://github.com/nipraxis-summer-2023/diagnostics-<teamname>`, where
   `<teamname>` is your agreed team name.
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
    code, using a command of form: `git remote add upstream https://github.com/nipraxis-summer-2023/diagnostics-<teamname>`.
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
22. Next make a pull request from this branch on Github.  Either use the URL
    that Github displays in your terminal from the command above, of form
    `https://github.com/<your-gh-user>/diagnostics-<teamname}/pull/new/editing-readme`,
    OR go to your fork URL (of
    `https://github.com/<your-gh-user>/diagnostics-<teamname>`, and use the new
    green "Compare and pull request" button for your `editing-readme` branch.
    Click on that
23. Fill in the pull request description and submit the pull request.

The team leader should:

1. Go to the main repository page — of form
   `https://github.com/nipraxis-summer-2023/diagnostics-<teamname>`.
2. Click on one or more of the Pull Request pages available there, and click on
   the green Merge button to merge it / them.  (In fact, there are several
   options available via that green button, we are taking the default route by
   clicking on the green button.  See [the Github merge
   page](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request#merging-a-pull-request)
   for more details.

### Techniques

* @ mentions on Github.

## Modules and testing

* [sys.path](https://textbook.nipraxis.org/sys_path)
* [assert](https://textbook.nipraxis.org/assert)

### Reading and homework for next week

You should (by Thursday) receive a pull request into your upstream
repository.  Please check there for the homework.

If you do not see a pull request, please email [Matthew](mailto:matthew.brett@gmail.com).

The pull request has instructions, and some more pages to read.

Your task:

* Merge the pull request.
* Go to your local clone of your fork.
* `git fetch upstream`
* `git branch fix-validation upstream/main`
* `git checkout fix-validation`

For instructions, first, look in the **Get the data** section of the
`README.md` file, and follow the instructions there.

Then look at the files:

* `scripts/validate_data.py`

Next work on the code to run the given commands and fix the errors.  See
the instructions in the PR.

Now push, and make a pull request.   Work together to find the best solution, review the pull request, and merge it.

## That's it.

That's it for this session.
