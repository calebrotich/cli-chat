import click
import requests
from user_model import User
from db import database



@click.group()
def main():
    """
    Simple CLI for a chat room
    """
    
    database.create_tables()

@main.command()
def register():
    email = input('Please enter a valid email: ')
    password = input('Please enter a valid password: ')
    role = input('Please enter a role: ')
    new_user = User(email, password, role)
    new_user.save_user()
    click.echo(new_user)


@main.command()
@click.argument('id')
@click.argument('email')


def post(id, email):
    pass



if __name__ == "__main__":
    main()
