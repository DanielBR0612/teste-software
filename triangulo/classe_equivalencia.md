# Classes de Equivalência — Cálculo de Desconto por Cliente

## Passo 1 

Identificação das variáveis de entrada e das condições que estas devem satisfazer.

| Variáveis de entrada | Condições |
| :--- | :--- |
| Cliente | Pode ser do tipo A, B ou C |
| Qtd | O valor deve estar no intervalo de 1 a 1000 (1 <= Qtd <= 1000) |
| | Valor inteiro |

## Passo 2

Determinando as classes de equivalência. 

| Variáveis de entrada | Condições | Classes válidas | Classes inválidas |
| :--- | :--- | :--- | :--- |
| Cliente | Tipo de Cliente | 1. Cliente == 'A' <br> 2. Cliente == 'B' <br> 3. Cliente == 'C' | 4. Cliente diferente de 'A', 'B' ou 'C' |
| Qtd | 1 <= Qtd <= 1000 | 5. 1 <= Qtd < 10 <br> 6. 10 <= Qtd <= 99 <br> 7. 100 <= Qtd <= 1000 | 8. Qtd < 1 <br> 9. Qtd > 1000 |
| | Valor inteiro | 10. Qtd ∈ Z | 11. Qtd ∉ Z |

## Passo 3 

Especifique os casos de teste:

- Para (1) e (5), (6), (7) - Válidos: Cliente tipo A para cada faixa de quantidade.

    Cliente = 'A'

    Qtd = 5 (desconto = 0%)
    Qtd = 50 (desconto = 5%)
    Qtd = 150 (desconto = 10%)

- Para (2) e (5), (6), (7) - Válidos: Cliente tipo B para cada faixa de quantidade.

    Cliente = 'B'

    Qtd = 5 (desconto = 5%)
    Qtd = 50 (desconto = 15%)
    Qtd = 150 (desconto = 25%)

- Para (3) e (5), (6), (7) - Válidos: Cliente tipo C para cada faixa de quantidade.

    Cliente = 'C'

    Qtd = 5 (desconto = 0%)
    Qtd = 50 (desconto = 20%)
    Qtd = 150 (desconto = 25%)

- Para (4) - Cliente não é A, B ou C.

    Cliente = 'D'
    Qtd = 50

- Para (8) - Quantidade fora do limite inferior.

    Cliente = 'A'
    Qtd = 0

- Para (9) - Quantidade fora do limite superior.

    Cliente = 'B'
    Qtd = 1001

- Para (11) - Quantidade não é inteira.

    Cliente = 'C'
    Qtd = 5.5

---

# Classes de Equivalência — Inclusão de Contato na Agenda

## Passo 1 

Identificação das variáveis de entrada e das condições que estas devem satisfazer.

| Variáveis de entrada | Condições |
| :--- | :--- |
| Nome | Opcionalmente obrigatório (texto) |
| Telefone | Presença obrigatória |
| | Apenas dígitos numéricos |
| | Tamanho deve ter entre 8 e 15 dígitos (8 <= Tam_tel <= 15) |
| | Não pode estar duplicado na agenda |
| Email | Presença obrigatória |
| | Formato exigido: caracteres alfanuméricos contendo `@` e `.` no padrão `*@*.*` |

## Passo 2

Determinando as classes de equivalência. 

| Variáveis de entrada | Condições | Classes válidas | Classes inválidas |
| :--- | :--- | :--- | :--- |
| Telefone | Presença | 1. Telefone preenchido | 2. Telefone vazio ou nulo |
| | Formato | 3. Apenas dígitos (0-9) | 4. Contém letras ou caracteres especiais |
| | Tamanho | 5. 8 <= Tam_tel <= 15 | 6. Tam_tel < 8 <br> 7. Tam_tel > 15 |
| | Unicidade | 8. Número não existe na agenda | 9. Número já existe na agenda |
| Email | Presença / Formato | 10. Formato `*@*.*` alfanumérico | 11. Email vazio ou nulo <br> 12. Sem a parte antes do `@` <br> 13. Sem o `@` <br> 14. Sem a parte após o `@` e antes do `.` <br> 15. Sem o `.` <br> 16. Sem a parte final após o `.` |

## Passo 3 

Especifique os casos de teste:

- Para (1), (3), (5), (8) e (10) - Válidos: Contato com telefone único, apenas numérico, de tamanho adequado e com email válido.

    Nome = 'João Silva'
    Telefone = '11987654321' (11 dígitos, não registrado antes)
    Email = 'joao@email.com'

- Para (2) - Telefone vazio ou nulo.

    Nome = 'Maria Souza'
    Telefone = ''
    Email = 'maria@email.com'

- Para (4) - Telefone com caracteres não numéricos.

    Nome = 'Carlos'
    Telefone = '1198765-ABCD'
    Email = 'carlos@email.com'

- Para (6) - Telefone com menos de 8 dígitos.

    Nome = 'Ana'
    Telefone = '1234567' (7 dígitos)
    Email = 'ana@email.com'

- Para (7) - Telefone com mais de 15 dígitos.

    Nome = 'Pedro'
    Telefone = '1234567890123456' (16 dígitos)
    Email = 'pedro@email.com'

- Para (9) - Telefone já existente na agenda.

    (Assumindo que '11987654321' já está salvo para João Silva)
    Nome = 'Marcos'
    Telefone = '11987654321'
    Email = 'marcos@email.com'

- Para (11) - Email vazio ou nulo.

    Nome = 'Lucas'
    Telefone = '11999999999'
    Email = ''

- Para (13) e (15) - Formato de email inválido (ausência de '@' ou '.').

    Nome = 'Julia'
    Telefone = '11888888888'
    Email = 'julia.email.com' (sem '@')
    
    Nome = 'Julia'
    Telefone = '11888888888'
    Email = 'julia@emailcom' (sem '.')

- Para (12), (14) ou (16) - Formato de email inválido por ausência dos blocos alfanuméricos `*@*.*`.

    Nome = 'Paulo'
    Telefone = '11777777777'
    Email = '@email.com' (sem parte inicial)
    
    Nome = 'Paulo'
    Telefone = '11777777777'
    Email = 'paulo@.com' (sem domínio do meio)
    
    Nome = 'Paulo'
    Telefone = '11777777777'
    Email = 'paulo@email.' (sem a extensão final)