import argparse
from ecommerce_rag.ingestion.pipeline import ingest_file
p=argparse.ArgumentParser(); p.add_argument("paths",nargs="+"); args=p.parse_args()
for path in args.paths: print(path,len(ingest_file(path)))
