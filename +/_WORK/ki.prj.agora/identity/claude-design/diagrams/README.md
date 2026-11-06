# Diagrams

Mermaid sources and their renderings for [architecture.md](../architecture.md).

| Picture | Source | Light | Night |
| --- | --- | --- | --- |
| One Mac | `1-one-mac.mmd` | `1-one-mac.svg` | `1-one-mac-night.svg` |
| Two Macs | `2-two-macs.mmd` | `2-two-macs.svg` | `2-two-macs-night.svg` |
| The life of a message | `3-life-of-a-message.mmd` | `3-life-of-a-message.svg` | `3-life-of-a-message-night.svg` |

The colours are `ki-design` tokens. `mermaid.config.json` sets the light theme; each source sets the node colours with its `classDef` lines. The night rendering is made from the light SVG by `night.py`, which swaps each light token for its night token.

To render again, with the Mermaid CLI 11 (`mmdc`), which carries the ELK layout the first two use:

```sh
for f in 1-one-mac 2-two-macs 3-life-of-a-message; do
  mmdc -c mermaid.config.json -b '#f5efe0' -i $f.mmd -o $f.svg
  python3 night.py $f.svg
done
```
