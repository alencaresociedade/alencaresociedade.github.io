from pathlib import Path

RAIZ = Path(__file__).parent
CONTEUDO = RAIZ / "content"
TEMPLATES = RAIZ / "templates"
STATIC = RAIZ / "static"
SAIDA = RAIZ / "docs"
DADOS = RAIZ / "data"

SITE_URL = "https://alencaresociedade.github.io"
NOME_SITE = "Alencar e Sociedade"
AUTOR_PADRAO = "Adryan de Alencar"

# Seções do site, na ordem em que aparecem no header e no menu lateral.
# O slug vira parte do endereço: <slug>/<categoria>/<idioma>/<matéria>.html
# A primeira é a padrão: matéria sem "secao" no frontmatter cai nela
# (e continua em noticias/..., então nenhum link antigo muda).
SECOES = [
       {"slug": "ensaios", "nome": "Ensaios"},
       {"slug": "arte-e-cultura", "nome": "Arte e Cultura"},
]

FONTE_BOLD = STATIC / "fonts/ZTNature-Black.ttf"
FONTE_REG = STATIC / "fonts/ZTNature-Medium.ttf"

LINKS = [
    {"titulo": "Últimas matérias", "url": "index.html", "desc": NOME_SITE},
    {"titulo": "LinkedIn", "url": "https://www.linkedin.com/in/adryan-de-alencar-61b386309", "desc": "Perfil profissional"},
    {"titulo": "Lattes", "url": "http://lattes.cnpq.br/3380250362638685", "desc": "Currículo Lattes"},
]

# Build de página-ponte só para links trocados.
REDIRECIONAR_ANTIGOS = []
