# Testando aplicações dentro do Docker
Construido imagens e executando contêineres dentro do Docker

# Comandos

- Versão do Docker
```bash
docker --version
```

- Ajuda com comandos
```bash
docker <comando> --help
```

- Visualizar imagens
```bash
docker images
```

- Visualizar Contêineres em execução
```bash
docker ps
```

- Visualizar todos os Contêineres
```bash
docker ps -a
```

- Criar uma imagem
```bash
docker build -t <nome da imagem> .
``` 

- Executar a imagem
```bash
docker run -it --rm --name=<nome do contêiner> <nome da imagem>
```

# Resultados

Pasta Simples
<span>
    <img src="https://user-images.githubusercontent.com/85804895/222618387-7ea489bf-800d-4c91-85e3-6961b1221734.png">
</span>

<span>
    <img src="https://user-images.githubusercontent.com/85804895/222618477-4363487f-8f37-4b54-af3f-83f5fa9f3d7a.png">
</span>

