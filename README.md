## Template API Flask ##
Template com o conjunto de artefatos iniciais para criação de um serviço em python.

---

#### Configurações iniciais de ambiente
1. Instale um Virtual Environments do python.
```shell 
sudo apt-get install python3-venv 
```
2. Instale o pacote requests
```shell
pip install -U requests
```

3. Instale o pacote de CORS 
```shell
pip install -U flask-cors
```
#### Docker
> Nota: É importante que tenha instalado e configurado em seu ambiente o <a href="https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04">Docker</a>. 

#### Executando

1. Instalar dependências do projeto
```shell
docker build .
```
2. Executar o programa principal e incializar o servidor
```shell
python3 run.py
```
