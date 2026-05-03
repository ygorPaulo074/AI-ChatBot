from invoke import task
from pathlib import Path
import shutil
import subprocess
import sys
import os

ROOT = Path(__file__).resolve().parent


# ── Helpers ────────────────────────────────────────────────────────────────────

def _read_data_path() -> Path:
    env_file = ROOT / ".env"
    data_path = ROOT / "data"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith("DATA_PATH="):
                val = line.split("=", 1)[1].strip()
                if val:
                    data_path = Path(val)
                break
    return data_path


def _clear_agents(data_path: Path) -> None:
    agents_path = data_path / "agents"
    if not agents_path.exists():
        print(f"[clear] Nada para limpar em {agents_path}")
        return
    try:
        shutil.rmtree(agents_path)
        agents_path.mkdir(parents=True)
        print(f"[clear] Limpo: {agents_path}")
    except Exception as e:
        print(f"[clear] Erro: {e}", file=sys.stderr)


def _ensure_initialized() -> bool:
    flag = ROOT / ".initialized"
    if not flag.exists():
        flag.write_text("invoke")
        return True
    return False


# ── Tasks ──────────────────────────────────────────────────────────────────────

@task
def setup(c):
    """Executa o assistente de configuração interativo."""
    c.run("python src/tools/setup.py", pty=True)


@task
def run(c):
    """Sobe o servidor FastAPI com uvicorn em modo reload."""
    _ensure_initialized()
    port = os.getenv("PORT", "8000")
    c.run(f"uvicorn main:app --reload --host 0.0.0.0 --port {port}", pty=True)


@task(help={"args": "Argumentos extras para o pytest (ex: -k test_agent)"})
def test(c, args=""):
    """Executa a suíte de testes e limpa os dados gerados ao final."""
    flag = ROOT / ".initialized"
    flag_created = not flag.exists()
    if flag_created:
        flag.write_text("invoke test")

    cmd = ["python", "-m", "pytest", "src/tests/", "-v", "--tb=short"]
    if args:
        cmd += args.split()

    try:
        result = subprocess.run(cmd, cwd=str(ROOT))
    finally:
        if flag_created and flag.exists():
            flag.unlink()
        _clear_agents(_read_data_path())

    sys.exit(result.returncode)


@task(help={"path": "Caminho alternativo para a pasta de dados"})
def clear(c, path=None):
    """Limpa os dados gerados em desenvolvimento (data/agents/)."""
    data_path = Path(path) if path else _read_data_path()
    _clear_agents(data_path)


@task
def lint(c):
    """Verifica o código com ruff (instale com: pip install ruff)."""
    c.run("ruff check src/ --statistics", warn=True)


@task
def docker_build(c):
    """Builda a imagem Docker (requer Dockerfile gerado pelo setup)."""
    if not (ROOT / "Dockerfile").exists():
        print("[docker-build] Dockerfile não encontrado. Execute 'invoke setup' e escolha Docker.")
        return
    c.run("docker build -t ai-chatbot .", pty=True)
