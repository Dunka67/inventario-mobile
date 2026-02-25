Arquitetura e Decisões Técnicas
Este projeto foi construído focando na resolução de problemas reais de usabilidade e na integridade dos dados durante o ciclo de vida da aplicação.

Gerenciamento de Estado (Session State): Utilização nativa do st.session_state para criar uma camada de memória persistente. Isso impede a perda de dados durante os recarregamentos automáticos de tela (reruns) característicos do framework.

Sistema CRUD em Memória: Implementação completa de operações de Criação, Leitura, Atualização (Concatenação de quantidades) e Exclusão de itens, garantindo que o usuário tenha controle total para corrigir erros de digitação antes da exportação final.

Processamento de Strings com Regex: O formatador de texto utiliza Expressões Regulares para varrer as strings de entrada, extrair os valores numéricos isolados e realizar a soma matemática automática do total da categoria no relatório final.

Programação Defensiva: Implementação de flags booleanas de estado para gerenciar janelas de confirmação de exclusão e interceptação de renderização de widgets para limpeza de inputs.

Tecnologias Utilizadas
Python 3.x

Streamlit (Front-end e roteamento de estado)

Regex (Processamento de linguagem natural e extração de dados)

Datetime (Geração de timestamps de auditoria)

Como executar o projeto localmente
Clone o repositório:
git clone https://github.com/Dunka67/inventario-mobile.git

Acesse a pasta do projeto:
cd inventario-mobile

Instale as dependências:
pip install -r requirements.txt

Execute a aplicação indicando o caminho do arquivo principal:
streamlit run src/app.py