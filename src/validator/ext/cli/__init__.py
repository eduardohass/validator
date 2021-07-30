import click
# from validator.ext.db import bancodados 

def init_app(app):
    
    @app.cli.command()
    def get_rules():
        """Responsável por retornar todas as regras cadastradas no banco de dados.

        Returns:
            [type]: [description]
        """
        click.echo("Todos as regras do database")