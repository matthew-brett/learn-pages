The *second session* is the Thursday or Friday session — whichever you have
chosen to join.
These are the notes for the second session, for week 2.

We will update them before and after the session, to please keep checking back for updates.  Just refresh the page in your browser to get updates.

* Thursday 15:00 UTC session: [Thursday Zoom
  link](https://bham-ac-uk.zoom.us/j/85697917669?pwd=R09RRVoxSXl5YnVjVDVuN3NDM2lCdz09)
* Friday 18:00 UTC session: [Friday Zoom link](https://bham-ac-uk.zoom.us/j/82522323304?pwd=VjRRWDNkZjF5clBDd3FNNGJWcTUyZz09).

## Recording

[Link to Thursday recording](https://bham-ac-uk.zoom.us/rec/share/ZJ3xT8aTQlF5IImafSNW58-2oDbfc2xchK_P1NNnG-GK9wSzJHtl3QrVNF3kY6XP.A_11GhqJI1XpX_5S?startTime=1651158428000)

## Schedule and plan

* The final project.
* Start of command-line / text editor workflow.

### Modules and functions

Quick walk through of the [Four dimensions
exercise](https://hub.nipraxis.org/hub/user-redirect/git-pull?repo=https%3A//github.com/nipraxis/four_dimensions&subPath=four_dimensions.ipynb)

Then see [on_modules](https://textbook.nipraxis.org/on_modules).

### Exercise

```
git clone https://github.com/nipraxis/first_module
cd first_module
ipython
```

then (in IPython):

```
run spm_funcs.py
```

### Reading and homework for next week

There is a well-done video on Git and Github on Youtube, link below.

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
are not using VSCode, just type the same commands in the terminal.

The video uses the `-m` flag to `git commit` to provide a commit message and
maybe a description.  We suggest you don't do that, and you set up your editor
to work with Git, so when you type `git commit`, Git will open your editor for
you to type a message.

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
*   Make the same edits you made when you did this exercise as the
    `first_module` exercise.  The instructions are in the `spm_funcs.py` file.
*   `git add` these changes, then `git commit` the changes.
*   **Push** the changes from this branch up to your fork.  Make sure you
    are pushing the new branch.
*   Do a **Pull request** from this new branch to the original (base)
    repository `master` branch at
    <https://github.com/nipraxis/first-pull-request>
*   We will review your pull request!

## That's it.

That's it for this session.
