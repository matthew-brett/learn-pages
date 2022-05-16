* [Monday session Zoom link](https://bham-ac-uk.zoom.us/j/87903087978?pwd=OEtJbXBCekRiRjV2UkJnRmtxbUxXUT09)
* [Tuesday session Zoom link](https://bham-ac-uk.zoom.us/j/86508385148?pwd=WjNSdTdQUWkyWjRwVjBTeTVjSGczQT09)

## Recording

We will post this after the Tuesday session.

## Schedule and plan

### DVars and testing

We will be working with the [DVARS
metric](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5915574/).

The reference above defines DVARS as the "spatial root mean square".

It's a measure of the difference in the voxel values between two volumes.

Assume `this_vol` is one 3D array representing a volume, and `prev_vol` is
another 3D array representing a volume.  The DVARS difference between these two volumes is:

```{python}
vol_diff = this_vol - prev_vol
dvar_val = np.sqrt(np.mean(vol_diff ** 2))
```

Your task, should you choose to accept it, is the following.

* Nominate a team member, and tell us (your instructors) the URL of the NTM's
fork of your diagnostics project.  For example if your diagnostics project
upstream was `https://github.com/nipraxis-spring-2022/diagnostics-example` and
`matthew-brett` was the Github username of the NTM, then you would sent the
URL `https://github.com/matthew-brett/diagnostics-example`.
* We will then make pull request to the Github repository of your NTM.
* The NTM should:
  * Merge the pull request on Github
  * On their own computer do a `git fetch origin` inside their diagnostics
  repository.
  * Start a new branch to do a PR to the upstream repository with:

    ```
    git branch add-dvars origin/main --no-track
    git checkout add-dvars
    ```

  * Run the test command:

    ```
    python3 -m pytest findoutlie/tests/test_dvars.py
    ```

    If you get an error `No module named pytest`, then run:

    ```
    python3 -m pip install pytest
    ```

    and try again.

  * You might consider also *installing* your new directory module `findoutlie`.  To do this:

    ```
    # You may be able to omit the --user below
    python3 -m pip install --user flit
    python3 -m flit install -s
    ```

    Don't worry if this does not work, or is confusing.  We will come back to
    that later.

  * Read the files:

    * `findoutlie/metrics.py` and
    * `findoutlie/tests/test_dvars.py`

    and complete these to make the tests pass.

  * Hint — for full efficiency, you might consider revisiting the [4D to 2D
  reshaping page](https://textbook.nipraxis.org/reshape_and_4d.html)

  * When you have solved this, make a pull request to the upstream repository,
  and @ mention one of the instructors for a review.

### Voxel statistics

* [Voxel time courses](https://textbook.nipraxis.org/voxel_time_courses).
* Git / testing exercise at <https://github.com/nipraxis/pearson>.
* [Voxel correlation
exercise](https://hub.nipraxis.org/hub/user-redirect/git-pull?repo=https%3A//github.com/nipraxis/voxel_correlation&subPath=voxel_correlation.ipynb)

## That's it.

That's it for this session.
