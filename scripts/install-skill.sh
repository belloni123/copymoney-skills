#!/bin/sh
set -eu

project_root=$(CDPATH='' cd -- "$(dirname -- "$0")/.." && pwd -P)
source_dir="$project_root/.agents/skills/copymoney-copywriter"

usage() {
    printf 'Uso: sh scripts/install-skill.sh [codex|claude|both]\n'
}

if [ "$#" -gt 1 ]; then
    usage >&2
    exit 2
fi

case "${1:-codex}" in
    codex) set -- "$HOME/.agents/skills" ;;
    claude) set -- "$HOME/.claude/skills" ;;
    both) set -- "$HOME/.agents/skills" "$HOME/.claude/skills" ;;
    -h|--help)
        usage
        exit 0
        ;;
    *)
        usage >&2
        exit 2
        ;;
esac

if [ ! -f "$source_dir/SKILL.md" ]; then
    printf 'Skill não encontrada em %s. Rode o instalador a partir de um clone completo.\n' "$source_dir" >&2
    exit 1
fi

is_installed() {
    [ -L "$1" ] && [ "$(readlink "$1")" = "$source_dir" ]
}

for target_dir in "$@"; do
    target="$target_dir/copymoney-copywriter"
    if ! is_installed "$target" && { [ -e "$target" ] || [ -L "$target" ]; }; then
        printf 'Já existe uma instalação diferente em %s. Confira o destino antes de substituir.\n' "$target" >&2
        exit 1
    fi
done

for target_dir in "$@"; do
    target="$target_dir/copymoney-copywriter"
    if is_installed "$target"; then
        printf 'Skill já vinculada em %s\n' "$target"
        continue
    fi
    mkdir -p "$target_dir"
    ln -s "$source_dir" "$target"
    printf 'Skill vinculada em %s\n' "$target"
done
