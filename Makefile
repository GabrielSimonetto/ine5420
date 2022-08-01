.RECIPEPREFIX = >

.PHONY: run
run: 
> poetry run python src

.PHONY: install
install: 
> poetry install

# run pyuic5 -x ... to get an executable py file
.PHONY: convert
convert: 
> poetry run pyuic5 $(ui_file) -o $(py_file)
