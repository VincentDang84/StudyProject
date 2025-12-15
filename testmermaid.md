flowchart LR
    classDef bigFont font-size:30px,font-weight:bold;
  
    %% ======================
    %% Data Collection Module
    %% ======================
    subgraph DC[ ]
        direction TB
        DCH[Data Collection]==>DC1[Secondary Data_Industry Report Data]
        DCH[Data Collection]==>DC2[Mixed Data_Competitor Benchmarking]
        DCH[Data Collection]==>DC3[Primary Data_Questionnaire Survey]
    end

    %% ======================
    %% Research & Analysis Module
    %% ======================
    subgraph A0[ ]
        direction LR

        A[Data Analysis]

        A ==> B[Market Analysis PESTLE]
        B ==> B1[Market Size & Growth]
        B ==> B2[Customer Trends & Behaviours]

        A ==> C[Competitor Analysis]
        C ==> C1[Direct Competitors]
        C ==> C2[Indirect Competitors]
        C ==> C3[Level of Service Integration]

        A ==> D[Customer Analysis]
        D ==> D1[Segmentation]
        D ==> D2[Customer Personas]
        D ==> D3[Needs, Pains & Expectations]
        D ==> D4[Purchasing Decision Making Factors Analysis]
    end

    %% ======================
    %% Data feeds into Analysis
    %% ======================
    DC1 ==> A0
    DC2 ==> A0
    DC3 ==> A0

    %% ======================
    %% Strategic Synthesis Layer
    %% ======================
    S[SWOT Strategic Analysis]

    B1 ==> S
    B2 ==> S
    C1 ==> S
    C2 ==> S
    C3 ==> S
    D1 ==> S
    D2 ==> S
    D3 ==> S
    D4 ==> S
    %% ======================
    %% Lean BMC Module
    %% ======================
    S ==> E0

    subgraph E0[ ]
        direction LR
        EH[Lean Business Model Canvas]
        E1[Problem]
        E2[Customer Segments]
        E3[Value Proposition]
        E4[Solution]
        E5[Channels]
        E6[Revenue Streams]
        E7[Cost Structure]
        E8[Key Metrics]
        E9[Unfair Advantage]
    end

    %% ======================
    %% Styling
    %% ======================
    class DCH,EH bigFont
    class D4,DC1,DC2,DC3,A,B,B1,B2,C,C1,C2,C3,D,D1,D2,D3,S,E1,E2,E3,E4,E5,E6,E7,E8,E9 bigFont

    style DC fill:#FFFDE7,stroke:#F9A825,stroke-width:2px
    style A0 fill:#F1F8E9,stroke:#558B2F,stroke-width:2px
    style S fill:#FFF3E0,stroke:#EF6C00,stroke-width:2px,font-weight:bold
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
    style A fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E1 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E2 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E3 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E4 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E5 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E6 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E7 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E8 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style E9 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style EH fill:#ADD8E6,stroke:#1565C0,stroke-width:2px
    style DCH fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style DC1 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style DC2 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style DC3 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
    style D4 fill:#FFFFFF,stroke:#1565C0,stroke-width:2px
Beta
0 / 0
used queries
1
