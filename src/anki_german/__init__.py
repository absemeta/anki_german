import typer
from .translation import get_translator, Provider

app = typer.Typer()

@app.command()
def translate(
    word: str,
    language: str = typer.Option("german", help="Source language"),
    translate_to: str = typer.Option("english", help="Target language"),
) -> None:
    """
    Translate a word from one language to another.
    Default translation is from German to English.
    """
    try:
        translator = get_translator(Provider.OPENAI)
        result = translator.translate(word, language, translate_to)
        typer.echo(f"Translation: {result}")
    except Exception as e:
        typer.echo(f"Error during translation: {str(e)}", err=True)
        raise typer.Exit(1)

def main():
    app()

if __name__ == '__main__':
    main()
