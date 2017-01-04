> Resume for: https://gist.github.com/chrisjacob/825950

1. Create master repository
2. Following commands this below

```bash
(master) $ git clone https://github.com/agusmakmun/csf-blocker.git
(master) $ nano .gitignore # add `docs/` inside it.
(master) $ git add .
(master) $ git commit -m "exluded the docs from master branch"
(master) $ git push origin master
```

> Don't forget to add `docs/` into your `.gitignore` _(master)_. 
> This to makesure the folder of `/docs/` isn't included whenever you push at master branch.

```
(master) $ cd csf-blocker/
(master) $ git branch                               # to check the exited branch `default: master`
(master) $ mkdir docs/                              # example sub folder
(master) $ cp -R .git/ docs/                        # to copying default `.git` config from master.
(child)  $ cd docs/                                 # to go to `/csf-blocker/docs/`
(child)  $ git branch gh-pages                      # to create new branch
(child)  $ git checkout gh-pages                    # to switch as `gh-pages`
(child)  $ touch .gitignore                         # initial .gitignore for `gh-pages`
                                                    # and then, create your project.
(child)  $ git add .                                # add your `.gitignore` and others.
(child)  $ git commit -m 'Initial launch for docs'  # commit name
(child)  $ git push origin gh-pages                 # to push to your gh-pages branch
```

And then, checkout at your branch, example: 
  * all branch: https://github.com/agusmakmun/csf-blocker/branches
  * gh-pages branch: https://github.com/agusmakmun/csf-blocker/tree/gh-pages

To switch as `master` branch again, you should do this:

```bash
(child)  $ cd ..                                                    # to back to your master project
(master) $ git checkout master                                      # to switch as master branch
                                                                    # and then, change your master project.
(master) $ git add .                                                # to add your changed files.
(master) $ git commit -m "I'm come back in master"                  # commit name
(master) $ git push origin master                                   # to push to your master branch
```

> If your `gh-pages` is as github pages, the domain name is `agusmakmun.github.io/csf-blocker`
