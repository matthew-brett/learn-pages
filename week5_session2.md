* Thursday 15:00 UTC session: [Thursday Zoom
  link](https://bham-ac-uk.zoom.us/j/85697917669?pwd=R09RRVoxSXl5YnVjVDVuN3NDM2lCdz09)
* Friday 18:00 UTC session: [Friday Zoom link](https://bham-ac-uk.zoom.us/j/82522323304?pwd=VjRRWDNkZjF5clBDd3FNNGJWcTUyZz09).

## Recording

We will add a link here after the Friday session.

## Schedule and plan

* Github workflow and the final project.

### Working with the template repo

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
   `nipraxis-spring-2022/diagnostics-<teamname>` where `<teamname>` is the
   name you specified in your issue.
7. Go to the link for your repository.  It will be of form
   `https://github.com/nipraxis-spring-2022/diagnostics-<teamname>`.
8. Make sure you know the Github usernames of your team members.
9. Go to the Settings tab.
10. Click on "Collaborators and Teams" on the left.
11. Click on "Add people".  Add the team members with whatever permissions you
    agree.  Maybe "maintain" is a good default.
12. Wait for your team members to accept their invitations.

Everyone (including the team leader):

1. You should get an invitation to your team repository.
2. Click on the link, that should be of form
   `https://github.com/nipraxis-spring-2022/diagnostics-<teamname>`, where `<teamname>` is your agreed team name.
3. Click on the "Fork" button near the top right of the screen.
4. Accept the defaults, click "Create Fork".
5. Now you should be at a new page, with URL of form:
   `https://github.com/<your-gh-user>/diagnostics-<teamname>` where `<your-gh-user>` is your Github username.
6. Click on the green "Code" button, select the "SSH" tab.  Copy the link
   there, which will be of form:
   `git@github.com:<your-gh-user>/diagnostics-<teamname>`
7. Open a terminal on your computer.  Change to a suitable directory to store
   your code.  Consider `cd $HOME/nipraxis` if you don't have a strong
   alternative preference.
8. Type a suitably modified version of this command: `git clone
   git@github.com:<your-gh-user>/diagnostics-<teamname>`, replacing the
   relevant parts with your username and your team name.
9. You should now have a local *clone* of your *fork*.
10. Change directory to the new cloned repository, with command of form `cd
    diagnostics-<teamname>`.
11. Add a new *remote* that points to the main "upstream" version of your team
    code, using a command of form: `git remote add upstream https://github.com/nipraxis-spring-2022/diagnostics-<teamname>`.
12. Check your remote worked with the command `git fetch upstream`.
13. Make a new feature branch `editing-readme`, with the command `git branch
    editing-readme`.
14. Checkout this branch with `git checkout editing-readme`.
15. Make sure you are up to date with the latest code from upstream with `git
    merge upstream/main`.  This may do nothing, if there are no new changes in
    the upstream `main` branch.
16. Use your text editor to make a change to the `README.md` file.
17. `git add README.md`
18. `git commit` (if you have your text editor set up correctly to work with
    Git) or `git commit -m 'Edit to README'` (if you do not).
19. Push up your changes to your *fork* with `git push origin editing-readme
    --set-upstream`.
20. Go to your fork URL (of form
    `https://github.com/<your-gh-user>/diagnostics-<teamname>`)
21. You should see a new green "Compare and pull request" button for your
    `editing-readme` branch. Click on that, fill in the details and submit the pull request.

## Modules and testing

* [sys.path](https://textbook.nipraxis.org/sys_path)
* [assert](https://textbook.nipraxis.org/assert)
* [path manipulation](https://textbook.nipraxis.org/path_manipulation)
* [docstrings](https://textbook.nipraxis.org/docstrings)

Now: <https://github.com/nipraxis/outlier-utils>

### Reading and homework for next week

TBA

## That's it.

That's it for this session.
