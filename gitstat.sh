#!/bin/bash

function gitstat_myself() {
    git log --author="$(git config --get user.name)" --pretty=tformat: --numstat | gawk \
        '{ add += $1 ; subs += $2 ; loc += $1 - $2 }\
        END { printf "added lines: %s removed lines : %s total lines: %s\n",add,subs,loc }' -
    git log --author="$(git config --get user.name)" --pretty='%aN' | uniq -c | gawk '{commitcount = $1} \
    END {printf "commit count: %d", commitcount}'

}

function gitstat_commit_sort() {
    git log --pretty='%aN' | sort | uniq -c | sort -k1 -n -r
}
