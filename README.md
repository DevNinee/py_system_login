#  Login GUI em Python com Tkinter

Este projeto é uma interface gráfica de login simples, desenvolvida em **Python** utilizando o **Tkinter**. É ideal para fins educacionais e como base para sistemas maiores que exigem autenticação de usuário.

---

##  Demonstração

# screenshots that show the web application running.
1.  Home Screen 
<img width="360" alt="loginpy" src="https://github.com/user-attachments/assets/9887c9ba-19ea-4831-bc1e-648a018a892e"> 

2. Set Name and password,click in Login
<img width="442" alt="Captura de Tela 2024-08-19 às 17 12 30" src="https://github.com/user-attachments/assets/38bc6322-41dd-491e-ada3-7a98d804cf29">

4. Correctly informations 
<img width="343" alt="Captura de Tela 2024-08-19 às 17 13 18" src="https://github.com/user-attachments/assets/53a6f30c-66d8-44b7-ba91-d9f3e8ff0b81">

5. Incorrectly informations
<img width="510" alt="Captura de Tela 2024-08-19 às 17 15 21" src="https://github.com/user-attachments/assets/f56cad00-57b5-48f0-abc3-86cb5b988bb3">
---

##  Funcionalidades

- Interface gráfica simples e responsiva
- Validação de usuário e senha
- Mensagens de sucesso ou erro com `messagebox`
- Simulação de painel após login
- Uso de cores personalizadas e organização por frames

---

## Tecnologias Utilizadas

- **Python 3**
- **Tkinter** (GUI nativa do Python)

---

##  Estrutura do Código

- **Divisão de layout**: interface separada em `frame_up` e `frame_down`
- **Cores personalizadas** para manter consistência visual
- **Função `check_pass()`**:
  - Valida usuários com nome/senha fixos (`admin/admin` ou `Dev/01234567`)
  - Se o login for válido, limpa os frames e chama `new_window()`
- **Função `new_window()`**:
  - Exibe saudação e substitui os widgets da tela de login

---

##  Usuários de Teste

| Nome de Usuário | Senha       |
|-----------------|-------------|
| admin           | admin       |
| Dev             | 01234567    |

---

. Melhorias Sugeridas
Integração com banco de dados (SQLite ou Firebase)

Cadastro de novos usuários

Sistema de recuperação de senha

Responsividade para diferentes resoluções

Licença
Este projeto é livre para fins de aprendizado e desenvolvimento pessoal.

##  Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Salve o código em um arquivo `.py`, por exemplo: `login_gui.py`
3. Execute com:
 ```bash
5. python login_gui.py
 Requisitos
Python 3.x

Tkinter já vem embutido na maioria das distribuições do Python. Caso não esteja disponível, instale com:

sudo apt-get install python3-tk     # Linux (Ubuntu/Debian)







