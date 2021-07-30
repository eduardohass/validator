import logging as log
from flask import request, render_template, redirect, url_for
from flask import Blueprint
from validator.ext.db.rule import Rule

bp = Blueprint('site',__name__)

@bp.route("/")
def index():
    return render_template('index.html', site_title='Página inicial', site_subtitle="Bem vindo")

# @bp.route("/rule")
# def get_rule():
#     return render_template('lista.html')

@bp.route('/rule', methods=['GET', ])
def get_rule():
    log.info('route - /rule [GET]')
    rules = Rule.get_rules({"status": bool('true')})
    if rules is not None:
        return render_template('lista.html', title='Regras', rules=rules)
    else:
        return 'Erro ao recuperar a regra', 500




@bp.route('/rule', methods=['POST', ])
def set_rule():
    log.info('route - /rule [POST]')

    new_rule = Rule(request.form['name'].strip().lower(), # esse replace de aspas é para funcionar a busca find_one() dict
                    request.form['category'].strip().lower(),
                    request.form['status'].strip(), 
                    request.form['type'].strip().lower())

    # TODO = Tem um problema que é na validação
    # porque ele nao esta validando case sensitive
    # nao esta validando por id e sim pelo nome
    # isso é falho porque deveria ser por id
    # # talvez uma solucao seja fazer ID fixo (ex: sempre regra de * será o ID=1)    
    if Rule.rule_exists(new_rule):
        print('Regra já existe')
        return 'Regra já existe', 500
    else:
        Rule.set_rule(new_rule)
        return redirect(url_for('site.get_rule'), code=200)