speedevo
==============

#### Esse é um pacote que faz teste de velocidade na sua internet e gera um arquivo em .xlsx com as informação do teste.

## Instalação:

```
pip install speedevo
```

## Como usar:

```
from speedevo import speedevo
s = speedevo.Speedevo()
s.speed_test('nomeDoArquivo')

Para a utilização do line e histogram, precisa antes ser gerado o arquivo .xlxs do speed_test
s.line('nomeDoArquivo')
s.histogram('nomeDoArquivo')
```
