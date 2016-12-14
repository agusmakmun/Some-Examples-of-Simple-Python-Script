### GIT Collaboration

```bash
1. Fork the project to your git account, (eg: github, bitbucket, gitlab, etc..)

$ git remote add upstream git@github.com:codenesia/repo-name.git   # add remote upstream
$ git remote add origin git@github.com:YOUR_NAME/repo-name.git     # add remote origin (fork repo).
$ git remote remove origin     # Remove origin if already exist and repeat the above steps.

$ git add .                           # adding your added/changed file.
$ git commit -m "YOUR COMMIT NAME"    # adding comment
$ git push -u origin master           # push to your fork repo.

8. Create pull request.

$ git fetch upstream           # fetch from master
$ git merge upstream/master    # merged to local
$ git push origin              # push to fork repo

$ git stash  # to force accept from master.
```
