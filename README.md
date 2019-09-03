# django-rest-example

API de cadastro/consulta de músicas, feito com Django-rest-framework, seguindo [este](https://medium.com/@marcosrabaioli/criando-uma-api-rest-utilizando-django-rest-framework-parte-1-55ac3e394fa) tutorial.

Itens que aprendi aqui:
- Instalação/configuração
- Criando modelo e serializer
- Criando as views
- Adicionando autenticação (do tipo sessão)
- Adicionando filtros

## Instruções:

### Criar e inicializar virtualenv

```bash
$python -m venv venv
$source venv/bin/activate
```

### Instalar dependências:

```bash
$pip install -r requirements.txt
```

### Fazer as migrações
```bash
$python manager.py migrate
```

### Criar o superuser
```bash
$python manager.py createsuperuser
```

### Iniciar o server
```bash
$python manager.py runserver
```
