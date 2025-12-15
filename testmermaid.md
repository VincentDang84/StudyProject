flowchart LR
   
    %% ======================
    %% Data Collection Module
    %% ======================
    subgraph DC["Data Collection Module"]
        direction TB
        DCH["Data Collection"]
        DC1["Secondary Data<br/>Industry Report Data"]
        DC2["Mixed Data<br/>Competitor Benchmarking"]
        DC3["Primary Data<br/>Questionnaire Survey"]

        DCH --> DC1
        DCH --> DC2
        DCH --> DC3
    end

    %% ======================
    %% Research & Analysis Module
    %% ======================
    subgraph A0["Research & Analysis Module"]
        direction LR

        A["Data Analysis"]

        B["Market Analysis (PESTLE)"]
        B1["Market Size & Growth"]
        B2["Customer Trends & Behaviours"]

        C["Competitor Analysis"]
        C1["Direct Competitors"]
        C2["Indirect Competitors"]
        C3["Level of Service Integration"]

        D["Customer Analysis"]
        D1["Segmentation"]
        D2["Customer Personas"]
        D3["Needs, Pains & Expectations"]
        D4["Purchasing Decision Making Factors Analysis"]

        A --> B
        B --> B1
        B --> B2

        A --> C
        C --> C1
        C --> C2
        C --> C3

        A --> D
        D --> D1
        D --> D2
        D --> D3
        D --> D4
    end

    %% ======================
    %% Data feeds into Analysis
    %% ======================
    DC1 --> A
    DC2 --> A
    DC3 --> A

    %% ======================
    %% Strategic Synthesis Layer
    %% ======================
    S["SWOT Strategic Analysis"]

    B1 --> S
    B2 --> S
    C1 --> S
    C2 --> S
    C3 --> S
    D1 --> S
    D2 --> S
    D3 --> S
    D4 --> S

    %% ======================
    %% Lean BMC Module
    %% ======================
    subgraph E0["Lean BMC Module"]
        direction LR
        EH["Lean Business Model Canvas"]
        E1["Problem"]
        E2["Customer Segments"]
        E3["Value Proposition"]
        E4["Solution"]
        E5["Channels"]
        E6["Revenue Streams"]
        E7["Cost Structure"]
        E8["Key Metrics"]
        E9["Unfair Advantage"]

        EH --> E1 --> E2 --> E3 --> E4 --> E5 --> E6 --> E7 --> E8 --> E9
    end

    S --> EH

    %% ======================
    %% Styling
    %% ======================
    classDef bigFont font-size:30px,font-weight:bold;

    class DCH,EH bigFont
    class D4,DC1,DC2,DC3,A,B,B1,B2,C,C1,C2,C3,D,D1,D2,D3,S,E1,E2,E3,E4,E5,E6,E7,E8,E9 bigFont

    style DC fill:#FFFDE7,stroke:#F9A825,stroke-width:2px
    style A0 fill:#F1F8E9,stroke:#558B2F,stroke-width:2px
    style S fill:#FFF3E0,stroke:#EF6C00,stroke-width:2px
    style E0 fill:#E3F2FD,stroke:#1565C0,stroke-width:2px

    style B fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style B1 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style B2 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style C fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style C1 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style C2 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style C3 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style D fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style D1 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style D2 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style D3 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style D4 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style A fill:#FFFFFF,stroke:#1565C0,stroke-width:2px

    style EH fill:#ADD8E6,stroke:#1565C0,stroke-width:2px
    style DCH fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style DC1 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style DC2 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style DC3 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px

    style E1 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E2 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E3 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E4 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E5 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E6 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E7 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E8 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E9 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
