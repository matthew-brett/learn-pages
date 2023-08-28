## Recording

[Week 4 session 1 recording](https://numfocus-org.zoom.us/rec/share/9K9OpxVP_9bu4AWA5JUpz1QspJB4QSjlAdQnEdlssIP5SZzf4lPj5txao_073QGs.nM-1yQNsqJDcC-aB)

## Schedule and plan

* More on four dimensions
* Modules and functions

### Indexing and four dimensions

* [Indexing with
  Booleans](https://textbook.nipraxis.org/boolean_indexing.html)
* [Boolean indexing in more
  dimensions](https://textbook.nipraxis.org/boolean_indexing_nd.html)
* [Introduction to four dimensions](https://textbook.nipraxis.org/intro_to_4d)
* [Four dimensions
  exercise](https://hub.nipraxis.org/hub/user-redirect/git-pull?repo=https%3A//github.com/nipraxis/four_dimensions&subPath=four_dimensions.ipynb)

## Homework

There is a well-done video on Git and Github on YouTube, link below.

Here are a few notes before you watch the video.

The video concentrates on the use of Git / Github for programmers, but all the
same things apply to scientists and academics writing collaborative projects
and papers.

It starts very basic, but bear with, it quickly gets on the specific stuff we
have not covered elsewhere, on using Git with Github.

The author is using the old-style default branch naming in Git, where the
default branch is called `master`.  The default branch, for modern Git, is now
called `main`.  Just read `main` for `master` throughout.

I would set up your Github account with an SSH key following the [Github
instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
before you start the video.  Although the video suggests that having no
passphrase for your SSH key is OK, we would not recommend that.  We suggest you
do in fact have a reasonably long (but memorable) SSH key passphrase.

The video starts using the terminal from within VSCode.  The author says this
later, but this is just the same as using terminal outside VSCode, so if you
are not using VSCode, just type the same commands in the terminal.  In fact,
I would recommend using the terminal outside VSCode even if you are using
VSCode, at least at first.

The video uses the `-m` flag to `git commit` to provide a commit message and
maybe a description.  We suggest you don't do that, and you set up your editor
to work with Git, so when you type `git commit`, Git will open your editor for
you to type a message.  See below for how to do this.

#### Setting your default editor for Git

The usual default editor for Git is Vim, so if you want that, you don't need to change anything.  If you don't then:

* [General instructions for some common editors](https://koenwoortman.com/git-change-default-editor/) including Emacs and VSCode.
* [For
  VSCode](https://dev.to/deadlybyte/make-vs-code-your-default-git-editor-j6d)
* [For PyCharm](https://clt.champlain.edu/kb/configuring-git-with-pycharm)

#### The video

The video is [Git and Github for
Beginners](https://www.youtube.com/watch?v=RGOj5yH7evk).

#### After the video

To make sure you understand most of the material in the video, do the
following:

*   **Fork** the repository at <https://github.com/nipraxis/first-pull-request>
    using the "Fork" button towards the top right.
*   **Clone** your fork of this repository to your computer.
*   **Make and checkout a new branch** called `spm-funcs-fixes`.
*   Make the changes given in the instructions at the top of the `spm_funcs.py`
    file.
*   `git add` these changes, then `git commit` the changes.
*   **Push** the changes from this branch up to your fork.  Make sure you
    are pushing the new branch.
*   Do a **Pull request** from this new branch to the original (base)
    repository `master` branch at
    <https://github.com/nipraxis/first-pull-request>
*   We will review your pull request!

### The Markdown tutorial

Markdown is the standard way of writing nicely formatted text on many
platforms, including on Github, and in the Jupyter notebook.  You will see it
in many places, and you will find yourself using it often — for example, in
Jupyter text cells.  Get used to writing Markdown by doing the [Markdown
tutorial](https://www.markdowntutorial.com).

### Voxel exercise

* [Voxel time course
  exercise](https://hub.nipraxis.org/hub/user-redirect/git-pull?repo=https%3A//github.com/nipraxis/first_activation_exercise&subPath=first_activation.ipynb)

## That's it.

That's it for this session.
