## Recording

[Week 5 session 2 recording](https://us06web.zoom.us/rec/share/6cBPJSNM-ro1jMn3euhV7krpH9E_Ao640b3MBcM7lg9gko7UamUaRQs_dupquddI.-vIh2nQXSLpbuYaM)

## Schedule and plan

### Details about the project

1. Fill out the script and any needed library code to run
   `scripts/find_outliers.py data` on your data, and return a list of
   outlier volumes for each scan (where there is an outlier);
2. You should add a text file giving a brief summary for each outlier scan,
   why you think the detected scans should be rejected as an outlier, and your
   educated guess as to the cause of the difference between this scan and the
   rest of the scans in the run;
3. You should do this by collaborating in your teams using git and github;

We will rate you on:

* the quality of your outlier detection as assessed by the improvement in the
  statistical testing for the experimental model after removing the outliers;
* the generality of your outlier detection as assessed by the improvement in
  the statistical testing for the experimental model after removing the
  outliers, for another similar dataset;
* the quality of your code;
* the quality and transparency of your process, from your interactions on
  github;
* the quality of your arguments about the scans rejected as outliers.

Your outlier detection script should be *reproducible*.

That means that we, your instructors, should be able to clone your repository,
and then follow simple instructions in order to be able to reproduce your run
of `scripts/find_outliers.py data` and get the same answer.

To make this possible, fill out the `README.md` text file in your repository
to describe a few simple steps that we can take to set up on our own machines
and run your code.  Have a look at the current `README.md` file for a
skeleton.  We should be able to perform these same steps to get the same
output as you from the outlier detection script.

## Modules and testing

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

```python
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

### And further

* [on convolution](https://textbook.nipraxis.org/on_convolution)
* [The hemodynamic response
  function](https://textbook.nipraxis.org/convolution_background)
* [HRF
  exercise](https://hub.nipraxis.org/hub/user-redirect/git-pull?repo=https%3A//github.com/nipraxis/make_hrf&subPath=make_hrf.ipynb)

### Homework

* Agree a provisional project analysis plan with your group.  Don't worry about
  the detail, it's just a draft to get the discussion going, or even just to
  clarify your ideas about what the task is.
* Write it up as `analysis_plan.md` and make a pull request to your upstream repository.
*   When you think it is ready to merge, @ mention the instructors by
    adding a comment to the pull-request on the lines of:

    > @nipraxis-fall-2022/instructors - this plan is now ready for review.

    We will review your analysis plan, discuss and then Approve it using the
    Github interface.

* All by Monday next week!

## That's it.

That's it for this session.
