# Análise do valor limite 

# Triangulo
---
## Fronteiras 

| Condição | Limite inválido | Limite válido |
|----------|------------------------|------------------------|
| Lado positivo | 0 (a+b ≤ c quando a=0) | 1 (mínimo positivo) |
| Regra de existência (a+b vs c) | a+b = c (≤, inválido) | a+b = c+1 (>, válido) |

## Casos de teste

**Variando o valor de a:**

| a  | b | c | Saída esperada | Fronteira |
|----|---|---|--------------------|-----------|
| 0  | 8 | 8 | Não é um triângulo válido   | a=0: a+b=8 ≤ c=8 |
| 1  | 8 | 8 | Isósceles          | a=1 |
| 15 | 8 | 8 | Isósceles          | a = b+c−1 |
| 16 | 8 | 8 | Não é um triângulo válido   | a = b+c |

**Variando o valor de b:** 

| a | b  | c | Saída Esperada | Fronteira |
|---|----|---|--------------------|-----------|
| 8 | 0  | 8 | Não é um triângulo válido   | b=0 |
| 8 | 1  | 8 | Isósceles          | b=1 |
| 8 | 15 | 8 | Isósceles          | b = a+c−1 |
| 8 | 16 | 8 | Não é um triângulo válido   | b = a+c |

**Variando o valor de c:**

| a | b | c  | Saída esperada | Fronteira |
|---|---|----|--------------------|-----------|
| 8 | 8 | 0  | Não é um triângulo válido   | c=0 |
| 8 | 8 | 1  | Isósceles          | c=1 |
| 8 | 8 | 15 | Isósceles          | c = a+b−1 |
| 8 | 8 | 16 | Não é triângulo    | c = a+b (no limite, inválido) |

## Análise do valor limite — Desconto por Dependente

A análise do valor limite testa os valores exatamente nos limites de cada condição (fronteiras), além de valores imediatamente abaixo e acima desses limites.

### Fronteiras

| Condição | Limite inválido (fora) | Limite válido (dentro) |
|----------|------------------------|------------------------|
| Limite inferior da idade [0..24] | -1 (idade negativa) | 0 (mínimo, 15%) |
| Transição para faixa de 12% | 12 (pertence aos 15%) | 13 (mínimo, 12%) |
| Transição para faixa de 5% | 18 (pertence aos 12%) | 19 (mínimo, 5%) |
| Transição para faixa de 3% | 21 (pertence aos 5%) | 22 (mínimo, 3%) |
| Limite superior da idade [0..24] | 25 (acima, fora do limite) | 24 (máximo, 3%) |

### Casos de teste

**Variando a idade do dependente:**

| Idade | Resultado Esperado | Fronteira |
|-------|--------------------|-----------|
| -1    | Inválido           | idade = -1 (mínimo inválido) |
| 0     | 15%                | idade = 0 (mínimo válido) |
| 12    | 15%                | idade = 12 (último valor válido - 15%) |
| 13    | 12%                | idade = 13 (mínimo válido - 12%) |
| 18    | 12%                | idade = 18 (último valor válido - 12%) |
| 19    | 5%                 | idade = 19 (mínimo válido - 5%) |
| 21    | 5%                 | idade = 21 (último valor válido - 5%) |
| 22    | 3%                 | idade = 22 (mínimo válido - 3%) |
| 24    | 3%                 | idade = 24 (último valor válido) |
| 25    | Inválido           | idade = 25 (no limite, inválido) |

