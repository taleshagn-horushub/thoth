# Exemplos de Diagramas de Arquitetura em Mermaid

## Arquitetura Web em Três Camadas

Este exemplo demonstra uma arquitetura web clássica com frontend, backend e banco de dados.

```mermaid
flowchart TD
    %% Definição de Classes para Estilização
    classDef client fill:#f9f,stroke:#333,stroke-width:2px;
    classDef server fill:#bbf,stroke:#333,stroke-width:2px;
    classDef db fill:#bfb,stroke:#333,stroke-width:2px;

    %% Nós
    user((Usuário)):::client
    
    subgraph Frontend [Camada de Apresentação]
        ui[Interface Web]:::client
    end
    
    subgraph Backend [Camada de Lógica de Negócios]
        api[API REST]:::server
        auth[Serviço de Autenticação]:::server
    end
    
    subgraph Database [Camada de Dados]
        db[(Banco de Dados Relacional)]:::db
        cache[(Cache Redis)]:::db
    end

    %% Relações
    user -->|Acessa| ui
    ui -->|Requisições HTTP| api
    api -->|Valida Token| auth
    api -->|Lê/Escreve Dados| db
    api -->|Busca Dados em Cache| cache
```

## Arquitetura de Microsserviços

Este exemplo mostra uma arquitetura baseada em microsserviços com um API Gateway.

```mermaid
flowchart LR
    %% Definição de Classes
    classDef external fill:#f96,stroke:#333,stroke-width:2px;
    classDef gateway fill:#ff9,stroke:#333,stroke-width:2px;
    classDef service fill:#bbf,stroke:#333,stroke-width:2px;
    classDef db fill:#bfb,stroke:#333,stroke-width:2px;

    %% Nós
    client[Cliente Mobile/Web]:::external
    gateway[API Gateway]:::gateway
    
    subgraph Microsserviços
        user_svc[Serviço de Usuários]:::service
        order_svc[Serviço de Pedidos]:::service
        inventory_svc[Serviço de Inventário]:::service
    end
    
    subgraph Bancos de Dados
        user_db[(DB Usuários)]:::db
        order_db[(DB Pedidos)]:::db
        inventory_db[(DB Inventário)]:::db
    end

    %% Relações
    client -->|Requisições| gateway
    gateway -->|Roteamento| user_svc
    gateway -->|Roteamento| order_svc
    gateway -->|Roteamento| inventory_svc
    
    user_svc -->|Lê/Escreve| user_db
    order_svc -->|Lê/Escreve| order_db
    inventory_svc -->|Lê/Escreve| inventory_db
    
    order_svc -.->|Verifica Estoque| inventory_svc
```

## Pipeline de Dados

Este exemplo ilustra um fluxo de processamento de dados.

```mermaid
flowchart LR
    %% Definição de Classes
    classDef source fill:#f96,stroke:#333,stroke-width:2px;
    classDef process fill:#bbf,stroke:#333,stroke-width:2px;
    classDef storage fill:#bfb,stroke:#333,stroke-width:2px;
    classDef bi fill:#f9f,stroke:#333,stroke-width:2px;

    %% Nós
    app_logs[Logs da Aplicação]:::source
    db_events[Eventos do Banco]:::source
    
    subgraph Ingestão e Processamento
        kafka[Apache Kafka]:::process
        spark[Apache Spark]:::process
    end
    
    subgraph Armazenamento
        data_lake[(Data Lake)]:::storage
        data_warehouse[(Data Warehouse)]:::storage
    end
    
    dashboard[Dashboard BI]:::bi

    %% Relações
    app_logs -->|Envia Eventos| kafka
    db_events -->|CDC| kafka
    
    kafka -->|Consome Tópicos| spark
    
    spark -->|Salva Dados Brutos| data_lake
    spark -->|Transforma e Agrega| data_warehouse
    
    data_warehouse -->|Consulta Dados| dashboard
```
