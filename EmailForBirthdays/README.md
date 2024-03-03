# Gerando Aniversariantes e Enviando Mensagens de Aniversário por Email

Este é um pequeno script Python que gera dados aleatórios de aniversariantes e os escreve em um arquivo CSV chamado `aniversariantes.csv`. Ele utiliza a biblioteca `Faker` para criar nomes, endereços de e-mail, datas de nascimento e idades fictícias.

Após concluida a primeira parte iniciamos lendo o arquivo CSV gerado anteriormente contendo informações sobre aniversariantes e envia mensagens de aniversário por email usando o servidor SMTP (MailHog).


## Como funciona

1. O script cria um arquivo CSV chamado `aniversariantes.csv`.
2. Ele escreve uma linha de cabeçalho com os campos: `nome`, `email`, `idade` e `data_de_nascimento`.
3. Em seguida, gera dados aleatórios para o número especificado de registros (no exemplo, 10 registros).
4. Para cada registro:
   - Gera um nome aleatório.
   - Gera um endereço de e-mail aleatório.
   - Calcula a idade com base na data de nascimento gerada aleatoriamente.
   - Escreve esses dados no arquivo CSV.
5. Por fim, adiciona um registro adicional para o aniversário de hoje, com objetivo de utilizar futuramente em `send_birthday_emails`:
   - Gera um nome, um e-mail aleatórios e coloca a data de hoje .
   - Calcula a idade com base na data de nascimento gerada aleatoriamente, garantindo que seja um aniversário válido.
   - Escreve esses dados no arquivo CSV.
6. O script lê o arquivo CSV e verifica se a data de nascimento coincide com a data atual.
7. Se houver aniversariantes no dia, ele envia uma mensagem de aniversário para cada um deles.