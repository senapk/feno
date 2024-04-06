# Básico

Crie um arquivo `Readme.md` com o seguinte formato:

    # Título da atividade

    A descrição que você quiser

    ```txt
    >>>>>>>> teste 1
    entrada
    entrada
    ========
    saida
    saida
    <<<<<<<<
    
    >>>>>>>> teste 2
    entrada
    entrada
    ========
    saida
    saida
    <<<<<<<<

    ```

- A primeira linha é o título da atividade.
- Você pode inserir quantos testes quiser.
- Execute o `feno` na pasta local com:

```bash
feno .
```

Ele vai criar uma pasta `.cache` com:

- `q.html` - Um arquivo html com a descrição do problema.
- `q.tio` - Um arquivo com as questões no formato tio.
- `mapi.json` - Um arquivo com os testes formatado para o moodle, que pode ser utilizado pelo projeto [mula](https://github.com/senapk/mula).
