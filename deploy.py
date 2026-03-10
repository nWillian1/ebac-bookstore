import os
import requests
from git import Repo

def run_deploy():
    username = os.getenv('PA_USERNAME')
    token = os.getenv('PA_TOKEN')
    
    if not username or not token:
        print("Erro: PA_USERNAME ou PA_TOKEN não encontrados no ambiente.")
        return

    try:
        repo = Repo(os.getcwd())
        origin = repo.remotes.origin
        origin.pull()
        print("Git Pull realizado com sucesso no servidor!")

        url = f'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{username}.pythonanywhere.com/reload/'
        
        response = requests.post(
            url,
            headers={'Authorization': f'Token {token}'}
        )

        if response.status_code == 200:
            print("Site recarregado com sucesso no PythonAnywhere!")
        else:
            print(f"Falha ao recarregar o site: {response.status_code}")
            print(response.content)

    except Exception as e:
        print(f"Ocorreu um erro durante o deploy: {e}")

if __name__ == "__main__":
    run_deploy()