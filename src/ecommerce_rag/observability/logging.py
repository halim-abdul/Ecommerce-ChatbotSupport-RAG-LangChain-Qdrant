import json,logging

def log_event(logger:logging.Logger,event:str,**fields):
    logger.info(json.dumps({"event":event,**fields},default=str))
