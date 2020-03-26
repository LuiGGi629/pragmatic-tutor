man grep

grep "java" ./.3T/log.txt

# whole words
grep -w "java" ./.3T/log.txt

# grep is case sensitive. We can tell it via -i to not be
grep -wi "Java" ./.3T/log.txt

# line number
grep -win "Java" ./.3T/log.txt

# context where match was found. (4) Lines behind my match
grep -win -B 4 "DataMan" ./.3T/log.txt
# after
grep -win -A 4 "DataMan" ./.3T/log.txt

# context surrounding our match
grep -win -C 2 "DataMan" ./.3T/log.txt

# search multiple files at once
grep -win "DataMan" ./.3T/*
grep -win "DataMan" ./.3T/*.txt

# search in sub dir. be careful with recursive searches
grep -winr "Pandas" .

# return only files which contain match
grep -wirl "DataMan" ./.3T/
# num of matches in each file
grep -wirc "DataMan" ./.3T/

# we can pipe the output of other commands into grep
history | grep "git commit"

history | grep "git commit" | grep "async"

# advanced searches using regexp (phone numbers)
grep "...-...-...." data.txt
grep "\d\d\d-\d\d\d-\d\d\d\d" data.txt

































