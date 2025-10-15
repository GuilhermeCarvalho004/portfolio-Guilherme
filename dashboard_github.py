import streamlit as st
import requests
import pandas as pd

st.title("Dashboard de Ações do GitHub")

repo = st.text_input("Digite o repositório (formato: owner/repo)", "GuilhermeCarvalho004/portfolio-Guilherme")

def get_issues(repo):
    url = f"https://api.github.com/repos/{repo}/issues"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return pd.DataFrame()

def get_pulls(repo):
    url = f"https://api.github.com/repos/{repo}/pulls"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return pd.DataFrame()

def get_commits(repo):
    url = f"https://api.github.com/repos/{repo}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return pd.DataFrame()

if repo:
    st.header("Issues abertas")
    issues = get_issues(repo)
    if not issues.empty:
        st.write(issues[["number", "title", "state", "created_at"]])
    else:
        st.write("Nenhuma issue encontrada ou o repositório não existe.")

    st.header("Pull Requests abertas")
    prs = get_pulls(repo)
    if not prs.empty:
        st.write(prs[["number", "title", "state", "created_at"]])
    else:
        st.write("Nenhum PR encontrado ou o repositório não existe.")

    st.header("Commits recentes")
    commits = get_commits(repo)
    if not commits.empty:
        st.write(commits[["sha", "commit"]].head(10))
    else:
        st.write("Nenhum commit encontrado ou o repositório não existe.")