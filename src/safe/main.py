import click
from encrypt import encrypt_data
from decrypt import decrypt_data
from helpers import load_file, save_file

@click.group()
def cli():
    """A CLI tool for file encryption and decryption."""
    pass

@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--key', prompt=True, hide_input=True, confirmation_prompt=True, help="Encryption key")
def encrypt(input_file, output_file, key):
    """Encrypt the INPUT_FILE and save it as OUTPUT_FILE."""
    data = load_file(input_file)
    encrypted_data = encrypt_data(data, key)
    save_file(output_file, encrypted_data)
    click.echo(f"File encrypted and saved to {output_file}")

@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--key', prompt=True, hide_input=True, confirmation_prompt=True, help="Decryption key")
def decrypt(input_file, output_file, key):
    """Decrypt the INPUT_FILE and save it as OUTPUT_FILE."""
    data = load_file(input_file)
    decrypted_data = decrypt_data(data, key)
    save_file(output_file, decrypted_data)
    click.echo(f"File decrypted and saved to {output_file}")

if __name__ == '__main__':
    cli()
