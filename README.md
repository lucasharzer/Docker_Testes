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
docker build -t <nome_imagem> .
``` 

- Executar a imagem
```bash
docker run -it --rm --name=<nome_contêiner> <nome_imagem>
```

# Resultados

Pasta Simples
<span>
    <img src="https://user-images.githubusercontent.com/85804895/222618387-7ea489bf-800d-4c91-85e3-6961b1221734.png">
</span>

<span>
    <img src="https://user-images.githubusercontent.com/85804895/222618477-4363487f-8f37-4b54-af3f-83f5fa9f3d7a.png">
</span>

Pasta Playwright
<span>
    <img src="https://user-images.githubusercontent.com/85804895/222929412-518af896-65a9-403d-a0c9-d5521a93fb51.png">
</span>

<span>
    <img src="https://user-images.githubusercontent.com/85804895/222929431-2e4fb765-2f46-46ff-9ff0-e35bd4499562.png">
</span>

Pasta Selenium (Chrome e Firefox)
<span>
    <img src="https://user-images.githubusercontent.com/85804895/223288680-3b3e83da-f417-40ef-a015-aef7c1a5b21d.png">
</span>

<span>
    <img src="https://user-images.githubusercontent.com/85804895/223289907-e68d5eba-4023-48b8-bdf1-f4913f6ffdef.png">
</span>

