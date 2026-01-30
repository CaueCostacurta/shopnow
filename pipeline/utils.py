from pathlib import Path
from pipeline.metas_generator import find_repo_root

# Função para encontrar o diretório raiz do repositório
def find_repo_root(start: Path = Path.cwd()) -> Path:
    p = start.resolve()
    for parent in [p] + list(p.parents):
        if (parent / "README.md").exists() or (parent / ".git").exists():
            return parent
    return p  # fallback: cwd

# Cria o diretório de dados brutos, se não existir
def create_raw_dir() -> Path:
    BASE_DIR = find_repo_root()
    RAW_DIR = BASE_DIR / "data" / "raw"
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    return RAW_DIR

# Define o diretório base e o diretório de dados brutos
def get_raw_dir() -> Path:
    BASE_DIR = find_repo_root()
    RAW_DIR = BASE_DIR / "data" / "raw"
    return RAW_DIR