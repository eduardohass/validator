import logging as log
from validator.ext.db import bancodados

class Rule:
    def __init__(self, name, category, status, type):
        self.name = name                # nome da regra
        self.category = category        # categoria (cabeçalho, código, etc)
        self.status = eval(status)      # ativo ou inativo
        self.type = type                # wildcard, orderby etc.


    def get_rules(query):
        log.info('[get_rules]')
        try:
            return bancodados.find(bancodados, "rules", query)
        except Exception as e:
            log.exception('[get_rules][error] - erro ao selecionar regras')
            log.exception("Error type: {0}".format(type(e)))
            log.exception("Error type: {0}".format(e))
            return None
          

    def set_rule(rule):
        log.info('[set_rule]')
        try:
            bancodados.insert(bancodados, "rules", rule.__dict__)
            log.info('[set_rule] - regra cadastrada com sucesso')
            return(200)
        except Exception as e:
            log.exception('[set_rule][error] - erro ao inserir nova regra')
            log.exception("Error type: {0}".format(type(e)))
            log.exception("Error type: {0}".format(e))
            return 500


    def rule_exists(rule):
        log.info('[rule_exists]')
        try:
            obj = Database.find_one("rules", {'name': rule.name})
            if obj is not None:
                log.info('[rule_exists] - Regra ja existente')
                return True
            else:
                log.info('[rule_exists] - Regra não existe')
            
            return False
        except Exception as e:
            log.exception('[rule_exists][error] - erro ao validar se a regra existe')
            log.exception("Error type: {0}".format(type(e)))
            log.exception("Error type: {0}".format(e))
            return False
