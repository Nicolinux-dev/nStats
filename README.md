# nStats

**nStats** é um monitor de recursos do sistema desenvolvido em Python para acompanhar, diretamente pelo terminal, o uso de **CPU, memória RAM e disco** em sistemas Linux.

O projeto foi desenvolvido para Linux, sistema utilizado durante seu desenvolvimento, com foco em simplicidade, baixo consumo de recursos e visualização rápida das principais informações do sistema.

## 📊 Recursos

Atualmente, o nStats apresenta:

### CPU

* Uso da CPU em porcentagem
* Frequência de cada CPU lógica
* Quantidade de núcleos físicos
* Quantidade de núcleos lógicos

### Memória RAM

* Uso da RAM em porcentagem
* Quantidade de RAM utilizada
* Quantidade de RAM disponível

### Disco

* Uso do disco em porcentagem
* Espaço utilizado
* Espaço livre
* Espaço total

### Atualização automática

As informações do sistema são atualizadas automaticamente a cada 2 segundos enquanto o programa está em execução.

## 🛠️ Tecnologias

O projeto utiliza:

* Python 3
* [psutil](https://pypi.org/project/psutil/)
* `subprocess` — biblioteca padrão do Python

## 🐧 Compatibilidade

Atualmente, o **nStats é desenvolvido e testado em Linux**.

> O suporte para outros sistemas operacionais poderá ser considerado futuramente.

## 📋 Requisitos

Para executar o nStats, você precisa ter:

* Uma distribuição Linux
* Python 3
* `pip`

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/Nicolinux-dev/nStats.git
cd nStats
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Executando

Execute o programa com:

```bash
python3 src/main.py
```

Após iniciar, o nStats exibirá as informações de CPU, RAM e disco no terminal e continuará atualizando os dados automaticamente.

Para interromper o programa, pressione:

```text
Ctrl + C
```

## 🖥️ Exemplo

```text
╔═════════════════════════════╗
║       Nicolinux-nStats      ║
║     Monitor de Recursos     ║
╚═════════════════════════════╝

Uso da CPU: 12.4%
CPU 0: 2.87 GHz
CPU 1: 2.89 GHz
Núcleos físicos: 1
Núcleos lógicos: 2

Uso de RAM: 55.0%
RAM usada: 4.3 GB
RAM disponível: 3.5 GB

Uso do disco: 33.2%
Espaço usado: 9.9 GB
Espaço livre: 19.8 GB
Espaço total: 31.3 GB
------------------------------
```

> Os valores apresentados acima são apenas um exemplo e variam de acordo com o sistema.

## 📁 Estrutura do projeto

```text
nStats/
├── README.md
├── requirements.txt
└── src/
    └── main.py
```

Desenvolvido por **Nicolinux** 🐧

[GitHub — Nicolinux-dev/nStats](https://github.com/Nicolinux-dev/nStats)