# thol_scripts

My personal collection of 2HOL related scripts.

## printObjectSprites.py

Print all relevant sprites of an object via its description.

For more info, use `./printObjectSprites.py --help`.

Examples:
```sh
# load sprite image into gimp
./printObjectSprites.py 'polar bear skin' ../OneLifeData7/ | xargs gimp

# get count of sprites from an object description which contains the string 'apple'
./printObjectSprites.py '.*apple.*' ../OneLifeData7/ | sort | uniq | wc -l

# get all sprites from object with description that starts with 'female' (eve)
./printObjectSprites.py 'female.*' ../OneLifeData7/ | sort | uniq
```
