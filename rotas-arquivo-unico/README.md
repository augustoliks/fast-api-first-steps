- Instalação de Dependências
```shell script
virtualenv --python=$(which python3.7) .venv
```

- Execução do Projeto
```shell script
uvicorn main:app --reload
```

---

É possível executar este exemplo, a partir do _shell-script_ `run.sh`

```shell script
chmod +x run.sh
sh run.sh
```