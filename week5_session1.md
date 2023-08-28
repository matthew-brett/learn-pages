## Recording

We will post the recording after the session.

## Schedule and plan

### Github walkthrough

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

### Techniques

* @ mentions on Github.

## Modules and testing

* [sys.path](https://textbook.nipraxis.org/sys_path)
* [assert](https://textbook.nipraxis.org/assert)
* [docstrings](https://textbook.nipraxis.org/docstrings)
* [validating data](https://textbook.nipraxis.org/validating_data)
* [Module directories](https://textbook.nipraxis.org/module_directories.html)
* [On testing](https://textbook.nipraxis.org/on_testing)

### DVARS and testing

We will be working with the [DVARS
metric](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5915574/).

The reference above defines DVARS as the "spatial root mean square".

It's a measure of the difference in the voxel values between two volumes.

Assume `this_vol` is one 3D array representing a volume, and `prev_vol` is
another 3D array representing a volume.  The DVARS difference between these two
volumes is:

```{python}
vol_diff = this_vol - prev_vol
dvar_val = np.sqrt(np.mean(vol_diff ** 2))
```

* Go to your breakout rooms as usual.
* We will send a pull request to the Github repository of your project's
  upstream repository.
* A team member (maybe the *driver*) should merge the pull request on Github.
* The driver for your session should do the following steps, with the
  *navigators* instructing the driver what to do, and watching for (the
  inevitable) mistakes.
* The rest of the steps are for the *driver*.
* Start a terminal.
* Navigate to your Git working directory with something like `cd
  $HOME/Documents/nipraxis-work/diagnostics-<team_name>` where `<team_name>` is
  your team name.
* Fetch the new contents of the upstream repository with `git fetch upstream`.
*   Start a new branch to do a PR to the upstream repository with:

    ```
    git branch add-dvars upstream/main --no-track
    git checkout add-dvars
    ```
*   Install your new directory module `findoutlie` using the Python package
    manager *Pip*.  Here we are using the `--editable` flag to tell Pip to
    install the package in *editable* mode.  In this mode, when you make
    changes to the package files, you see the changes in the installed package
    immediately, without having to do another install.  You may or may not need
    the `--user` flag.  Try with `--user`, and drop `--user` if that fails.

    ```
    python3 -m pip install --user --editable .
    ```

*   Now test that you can import the `findoutlie` module by running this
    command.  The `-c` flag tells Python to run the code that follows the `-c`
    flag.

    ```
    python3 -c 'import findoutlie'
    ```

    This should give *no error*, because the previous step installed the
    `findoutlie` directory module to somewhere on Python's search path. Tell us
    if any of the commands above did give an error.

*   Run the test command:

    ```
    python3 -m pytest findoutlie/tests/test_dvars.py
    ```

    If you get an error `No module named pytest`, then run:

    ```
    python3 -m pip install pytest
    ```

    and try again.

*   Read the files:

    * `findoutlie/metrics.py` and
    * `findoutlie/tests/test_dvars.py`

    and complete the `findoutlie/metrics.py` to make the tests pass.

* **Hint 1** — one of the ways to write the `dvars` function in the most
  efficient way, would use ideas from [4D to 2D reshaping
  page](https://textbook.nipraxis.org/reshape_and_4d.html). You might also
  benefit from the `np.diff` function.

* When you have solved this, make a pull request to the upstream repository,
  and @ mention one of the instructors for a review.

### Voxel statistics

If we have time...

*   Git / testing exercise at <https://github.com/nipraxis/pearson>.

    ```
    git clone https://github.com/nipraxis/pearson
    cd pearson
    pytest .
    ```

* [Voxel time courses](https://textbook.nipraxis.org/voxel_time_courses).
* [Voxel correlation
  exercise](https://hub.nipraxis.org/hub/user-redirect/git-pull?repo=https%3A//github.com/nipraxis/voxel_correlation&subPath=voxel_correlation.ipynb)

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
