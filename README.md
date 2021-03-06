# JusrisfAI Challenge

Este projeto foi criado para o desenvolvimento de um desafio de Web Scraping para automação de consultas de leis.

Este desafio foi desenvolvido pela start-up JurisfAI.

## Getting Started

Para executar corretamente o projeto em sua máquina, siga as instruções a seguir.

## Prerequisites

Você precisará de Python 3 e pip. É altamente recomendado utilizar ambientes virtuais
com o virtualenv e o arquivo `requirements.txt` para instalar os pacotes dependências
do desafio:

```bash
pip3 install virtualenv
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
```

Windows

```bash
pip3 install virtualenv
virtualenv ..\venv -p python3
..\venv\Scripts\activate
pip install -r requirements.txt
```

Quando finalizado, você pode desativar o ambiente virtual do virtualenv com:

```bash
deactivate
```

## Running the code

Para executar o projeto basta rodar o comando a seguir:

```
python scraping_rules.py
```

Ao rodar o mesmo, será necessário informar alguns parâmetros para que o programa realize a consulta.

## Contributing

- Faça um fork desse repositório;
- Cria uma branch com a sua feature: `git checkout -b minha-feature`;
- Faça commit das suas alterações: `git commit -m 'feat: Minha nova feature'`;
- Faça push para a sua branch: `git push origin minha-feature`.

## License

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](https://github.com/JedersonLuz/jusrisfai_challenge/blob/master/LICENSE) para mais detalhes.
