# Gerenciador de RH

## Descrição
Este é um sistema de Gerenciamento de Recursos Humanos desenvolvido em Python. O software permite o gerenciamento de funcionários, incluindo a adição, remoção e atualização de dados dos empregados, controle de salários, benefícios, descontos e verificação de conformidade com leis trabalhistas.

---

## Funcionalidades
- Cadastro e remoção de funcionários.
- Atualização de informações dos funcionários.
- Avaliação de desempenho.
- Controle de salário, benefícios e descontos.
- Verificação automática de conformidade com leis trabalhistas.

---

## Estrutura do Código
### Classes Principais
#### `Funcionarios`
Classe base para representar um funcionário. Contém atributos como nome, idade, cargo, salário, status e notas de avaliação. Possui métodos para:
- `Print_Informação_Funcionário_teste`: Exibe as informações do funcionário.
- `Registro_Automatico_Violação_de_Lei_trabalhista`: Verifica se um funcionário está em conformidade com as leis trabalhistas.
- `Sentença_Logica`: Avalia se uma condição lógica definida para um benefício/desconto ou lei é satisfeita.
- `Definir_Termo_Lógico`: Solicita ao usuário a definição de um termo lógico (número ou atributo de funcionário).
- `Definir_Condição_Logica`: Solicita ao usuário a definição de uma condição lógica (>, <, ==, etc.).
- `Registro_Benefício_Desconto_Automatico_teste`: Aplica automaticamente benefícios e descontos aos funcionários.
- `Calcular_Salario_Total`: Calcula o salário total considerando benefícios e descontos.

#### `Gerente`
Herdado de `Funcionarios`, adiciona funcionalidades como:
- `Atualizar_Informações_teste`: Atualiza os dados de um funcionário.
- `Avaliação_funcionário_teste`: Realiza uma avaliação de desempenho do funcionário.
- `Print_Avaliação_funcionário_teste`: Exibe as avaliações do funcionário.
- `Print_Benefício_Desconto_teste`: Exibe informações de um benefício ou desconto.
- `Print_Benefício_Desconto_Funcionários`: Lista os benefícios/descontos aplicados a um funcionário.
- `Registrar_Benefício_Desconto_teste`: Permite registrar manual ou automaticamente benefícios e descontos para um funcionário.
- `Print_Leis_teste`: Exibe as regras trabalhistas cadastradas.
- `Print_Leis_dos_Funcionários`: Lista funcionários que não estão em conformidade com as leis.

#### `Chefe`
Herdado de `Gerente`, inclui:
- `Adicionar_funcionário_teste`: Adiciona um novo funcionário ao sistema.
- `Remover_Funcionário_teste`: Remove um funcionário do sistema.
- `Adicionar_Benefício_Desconto_teste`: Adiciona um novo benefício ou desconto ao sistema.
- `Remover_Benefício_Desconto_teste`: Remove um benefício ou desconto do sistema.
- `Atualizar_Benefício_Deconto_teste`: Atualiza informações de um benefício ou desconto.
- `Adicionar_Lei_teste`: Adiciona uma nova lei trabalhista ao sistema.
- `Remover_Lei_teste`: Remove uma lei trabalhista do sistema.
- `Atualizar_Lei_teste`: Atualiza uma lei trabalhista existente.

#### `Lei`
Define leis trabalhistas com sentenças lógicas para verificar conformidade dos funcionários.

#### `Beneficio_Desconto`
Herdado de `Lei`, representa benefícios e descontos aplicáveis aos funcionários.

---

## Como Usar
1. Execute o script `Gerent_RH_final.py`.
2. Escolha uma opção no menu interativo.
3. Gerencie funcionários, benefícios, descontos e leis conforme necessário.

---

## Dependências
- Python 3.x

---

## Autor
Desenvolvido para gestão eficiente de RH.

