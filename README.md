# Teste_Funcional_Identifer

# Configuração do Ambiente de Teste

Este guia descreve como configurar um ambiente de teste usando `venv`, instalar dependências a partir de um arquivo `requirements.txt` e executar testes usando `pytest`.

## Passo 1: Configurar um Ambiente Virtual (venv)

Primeiro, crie um ambiente virtual para isolar as dependências do projeto. O ambiente virtual permite que você mantenha diferentes projetos com suas próprias dependências sem interferir um no outro.

```bash
# No terminal, navegue até a pasta do seu projeto
cd /caminho/para/seu/projeto
```

# Crie um ambiente virtual chamado "venv" (ou outro nome de sua escolha)
python -m venv venv

# Configuração do Ambiente de Teste

Este guia descreve como configurar um ambiente de teste usando `venv`, instalar dependências a partir de um arquivo `requirements.txt` e executar testes usando `pytest`.

## Passo 2: Ativar o Ambiente Virtual

Agora, ative o ambiente virtual para começar a trabalhar com ele.

```bash
# No Windows:
venv\Scripts\activate
```
```bash
No macOS e Linux:
source venv/bin/activate
```
## Passo 3: Instalar Dependências

Com o ambiente virtual ativado, você pode instalar as dependências a partir de um arquivo requirements.txt. Certifique-se de que o arquivo requirements.txt esteja localizado no diretório do seu projeto.

```bash
pip install -r requirements.txt
```
Isso instalará todas as dependências listadas no arquivo requirements.txt.


## Passo 4: Executar Testes com pytest

Agora que você tem todas as dependências instaladas, você pode executar os testes do seu projeto usando pytest.

```bash
pytest
```
O pytest irá procurar por arquivos de teste no diretório do seu projeto e executá-los. Certifique-se de que seus arquivos de teste tenham nomes que correspondam ao padrão de nomenclatura do pytest, como test_*.py. para o projeto: test_identifier.py

<br>
projeto/ <br>
├── venv/ <br>
├── test/<br>
│      ├──  identifier/<br>
│      │     ├── __init__<br>
│      │     ├── fake.py<br>
│      │     ├── identifier.py<br>
│      │     └── run.py<br>
|      └── __init__<br>
├── src/<br>
│      ├── __init__<br>
│      ├── test_identifer<br>
│      └── test_identifer2<br>
├── identifier.py <br>
├── requirements.txt <br>
└── test_identifier.py <br>
<br>

Após a execução dos testes, você verá os resultados no terminal.

## Desativar o Ambiente Virtual

Quando você terminar de trabalhar no projeto, você pode desativar o ambiente virtual.

```bash
deactivate
```
