**`git init`**: initialize project to use git

**`git clone <repository-url>`**: clones repo from url

**`git checkout -b <new-branch>`**: create new branch and switch to it

**`git add .`**: select all changes to be saved

(`git add *`: select all changes in current working directory (not subdirectories and dotfiles))

(**`git add <filename>`**: select file to save changes made on file)

**`git commit -m "<message>"`**: save changes with message

**`git push origin main`**: push changes to github main

**`git push origin <other-branch>`**: push changes to github other-branch

**`git pull origin main`**: pull changes from github main

**`git status`**: display status of changes

**`git log`**: display previous changes (and hashes)

**`git checkout <commit hash>`**: travel back to old commit


## Typical Git-GitHub Workflow

1. **Clone the repository** (from GitHub)
```
git clone <repository-url>
```

2. **Navigate into project repo**
```
cd <repository-name>
```

3. **Create development branch**
```
git checkout -b development
```

4. **Open project in VS Code to edit**
```
code .
```

5. **Make changes**

6. **Stage changes** (select what to commit)
```
git add .
```

7. **Commit changes**
```
git commit -m "Description of changes"
```

8. **Push changes to remote repo**
```
git push origin development
```

9. **Pull request** (aka poule request) (on GitHub)
Base branch: `main`/`master` ; compare with: `development`

10. **Review poule request** (on GitHub)

11. **Merge poule request** (on GitHub)

12. **Clean up local repo**
	1. `git checkout main`
	2. `git pull origin main`
	3. `git branch -d development`
