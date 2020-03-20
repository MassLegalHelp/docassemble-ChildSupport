from docassemble.base.functions import defined

def question_id(message):
  if defined("debug_enabled") and debug_enabled:
    return "[" + message + "] "
  else:
    return ""