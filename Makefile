.RECIPEPREFIX = >

.PHONY: app
app: 
> poetry run python3 ine5420/main.py

# run pyuic5 -x ... to get an executable py file
.PHONY: convert
convert: 
> poetry run pyuic5 $(ui_file) -o $(py_file)

.PHONY: test
test:
> poetry run pytest
