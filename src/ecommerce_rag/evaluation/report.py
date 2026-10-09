def markdown_report(metrics:dict)->str:
    rows=["# RAG Evaluation","", "| Metric | Value |","|---|---:|"]
    rows += [f"| {k} | {v} |" for k,v in metrics.items()]
    return "\n".join(rows)+"\n"
