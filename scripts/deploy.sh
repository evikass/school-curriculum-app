#!/bin/bash
# Setup git identity for gh-pages deploy
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"
npx gh-pages -d out -t
