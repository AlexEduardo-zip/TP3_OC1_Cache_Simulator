**Relatório - Simulador de Memória Cache**

**Objetivo:**

Desenvolver um simulador de memórias cache de um nível, explorando conceitos como associatividade completa, associatividade por conjunto e mapeamento direto.

**Implementação:**

O simulador foi implementado em C++, seguindo as especificações fornecidas. Utilizamos a biblioteca `<iostream>` para a entrada/saída de dados.

**Estratégia:**

Optamos por uma abordagem orientada a objetos, representando a cache como um vetor de linhas. A simulação considera o tamanho total da cache, o tamanho de cada linha e o tamanho de cada grupo.

**Funcionalidades Principais:**

1. `parseArguments`: Função para processar os argumentos da linha de comando.
2. `readMemoryAccesses`: Função para ler os acessos à memória do arquivo fornecido.
3. `simulateCache`: Simulação da memória cache, considerando políticas de mapeamento e substituição.

**Política Adotada:**

A política de substituição de páginas é FIFO (First In First Out), onde a primeira linha a entrar é a primeira a sair em caso de substituição. As linhas de um conjunto são armazenadas de forma consecutiva na cache.

**Saída Formatada:**

A saída segue as especificações, exibindo índice da linha, bit de validade e identificador do bloco. O identificador do bloco é obtido ignorando bits menos significativos e bits de identificação de bloco. A saída inclui a contagem de hits e misses.

**Testes Realizados:**

O programa foi testado com diversos casos, variando o tamanho da cache, tamanho das linhas e associatividade. Os resultados foram comparados com expectativas teóricas.

**Conclusão:**

O projeto proporcionou uma compreensão prática dos conceitos de memória cache, associatividade e políticas de substituição. A implementação bem-sucedida do simulador reflete a aplicação efetiva dos conhecimentos adquiridos na disciplina, consolidando a compreensão dos conceitos abordados.
