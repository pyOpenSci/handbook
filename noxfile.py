import os
import nox

nox.options.reuse_existing_virtualenvs = True

OUTPUT_DIR = "_build"
docs_dir = os.path.join("_build", "html")
build_command = ["-b", "html", ".", docs_dir]


@nox.session
def docs(session):
    session.install("-e", ".")
    cmd = ["sphinx-build"]
    cmd.extend(build_command + session.posargs)
    session.run(*cmd)


@nox.session(name="docs-live")
def docs_live(session):
    session.install("-e", ".")

    AUTOBUILD_IGNORE = [
        "_build",
        "build_assets",
        "tmp",
    ]
    cmd = ["sphinx-autobuild"]
    for folder in AUTOBUILD_IGNORE:
        cmd.extend(["--ignore", f"*/{folder}/*"])
    cmd.extend(build_command + session.posargs)
    session.run(*cmd)
