Esta pasta faz parte de um ambiente virtual do Python (`venv`) criada em um Linux. Para que você possa executar corretamente todos os códigos, é recomendável a criação ou ativação do ambiente virtual.

Se você estiver no Windows você deve [criar um novo ambiente virtual](https://docs.python.org/pt-br/3/tutorial/venv.html), levar os códigos para a pasta do ambiente criado, e instalar as bilbiotecas necessárias.

Para criar um novo ambiente virtual Python (vale para Linux e Windows) escreva no terminal:

`python -m venv nome_do_ambiente`

Para ativar o ambiente, se você estiver no Windows, digite no terminal:

`nome_do_ambiente\Scripts\activate.bat`

Assim que você ativar o ambiente virtual, você poderá perceber que no terminal a primeira informação em cada linha é `(nome_do_ambiente)`. Com o `venv` ativado você poderá baixar outras bibliotecas e criar códigos que estarão restritos a ele, ou seja, não afetarão outros projetos. 

Com seu ambiente ainda ativado, para instalar as mesmas bibliotecas utilizadas pelo `venv` `using_pandas`, basta escrever no terminal:

`pip install -r requirements.txt`

Quando você tiver terminado seus estudos, para desativar o ambiente, escreva no terminal (também vale para Linux e Windows):

`deactivate`

Se você estiver no Linux, bastará ativar o `venv`, uma vez que a pasta `using_pandas` é um ambiente virtual criado nesse OS, e todos os arquivos estão upados. Para ativar, digite no terminal:

`source using_pandas/bin/activate`