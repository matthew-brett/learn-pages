* Thursday 15:00 UTC session: [Thursday Zoom
  link](https://bham-ac-uk.zoom.us/j/85697917669?pwd=R09RRVoxSXl5YnVjVDVuN3NDM2lCdz09)
* Friday 18:00 UTC session: [Friday Zoom link](https://bham-ac-uk.zoom.us/j/82522323304?pwd=VjRRWDNkZjF5clBDd3FNNGJWcTUyZz09).

## Recording

We will post this after the Friday session.

## Schedule and plan

### Code review workflow

See live demo.

### Details about the project

#. Fill out the script and any needed library code to run
   `scripts/find_outliers.py data` on your data, and return a list of
   outlier volumes for each scan (where there is an outlier);
#. You should add a text file giving a brief summary for each outlier scan,
   why you think the detected scans should be rejected as an outlier, and your
   educated guess as to the cause of the difference between this scan and the
   rest of the scans in the run;
#. You should do this by collaborating in your teams using git and github;

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

### On testing

* [Module directories](https://textbook.nipraxis.org/module_directories)
* [Assert](https://textbook.nipraxis.org/assert)
* [Testing](https://textbook.nipraxis.org/on_testing)
* Stimuli exercise: `git clone https://github.com/nipraxis/stimutils`
* [Voxel time courses](https://textbook.nipraxis.org/voxel_time_courses)

### Reading and homework for next week

* Finish up the stimuli exercise above.
* Read / do the [Markdown tutorial](https://www.markdowntutorial.com)
* Submit, review and finalize your initial analysis plan in your upstream
  repository.

## That's it.

That's it for this session.
