## Recording

[Week 5 session 1
recording](https://us06web.zoom.us/rec/share/cDg8wK6-kwW6X6qvk1rMvKHy5bjlBegV9oqlgpZO9iXqcUKAi8U4KM2FQNK0i6n0.keJS-JQuaVo5oPUs)

## Schedule and plan

* @ mentions on Github.
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

## That's it.

That's it for this session.
