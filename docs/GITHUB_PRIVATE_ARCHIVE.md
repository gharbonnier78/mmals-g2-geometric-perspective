# Private GitHub archive procedure

```bash
git init
git add .
git commit -m "Freeze MMALS G2 reflection snapshot v0.2-internal"
git tag -a v0.2-internal -m "Private MMALS G2 context snapshot - 2026-07-17"
git remote add origin <PRIVATE_REPOSITORY_URL>
git push -u origin main --follow-tags
```

Repository visibility should remain **private**. The PDF and private publication-plan chapter are intentionally included. Before any public fork or release, remove or deliberately rewrite the Guillaume-only chapter and rerun the release gates recorded in `docs/PRIVATE_PUBLICATION_AND_GATE_PLAN.md`.
