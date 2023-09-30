# thol_scripts

My personal collection of 2HOL related scripts. Some scripts goes into their own directories.
View CHANGELOG.MD in them to see what changed.

## printObjectSprites.py

Print all relevant sprites of an object via its description.

For more info, use `./printObjectSprites.py --help`.

Examples:
```sh
# load sprite image into gimp
./printObjectSprites.py 'polar bear skin' ../OneLifeData7/ | xargs gimp

# get count of sprites from an object description which contains the string 'apple'
./printObjectSprites.py '.*apple.*' ../OneLifeData7/ | wc -l

# get all sprites from object with description that starts with 'female' (eve)
./printObjectSprites.py --sorted 'female.*' ../OneLifeData7/
```

## printRemoteObjectFiles.sh

Print all relevant object files directly OneLifeData7 Github repository without
downloading the whole repo first.

```sh
# the script defaults to printing from master branch

# get all object files and print the count
./printRemoteObjectFiles.sh | wc -l

# get from ff4abd4 commit
./printRemoteObjectFiles.sh ff4abd4

# get from a pinned release tag
./printRemoteObjectFiles.sh 2HOL_v20307
```
