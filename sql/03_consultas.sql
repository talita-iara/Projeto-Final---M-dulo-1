SELECT
   id_venda,
  valor_total,
    preco_unitario * quantidade + Imposto AS valor_calculado
FROM tratada_vendas;

SELECT COUNT(*) AS divergencias
FROM tratada_vendas
WHERE valor_total <> (
    preco_unitario * quantidade + Imposto
);

-- 1. filial com maior faturamento
SELECT
    filial,
    SUM(valor_total) AS faturamento
FROM tratada_vendas
GROUP BY filial
ORDER BY faturamento DESC;


-- 2. filial com maior quantidade de vendas
SELECT
    filial,
    COUNT(*) AS quantidade_vendas
FROM tratada_vendas
GROUP BY filial
ORDER BY quantidade_vendas DESC;


-- 3. linha de produto com maior faturamento
SELECT
    linha_produto,
    SUM(valor_total) AS faturamento
FROM tratada_vendas
GROUP BY linha_produto
ORDER BY faturamento DESC;


-- 4. linha de produto com melhor avaliacao media
SELECT
    linha_produto,
    AVG(avaliacao) AS avaliacao_media
FROM tratada_vendas
GROUP BY linha_produto
ORDER BY avaliacao_media DESC;


-- 5. forma de pagamento mais utilizada
SELECT
    forma_pagamento,
    COUNT(*) AS quantidade_vendas
FROM tratada_vendas
GROUP BY forma_pagamento
ORDER BY quantidade_vendas DESC;


-- 6. valor medio das vendas
SELECT
    AVG(valor_total) AS valor_medio_vendas
FROM tratada_vendas;


-- 7. maior venda
SELECT
    id_venda,
    valor_total
FROM tratada_vendas
ORDER BY valor_total DESC
LIMIT 1;


-- 8. dia da semana com maior quantidade de vendas
SELECT
    TRIM(TO_CHAR(data_venda, 'Day')) AS dia_semana,
    COUNT(*) AS quantidade_vendas
FROM tratada_vendas
GROUP BY TRIM(TO_CHAR(data_venda, 'Day'))
ORDER BY quantidade_vendas DESC;

-- 9. Valor medio das vendas por filial

SELECT
    filial,
    ROUND(AVG(valor_total), 2) AS valor_medio_venda
FROM tratada_vendas
GROUP BY filial
ORDER BY valor_medio_venda DESC;

-- 10. Faturamento das categorias por filial
SELECT
    filial,
    linha_produto,
    SUM(quantidade) AS unidades_vendidas,
    ROUND(SUM(valor_total), 2) AS faturamento
FROM tratada_vendas
GROUP BY filial, linha_produto
ORDER BY filial, faturamento DESC;