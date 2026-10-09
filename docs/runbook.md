# Operations runbook

1. Check `/health` and Qdrant reachability.
2. Inspect retrieval empty-rate and model errors.
3. Roll back policy/index changes if grounding regresses.
4. Rebuild the affected collection from source documents when metadata is inconsistent.
