mkdir -p .Jules
DATE=$(date +%Y-%m-%d)
cat << INNER_EOF >> .Jules/palette.md
## $DATE - [Accessible Names for Icon-Only Buttons]
**Learning:** In Open edX templates, screen reader text for icon-only buttons is frequently implemented using a visually hidden span with the \`sr\` class (e.g., \`<span class="sr">\${_('Close')}</span>\`) rather than exclusively relying on the \`aria-label\` attribute.
**Action:** When adding accessible names to icon-only buttons, either use the \`aria-label\` or \`title\` attributes, or ensure a visually hidden span (with class \`sr\`) is present and that the icon itself is hidden from screen readers using \`aria-hidden="true"\`.

INNER_EOF
