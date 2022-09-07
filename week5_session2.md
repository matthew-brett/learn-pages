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

### Voxel statistics

* [Voxel time courses](https://textbook.nipraxis.org/voxel_time_courses).
* [Voxel correlation
  exercise](https://hub.nipraxis.org/hub/user-redirect/git-pull?repo=https%3A//github.com/nipraxis/voxel_correlation&subPath=voxel_correlation.ipynb)
* [on convolution](https://textbook.nipraxis.org/on_convolution)
* [The hemodynamic response
  function](https://textbook.nipraxis.org/convolution_background)
* [HRF
  exercise](https://hub.nipraxis.org/hub/user-redirect/git-pull?repo=https%3A//github.com/nipraxis/make_hrf&subPath=make_hrf.ipynb)

### Homework

* Agree a project analysis plan with your group.
* Write it up as `analysis_plan.md` and make a pull request to your upstream repository.
*   When you think it is ready to merge, @ mention the instructors by
    adding a comment to the pull-request on the lines of:

    > @nipraxis-fall-2022/instructors - this plan is now ready for review.

    We will review your analysis plan, discuss and then Approve it using the
    Github interface.

* All by Monday next week!

## That's it.

That's it for this session.
