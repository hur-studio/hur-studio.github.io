#!/bin/bash
cd "$(dirname "$0")"
echo "Opening Huurs Studio Free 11-Surah Taster Package in browser..."
xdg-open "START_HERE.html" 2>/dev/null || sensible-browser "START_HERE.html" 2>/dev/null || firefox "START_HERE.html" 2>/dev/null || google-chrome "START_HERE.html" 2>/dev/null
