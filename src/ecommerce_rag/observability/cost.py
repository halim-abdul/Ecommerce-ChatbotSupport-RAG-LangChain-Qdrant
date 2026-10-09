def estimate_cost(prompt_tokens:int,completion_tokens:int,prompt_per_million:float,completion_per_million:float)->float:
    return prompt_tokens/1_000_000*prompt_per_million + completion_tokens/1_000_000*completion_per_million
