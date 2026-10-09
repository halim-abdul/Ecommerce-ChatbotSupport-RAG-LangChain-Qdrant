# Architecture

The online path separates intent routing, retrieval and generation. The offline path handles document normalization, chunking, embedding and Qdrant indexing. This separation lets ingestion scale independently from customer traffic.

```mermaid
flowchart LR
A[PDF/Text/Catalog]-->B[Load & Clean]
B-->C[Chunk & Metadata]
C-->D[Embeddings]
D-->E[(Qdrant)]
Q[Customer Question]-->R[Intent Router]
R-->E
E-->G[Grounded Context]
G-->L[LLM]
L-->S[Answer + Sources]
```
