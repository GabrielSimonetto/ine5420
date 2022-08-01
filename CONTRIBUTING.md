Isso aqui vai ser um rascunho por um tempo, só pra colocar uns workflow importante.

# Fazer incrementos na UI

1) rodar `designer -qt5` no terminal
    (ou qualquer outro jeito de entrar no QtDesigner)
2) abrir seu checkpoint desejado em `./src/qt_designer`
4) salvar o novo checkpoint na pagina com um numero de série, e um nome descritivo de o que tem de diferente
5) substituir nosso entrypoint python usando `pyuic5 -x <checkpoint.ui> -o <target.py>`, ou usando `make convert ui_file=<checkpoint.ui> py_file=<target.py>`

O `-x` faz com que o arquivo seja executavel, isso provavelmente nao vai ser bom quando a gente estiver colocando funcionalidades no main.py, mas eu nao achei um jeito simples de vincular a UI com o main antes.