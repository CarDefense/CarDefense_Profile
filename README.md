# CarDefense Profile
![CI status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Django](https://img.shields.io/badge/django-2.1-blue.svg)
![Python](https://img.shields.io/badge/python-3.6-ff69b4.svg)

## Microsserviço de gerencimanento de usuários

O microsserviço de usuários é utilizado no aplicativo CarDefense para gerenciar a autenticação de usuários.

## Instalação 

### Requisitos 
Para instalação do projeto você deve ter instalado:
* Docker
* Docker Compose

### Como instalar

1 - Clone o repositório
2 - Entre a pasta do projeto
3 - Rode o comando:
```
sudo docker-compose up
```
4 - Acesse localhost:8000

Para acessar o container da aplicação use o seguinte comando:
```
sudo docker exec -it cardefenseprofile_web_1 bash
```

Para ver todos os containers rodando na sua máguina use o seguinte comando:

```
sudo docker ps
```

## Outros microsserviços 
* [CarDefense Notification](https://github.com/CarDefense/CarDefense_Notification)
* [CarDefense Cars](https://github.com/CarDefense/CarDefense_Cars)
* [CarDefense Gamification](https://github.com/CarDefense/CarDefense_Gamification)





