======
day_00
======

############################
Introduction, Python, images
############################

*******************
Course introduction
*******************

* what we are going to teach;
* why we are teaching this way;
* structure of classes and homework;
* what the final project will look like (see :doc:`projects`);
* grading (see :doc:`logistics`).

Introduction talk slides:

* :download:`slides as PDF <day_00_slides.pdf>`;
* :download:`slides as Markdown source <day_00_slides.md>`.

**********************
Teaching and exercises
**********************

* :doc:`classwork/day_00/what_is_an_image`;
* :doc:`brisk_python`;
* (see also :doc:`classwork/day_00/introducing_python` for a slightly shorter
  and less comprehensive version of :doc:`brisk_python`).

To start the exercise, open your terminal and type::

    pip3 install --user ipython
    git clone https://github.com/psych-214-fall-2016/classwork.git
    cd classwork/day_00

Then::

    atom first_python.py

If we have time, we will start the introduction to the numpy data library,
from the `numpy introduction`_ of the `scipy lecture notes`_.

* The lecture on the `numpy array object`_;
* Some of the lecture on numerical `array operations`_.

********************
Reading and homework
********************

Please read:

* Donoho et al 2009 :cite:`donoho2009reproducible` (you can skip-read the
  sections on Sparselab, Symmlab and Spherelab);
* Preeyanon et al 2014 :cite:`preeyanon2014reproducible`;
* Wilson et al 2014 :cite:`wilson2014best`.

From these papers choose one recommendation for research practice and write:

* one to two paragraphs giving the strongest case you can make for *not* using
  that practice;
* one to two paragraphs giving the strongest refutation you can for your first
  paragraph.


======
lab_00
======

######################
Basic Python exercises
######################

Make sure you have read and understood :doc:`brisk_python`.

Next fetch the exercises using the ``git clone`` command below.  The exercises
are slightly modified versions of the exercises from the `Google Python
class`_.  Specifically, the edited versions run correctly on Python 3.

::

    git clone https://github.com/psych-214-fall-2016/day_00_lab
    cd day_00_lab

Check that all is well by running the test program::

    python3 hello.py

Next get ready to start the `basic exercises`_::

    cd basic

First do these exercises:

* ``list1.py``;
* ``list2.py``;
* ``string1.py``;
* ``string2.py``.

To do the exercises:

* open IPython_ (``ipython`` at the terminal command line);
* in IPython, type ``run list1.py`` (or ``list2.py`` etc).  This will run the
  tests embedded in the exercise.  These should fail until you have edited the
  file to add the code you need;
* open ``list1.py`` (etc) in Atom;
* look at the instructions in the file, and fill out the functions that the
  instructions suggest.  Rerun ``run list.py`` in IPython when you've finished
  a function, to see whether the tests pass.

Now you are ready for the more extended exercises in ``wordcount.py`` and
``mimic.py``.  To test ``wordcount.py``, do::

    run wordcount.py --count small.txt

and::

    run wordcount.py --topcount small.txt

in IPython.  See the instructions in ``wordcount.py`` for the meaning of
``--count`` and ``--topcount``.  You might also try using ``alice.txt``
instead of ``small.txt``.

For ``mimic.py`` use::

    run mimic.py small.txt

in IPython.


======
day_01
======

###########################
Arrays, images and plotting
###########################

********
Teaching
********

We will be using the background from the tutorial pages from the `scipy
lecture notes`_:

* The `numpy array object`_;
* `Array operations`_.

We'll cover:

* numpy_ arrays;
* plotting with `matplotlib`_;
* arrays can be displayed as images;
* a 2D array is a 2D image;
* 3D arrays and brain volumes;
* reshaping and slicing arrays;
* histograms;

See:

* :doc:`arrays_and_images`;
* :doc:`reshape_and_3d`.

*****
Setup
*****

See: `associating text editors with git`_.

*********
Exercises
*********

* :doc:`camera_exercise`;
* :doc:`anatomical_exercise`;
* :doc:`arteries_exercise`.

.. To cover
    Numpy allows creation of arrays
    An image is an array
    An array can be displayed with matplotlib
    An array can be reshaped
    An array can be transposed
    A 3D image is a 3D array
    A 3D array can be reshaped to 1D and back again
    Histograms.
    Operations on 1D (implicit) - mean, min, max
    Operations over axes (explicit) - mean, min, max
    np.lookfor
    Setting the colormap

**********************************
Reading and homework for next week
**********************************

* Read, learn, inwardly digest the `curious git`_ tutorial;
* Watch the videos at :doc:`git_videos`.


======
day_02
======

######################################
4D arrays, time series and diagnostics
######################################

*************************
4D arrays and time series
*************************

* Loading images with nibabel_;
* 4D images as collections of 3D images;
* getting volumes from 4D images;
* getting time-series from 4D images by slicing;

* intro page: :doc:`intro_to_4d`;
* exercise: :doc:`four_dimensions_exercise`.

*********************
Modules and functions
*********************

* intro :doc:`on_modules`.
* exercise::

    git clone https://github.com/psych-214-fall-2016/classwork
    cd classwork/day_02
    ipython

  then (in IPython)::

    run spm_funcs.py

****************************************
Introduction to the diagnostics exercise
****************************************

See :ref:`diagnostics-preparation`;

**********************************
Reading and homework for next week
**********************************

Reading is

* chapter 8 of Huettel et al 2014 :cite:`huettel2014functional`;
* `curious remotes`_ |--| the Curious Git section on using git to work with
  other repositories and other people.

Homework is to continue the diagnostics exercise.  See:
:ref:`outlier-detection-project`.


======
lab_02
======

################
Git walk-through
################

See: :doc:`git_walk_through`.


======
day_03
======

###########################
Vectors, projection and PCA
###########################

*****************
Vector projection
*****************

* `algebra of sums`_;
* `vectors and dot products`_;
* `vector projection`_.

*******************
numpy dot and outer
*******************

* :doc:`dot_and_outer`.

****************************
Principal component analysis
****************************

* background: `introduction to Principal Component Analysis`_;
* exercise: :doc:`pca_exercise`.

********
Deadline
********

You should have chosen a project mentor by the end of this week - see
:doc:`projects`.

**********************************
Reading and homework for next week
**********************************

* finish PCA exercise, with some github practice (see below);
* Huettel chapter 7 - :cite:`huettel2014functional`;
* continue the outlier competition - for October 10th;
* do the :doc:`github_pca_homework`.


======
lab_03
======

###########################################
Outlier detection and git / github workflow
###########################################

***************
Getting started
***************

* Refresher on git and remotes;
* Clone, fetch, push, pull;
* Github, forks and remotes;

Call the central repository: "upstream".

See :ref:`diagnostics-preparation` to start.

If you have not done this already, you will need to start by:

* Fork your *upstream* repository (for group 00, 01 or 02) to your *user*
  using the github interface;
* Clone your user copy;
* ``git log``;
* Move the data into the repository (see :ref:`diagnostics-preparation`).

*********
Exercises
*********

* Go to your upstream repository web-page:

    * Group 00 : https://github.com/psych-214-fall-2016/diagnostics-00
    * Group 01 : https://github.com/psych-214-fall-2016/diagnostics-01
    * Group 02 : https://github.com/psych-214-fall-2016/diagnostics-02

* I make a pull request to each repository;
* Select the Pull Requests tab and have a look at the changes I've suggested.
  Merge them.
* On your machine, in your user repository directory, do ``git log``.  Has
  anything changed?
* Do ``git fetch origin``.  Has anything changed?
* Add a remote for your upstream repository, e.g.::

    git remote add upstream https://github.com/psych-214-fall-2016/diagnostics-00

* Check your remotes with ``git remote -v``;
* Fetch information about your new remote with ``git fetch upstream``;
* Make a new branch to work on, starting at the position of
  ``upstream/master``::

    git branch for-exercise-1 upstream/master

* Do exercise 1 (from my pull-request). Read the comments at the top of
  ``scripts/calc_dvars.py``.  If you're running at normal speed, just do the
  first past of the exercises listed there.  If you're rushing ahead, try the
  other problems.
* When done, use Git to commit your changes;
* Send this new branch up to your user repository on github.  Type::

    git push origin for-exercise-1:for-exercise-1 --set-upstream

* Use the github web interface to make a pull request from this new branch to
  your upstream repository;
* Go again to your upstream repository web page.  Review the new pull request.
  Merge.
* Fetch the merged changes from your upstream repository with::

    git fetch upstream


======
day_04
======

###################################################
Correlation, regression, statistics on brain images
###################################################

******************
Project discussion
******************

* mentors;
* teams.

**********
Activation
**********

* :doc:`voxels_by_time`;
* :doc:`slicing_with_booleans`;
* :doc:`first_activation_exercise`.

**************************
Correlation and projection
**************************

* `vector angles`_;
* `correlation and projection`_;
* :doc:`pearson_functions` exercise.

.. _stimuli-exercise:

***********************
Correlation in practice
***********************

* :doc:`voxel_time_courses`;
* :download:`stimuli.py` file;
* :download:`test_stimuli.py` file;
* ::

    pip install pytest
    py.test test_stimuli.py

Then one of:

* :doc:`voxel_correlation_exercise`;
* :doc:`correlation_2d_exercise`.

******************************
Simple and multiple regression
******************************

* `introduction to the General Linear Model`_;
* simple regression;
* multiple regression with confounds.

**********************************
Reading and homework for next week
**********************************

* Do exercises from last week's lab: :ref:`git-workflow-exercises`;
* Continue work on outlier detection project for Monday next week.


======
lab_04
======

######################################
Git / github workflow, the Python path
######################################

*************************
What branch should I use?
*************************

* Never use ``master``;
* Make a new branch for each new bit of work.

*****************
Path manipulation
*****************

See: :doc:`path_manipulation`.

*******************************
Adding stuff to the Python PATH
*******************************

The mystery of where ``mymodule`` comes from, when you do ``import mymodule``.

See: :doc:`sys_path`.

*******************
Testing with assert
*******************

* :doc:`assert`.

****************
Some numpy stuff
****************

See: :doc:`numpy_logical`.

****************
Some live coding
****************

With guest editor Stéfan van der Walt:

* making issues;
* feature branches;
* pull requests;
* responding to comments on pull requests;
* merging pull requests with the "Merge" button on Github.

************
Git workflow
************

See: :doc:`git_workflow_exercises`.


======
day_05
======

##################################
Exploring the general linear model
##################################

***********
Python path
***********

* :doc:`using_pythonpath`;
* :download:`stimuli.py` file;
* :download:`test_stimuli.py` file;
* ::

    mkdir code
    mv stimuli.py code

* Install pytest if you haven't got it already::

    pip install pytest

* Show that the tests don't work yet::

    py.test test_stimuli.py

* Set Python path;
* Finally::

    mv test_stimuli.py code
    py.test code/test_stimuli.py

******************************
Simple and multiple regression
******************************

* finish going through the `introduction to the General Linear Model`_;
* we get the same results in R:

  .. code-block:: R

    psychopathy = c(11.416,   4.514,  12.204,  14.835,
                    8.416,   6.563,  17.343, 13.02,
                    15.19 ,  11.902,  22.721,  22.324)
    clammy = c(0.389,  0.2  ,  0.241,  0.463,
               4.585,  1.097,  1.642,  4.972,
               7.957,  5.585,  5.527,  6.964)
    res = lm(psychopathy ~ clammy)
    print(summary(res))

* :doc:`diag_inverse`;
* :doc:`subtract_mean_math`;
* :doc:`on_estimation_exercise`;
* on `matrix rank`_;
* :doc:`mean_test_example`.

*****************
Correlation again
*****************

* Make sure you have :download:`stimuli.py` and ``pearson.py`` on your Python
  path.  (``pearson.py`` comes from the exercise in :doc:`pearson_functions`);
* :doc:`correlation_2d_exercise`.

**********************************
Reading and homework for next week
**********************************

* Finish the :doc:`on_estimation_exercise` |--| see
  :doc:`github_glm_homework`;
* Do preliminary work on projects to prepare for project pitch next week.


======
lab_05
======

##################################
Some git, some multiple regression
##################################

*****************
Yay! A git review
*****************

Review is at :download:`git_short.pdf`.

Review should take about 10 minutes.

After you've worked through the review on your own, get into your groups, and
cross check your answers.  Decide who's got the answer right.

Then we'll go through the answers.

************************
The general linear model
************************

* `introduction to the general linear model`_.


======
day_06
======

#################################
Project pitch, ANOVA with the GLM
#################################

***************
Project pitches
***************

Pitches for your project proposals - see :doc:`projects`.

***********************************************
t tests and ANOVA with the general linear model
***********************************************

* :doc:`diag_inverse`;
* on `matrix rank`_;
* :doc:`mean_test_example`;
* :doc:`hypothesis_tests`;
* :doc:`on_dummies_exercise`.

********************************
The neural and hemodynamic model
********************************

* the neural and hemodynamic model;
* the concept of a hemodynamic response function (HRF);
* using convolution with the HRF to make a BOLD regressor;
* :doc:`convolution_background`;

**********************************
Reading and homework for next week
**********************************

* Finish the :doc:`on_dummies_exercise` |--| see
  :doc:`github_dummies_homework`;
* Review the `tutorial on convolution`_;
* Review Huettel chapter 7 - :cite:`huettel2014functional` |--| especially the
  parts on the hemodynamic response function.


======
lab_06
======

#######################
More on github workflow
#######################

* reviewing code;
* raising issues;
* responding to issues with pull requests.


======
day_07
======

######################################
The HRF, modeling and statistical maps
######################################

********
Teaching
********

* `tutorial on convolution`_;
* :doc:`convolution_background`;
* :doc:`make_an_hrf_exercise`;
* :doc:`hrf_correlation_exercise`.
* :doc:`model_one_voxel`;
* :doc:`test_one_voxel`;
* :doc:`multi_multiply`;
* :doc:`multi_model_exercise`;
* :doc:`non_tr_onsets`;
* `Tutorial on correlated regressors`_;

.. stuff we probably won't have time for:

    * modeling FMRI signal with multiple regression and the BOLD regressors;
    * investigating assumptions behind the HRF and linear time invariance.
    * smoothing;
    * t contrasts;
    * using multiple regressors
    * allowing for different onsets with the HRF temporal derivative;
    * investigating power and bias for correlated regressors;
    * modeling the baseline;
    * selecting models;

**********************************
Homework and reading for next week
**********************************

* :doc:`multi_model_homework`;
* `Tutorial on correlated regressors`_;
* `Introduction to smoothing`_;
* `Smoothing as convolution`_.


======
lab_07
======

######################################
F tests; convolution; project template
######################################

*******
F tests
*******

* :doc:`hypothesis_tests`;
* :doc:`on_dummies_exercise`.

***********
Convolution
***********

* `tutorial on convolution`_;
* the neural and hemodynamic model;
* the concept of a hemodynamic response function (HRF);
* using convolution with the HRF to make a BOLD regressor;
* :doc:`convolution_background`;
* :doc:`make_an_hrf_exercise`;
* :doc:`hrf_correlation_exercise`.

****************
Project template
****************

See the `course github organization`_.


======
day_08
======

##############################
Multiple comparison correction
##############################

**********
Logistics
**********

* project presentations next week;
* proposal to redistribute 12 percentage points from homework to:

    * project: 50% to 60%
    * participation : 25% to 27%

 See: :doc:`logistics`.

* solutions to :doc:`dummies exercise <on_dummies_exercise>` at :doc:`dummies
  solutions <on_dummies_solution>`.

*******************
Choosing directions
*******************

* on code quality:

  http://www.samueljohnson.com/editing.html#536

    "I would say to Robertson what an old tutor of a college said to one of
    his pupils: 'Read over your compositions, and where ever you meet with a
    passage which you think is particularly fine, strike it out.'"

    Samuel Johnson in James Boswell's "Life of Samuel Johnson".

  There are some automated metrics, of which, be careful::

    pip3 install --user radon
    radon cc .

* learning to code well:

  * read other people's code;
  * review code;
  * make other people review your code;
  * pair coding.
  * "is this the right way to think of the problem?";
  * "have I expressed my thinking clearly in this code?";
  * "what guarantee can I give that the code is correct?;
  * "under what circumstances is the code correct?".

********
Teaching
********

* testing and coverage on the project repositories:

  Test results:

  * https://travis-ci.org/psych-214-fall-2016/project-red
  * https://travis-ci.org/psych-214-fall-2016/project-blue

  Test coverage:

  * https://codecov.io/gh/psych-214-fall-2016/project-red
  * https://codecov.io/gh/psych-214-fall-2016/project-blue

.. _glmtools-exercise:

GLM and testing exercise
========================

* testing, and t test volumes:

    * :doc:`validate_against_scipy`;
    * pdb++ : ``pip3 install --user pdbpp``;
    * Exercise::

        git clone https://github.com/psych-214-fall-2016/glmtools
        cd glmtools
        pip3 install --user --editable .
        py.test glmtools

Multiple comparison correction
==============================

* the `Bonferroni correction`_;
* thresholding with `Random fields`_;
* thresholding with the `False Discovery Rate`_;

.. other-stuff

    * family-wise error and FDR;
    * permutation and parametric;
    * small volume correction and ROI analysis.

**********************************
Reading and homework for next week
**********************************

* Prepare project presentations;
* `slice timing correction`_;
* `Rotation in 2D`_
* `optimizing spatial transformations`_.


======
day_09
======

##################################
Slice timing and motion correction
##################################

*****************
Project proposals
*****************

Presentation of project proposals and feedback.

We discussed modeling the baseline (e.g. fixation) trials, and we looked at
the `tutorial on correlated regressors`_.

********
Teaching
********

See the `diagnostics analysis code
<https://github.com/psych-214-fall-2016/fmri-designs>`_ for an example of code
organization and testing.

* :doc:`otsu_threshold`;
* Correction with the `false discovery rate`_;
* `slice timing correction`_;
* :doc:`slice_timing_exercise`;
* how to do slice timing;
* when to use slice timing;
* slice timing artefacts.

********************
Reading and homework
********************

* `Rotation in 2D`_
* `Coordinate systems and affine transforms`_;
* A tutorial on `mutual information`_.


======
lab_09
======

####################################################
Multiple comparison correction, whole brain analysis
####################################################

* :doc:`whole_image_statistics`;
* :doc:`otsu_threshold`;
* the `Bonferroni correction`_;
* thresholding with `Random fields`_;
* `introduction to smoothing`_.


======
day_10
======

######################################
Affine and cross-modality registration
######################################

*******
Grading
*******

See: :doc:`project_grading`.

********
Teaching
********

* :doc:`coding_style`;
* finishing `optimizing spatial transformations`_;
* :doc:`rotation_2d_3d`;
* :doc:`resampling_with_ndimage`;
* :doc:`more_on_rotation_exercise`;
* :doc:`optimizing_rotation_exercise`;
* :doc:`image_header_and_affine`;
* :doc:`images_and_affines`;
* :doc:`reslicing_with_affines_exercise`;
* `mutual information`_.

.. other-stuff:

    * using the image affine for storing the results of registration;
    * cost functions for registration across imaging modalities;
    * rigid-body, linear, affine registration;
    * implementing an affine registration;
    * affine registration in SPM.

********************
Reading and homework
********************

* `Introduction to spatial normalization <https://vimeo.com/126900408>`_
* 15 minute section from the `lecture on spatial processing by Ged Ridgway
  <https://www.ucl.ac.uk/stream/media/swatch?v=1d42446d1c34>`_ - section on
  registration between subjects is from 35.00 - 50.07.


======
lab_10
======

###################################
Optimization and image registration
###################################

**********
Background
**********

* `functions are objects`_;
* `global scope`_;
* :doc:`list_comprehensions`.

**************************
Registration, optimization
**************************

* `optimizing spatial transformations`_.

*********************
Reading for next week
*********************

* `Rotation in 2D`_
* `coordinate systems and affine transforms`_.


======
day_11
======

##########################
Cross-subject registration
##########################

*********
Logistics
*********

* problems from projects;

********
Teaching
********

* :doc:`saving_images`;
* SPM coregistration:

  * copy the structural::

      cp ds107_sub012_highres.nii a_structural.nii

  * create the mean of the functional image::

    >>> import nibabel as nib
    >>> img = nib.load('ds107_sub012_t1r2.nii')
    >>> mean_vol = img.get_data().mean(axis=-1)
    >>> mean_img = nib.Nifti1Image(mean_vol, img.affine, img.header)
    >>> nib.save(mean_img, 'mean_functional.nii')

  * run coregistration in SPM.

* running cross-subject normalizations in SPM;
* making a distortion field in SPM;
* applying the SPM distortion field;

    * :doc:`numpy_squeeze`;
    * :doc:`numpy_transpose`;
    * :doc:`numpy_meshgrid`;
    * :doc:`map_coordinates`;
    * :doc:`applying_deformations_exercise`.

********************
Reading and homework
********************

Working on projects.


======
lab_11
======

######################
Affine transformations
######################

********
Revision
********
* `coordinate systems and affine transforms`_.
* :doc:`rotation_2d_3d`;

**********
Background
**********

See :cite:`Brett2002`;

* the MNI templates;
* review of spatial processing:

    * slice time correction;
    * motion correction;
    * coregistration of structural to functional;
    * coregistration of structural to template;
    * resampling of functional, stuctural to template;
    * smoothing.

* Matching structural to functional with `mutual information`_.

* :doc:`nibabel_affines`;
* :doc:`resampling_with_ndimage`;
* :doc:`what_extra_transform_exercise`;
* :doc:`numpy_random`;
* :doc:`diagonal_zooms`.

*********
Exercises
*********

* :doc:`optimizing_affine_exercise`.


======
day_12
======

####################################
Exploring cross-subject registration
####################################

*************
Presentations
*************

Problems from projects.

********
Teaching
********

Registration
============

* nibabel image viewer:

  .. code-block:: ipython

    In [1]: import nibabel as nib
    In [2]: import matplotlib.pyplot as plt
    In [3]: %matplotlib
    In [4]: structural = nib.load('ds114_sub009_highres.nii')
    In [5]: functional = nib.load('ds114_sub009_t2r1.nii')
    In [6]: func_viewer = functional.orthoview()
    In [7]: struct_viewer = structural.orthoview()
    In [8]: func_viewer.link_to(struct_viewer)

* :doc:`dipy_registration`;
* example registration problem |--| :doc:`anterior_cingulate`.

********************
Reading and homework
********************

Working on projects.


======
lab_12
======

######################
Scripting using nipype
######################

* :doc:`introducing_nipype`;
* :doc:`spm_slice_timing_exercise`;
* the rest of the analysis in SPM:

  * motion correction (registration between first image and later images in
    time series);
  * coregistration (registration between structural and functional);
  * spatial normalization (registration between structural and template);
  * reslicing (resampling images in to space of template);
  * smoothing;

* :doc:`full_scripting`.


