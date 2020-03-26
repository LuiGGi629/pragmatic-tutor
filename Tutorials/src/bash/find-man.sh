man find

find .

find Desktop/

find . -type d

find . -type f

find . -type f -name "Shoper.py"

find . -type f -name "Shop*"

find . -type f -iname "shop*"

find . -type f -name "*.py"

# files modified less than 10 mins ago
find . -type f -mmin -10
find . -type f -mmin +10

find . -type f -mmin +1 -mmin -5

# less than 20 days ago
find . -type f -mtime -20
find . -type f -mtime +20

# search by file size G, M, k
find . -size +5M

# search for currently empty files
find . -empty

# search based on permissions
find . -perm 777

# perform action on our results
# 1. change the user and group for every file and dir within a folder
find Tests/ -exec chown luigi:test-data {} +
# 2. Set dir permission to 775 and file permission to 664
find Tests/ -type d -exec chmod 775 {} +
find Tests/ -perm 775

find Tests/ -type f -exec chmod 664 {} +
find Tests/ -perm 664

# delete all img that end with .jpg in curr dir
find . -type f -name "*.jpg" -maxdepth 1

find . -type f -name "*.jpg" -maxdepth 1 -exec rm {} +








































