import streamlit as st
from dados.catalago import CATALOGO_PRODUTOS
from dados.utils.formatador import gerar_texto_whatsapp



st.set_page_config(page_title="Inventário Mobile", page_icon="📱")

if 'Deletar_Lancamento' not in st.session_state:
    st.session_state['Deletar_Lancamento'] = False

if 'reset_total' not in st.session_state:
    st.session_state['reset_total'] = False

if 'confirmar_limpeza' not in st.session_state:
    st.session_state['confirmar_limpeza'] = False

if 'inventario' not in st.session_state:
    st.session_state['inventario'] = {}

if 'conferente' not in st.session_state:
    st.session_state['conferente'] = ""

if 'turno' not in st.session_state:
    st.session_state['turno'] = "" 

if 'limpar_campo' not in st.session_state:
    st.session_state['limpar_campo'] = False

if 'mensagem_sucesso' in st.session_state:
    st.success(st.session_state['mensagem_sucesso'])
    del st.session_state['mensagem_sucesso']

if st.session_state['reset_total']:
    st.session_state['conferente'] = ""
    st.session_state['reset_total'] = False

st.title('Inventário Rápido')



st.selectbox('Turno', options=['Noite', 'Tarde', 'Manhã'], key='turno')
st.text_input('Nome Conferente', key='conferente')

st.divider()

categoria_escolhida = st.selectbox('Selecione a categria:', options=list(CATALOGO_PRODUTOS.keys()))
produto_escolhido = st.selectbox('Selecione o Porduto:', options=CATALOGO_PRODUTOS[categoria_escolhida],key='produto_key')

if produto_escolhido == "Outro (Digitar Manualmente)":
    produto_manual = st.text_input('Digite o nome do produto:', key='produto_manual')
    if produto_manual:
        produto_escolhido = produto_manual


if st.session_state['limpar_campo']:
    st.session_state['quantidade_input'] = ""
    st.session_state['limpar_campo'] = False


quantidade = st.text_input('Quantidade (Ex: 10 un / 2 fardos)', key='quantidade_input')


    
if st.button('Adicionar á lista'):  
    if quantidade == "":
        st.error("Por favor, insira uma quantidade válida.")
        st.stop()

    if produto_escolhido == 'Outro (Digitar Manualmente)':
        st.error('Por favor digite o nome do produto.')
        st.stop()

    if 'conferente' not in st.session_state or not st.session_state['conferente']:
        st.error("Por favor insira o nome do conferente.")
        st.stop()

    if categoria_escolhida not in st.session_state['inventario']:
        st.session_state['inventario'][categoria_escolhida] = {}
    
    if produto_escolhido in st.session_state['inventario'][categoria_escolhida]:
        valor_antigo = st.session_state['inventario'] [categoria_escolhida][produto_escolhido]
        st.session_state['inventario'][categoria_escolhida][produto_escolhido] = f'{valor_antigo}+ {quantidade}'
    else:
        st.session_state['inventario'][categoria_escolhida][produto_escolhido]= quantidade
    
    st.session_state['mensagem_sucesso'] = f'{produto_escolhido} adicionado com sucesso!'
    st.session_state['limpar_campo'] = True
    st.rerun()

    st.success(f"{produto_escolhido} adicionado com sucesso!")

st.divider()

st.subheader("Espelho Inventário")

texto_relatorio = gerar_texto_whatsapp(st.session_state['turno'], st.session_state['conferente'], st.session_state['inventario'])
st.code(texto_relatorio, language='markdown')

# 1. Crie a função que zera as variáveis na memória
def limpar_tudo():
    st.session_state['inventario'] = {}
    st.session_state['limpar_campo'] = False
    st.session_state['Deletar_Lancamento'] = False
    st.session_state['mensagem_sucesso'] = "Inventário limpo com sucesso!"
    st.session_state['reset_total'] = True


def deletar_lancamento(categoria, produto):
    if categoria in st.session_state['inventario'] and produto in st.session_state['inventario'][categoria]:
        del st.session_state['inventario'][categoria][produto]
        if not st.session_state['inventario'][categoria]:
            del st.session_state['inventario'][categoria]

        st.session_state['mensagem_sucesso'] = f'Lançamento de {produto} deletado com sucesso!'
    else:
        st.error('Lançamento não encontrado.')

if st.session_state['inventario']:
    st.subheader('Limpar algum lançamento')
    categoria_deletar = st.selectbox('Selecione a categria:', options=list(st.session_state['inventario'].keys()))
    produto_deletar = st.selectbox('Selecione o Porduto:', options=st.session_state['inventario'][categoria_deletar],key='produto_deletar_key')

    if st. button('Deletar Lançamento'):
        st.session_state['Deletar_Lancamento'] = True
        st.session_state['confirmar_limpeza'] = False
        st.rerun()
    if st.session_state['Deletar_Lancamento']:
        st.warning('Tem certeza que deseja deletar este lançamento? Esta ação não pode ser desfeita.')
        col_1, col_2 = st.columns(2)
        with col_1:  
            if st.button('Sim, Deletar Lançamento'):
                deletar_lancamento(categoria_deletar, produto_deletar)

                st.session_state['Deletar_Lancamento'] = False
                st.rerun()
            with col_2:
                if st.button('Cancelar'):
                    st.session_state['Deletar_Lancamento'] = False
                    st.rerun()

        # st.rerun()

    if st.button('Limpar Inventário'):
        st.session_state['confirmar_limpeza'] = True
        st.session_state['Deletar_Lancamento'] = False
        st.rerun()

    if st.session_state['confirmar_limpeza']:
        st.warning('Tem certeza que deseja apagar todo o inventário? Esta ação não pode ser desfeita.')
        col_sim, col_nao = st.columns(2)
        with col_sim:
            if st.button('Sim, limpar o inventário'):
                limpar_tudo()
                st.session_state['confirmar_limpeza'] = False
                st.rerun()
        with col_nao:
            if st.button('Cancelar Limpeza'):
                st.session_state['confirmar_limpeza'] = False
                st.rerun()