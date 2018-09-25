##How to delete sensitive folder
+ 1. create a new csv file name test.csv and commit to the file
![Alt text]()
![Alt text]()
+ 2. pull to local repository
>run git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch HW3_xj655/Lab3_xj655/test.csv' --prune-empty --tag-name-filter cat -- --all
>git push origin --force --all
>the screenshot for history after delete
![Alt text]()
