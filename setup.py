from cx_Freeze import setup, Executable

setup(
    name="pokemon-mystery-gift-code-helper",
    version="1.0",
    description="A helper tool for Pokémon Mystery Gift codes",
    executables=[Executable("main.py", base=None, target_name="PokemonMysteryGiftCodeHelper")]
)
