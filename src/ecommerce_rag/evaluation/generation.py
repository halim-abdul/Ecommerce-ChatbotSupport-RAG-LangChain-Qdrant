def citation_coverage(answer:str,source_labels:list[str])->float:
    if not source_labels: return 1.0
    used=sum(1 for s in source_labels if s in answer)
    return used/len(source_labels)

def refusal_expected(has_evidence:bool)->bool: return not has_evidence
