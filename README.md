# Teste_Funcional_Identifer

# Configuração do Ambiente de Teste

Este guia descreve como configurar um ambiente de teste usando `venv`, instalar dependências a partir de um arquivo `requirements.txt` e executar testes usando `pytest`.

## Passo 1: Configurar um Ambiente Virtual (venv)

Primeiro, crie um ambiente virtual para isolar as dependências do projeto. O ambiente virtual permite que você mantenha diferentes projetos com suas próprias dependências sem interferir um no outro.

```bash
# No terminal, navegue até a pasta do seu projeto
cd /caminho/para/seu/projeto

# Crie um ambiente virtual chamado "venv" (ou outro nome de sua escolha)
python -m venv venv
