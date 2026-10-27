#!/usr/bin/env python3
"""Verify the published evidence package; no EA or PawPath runtime is invoked."""

import csv
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
failures = []


def check(condition, message):
    if not condition:
        failures.append(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def anchor(text):
    text = re.sub(r'[^\w\- ]', '', text.lower())
    return text.replace(' ', '-')


manifest_paths = set()
for line in (ROOT / 'SHA256SUMS.txt').read_text().splitlines():
    expected, name = line.split(None, 1)
    path = ROOT / name
    manifest_paths.add(name)
    check(path.is_file() and digest(path) == expected, f'File hash mismatch: {name}')
actual_paths = {
    p.relative_to(ROOT).as_posix()
    for p in ROOT.rglob('*')
    if p.is_file()
    and '.git' not in p.relative_to(ROOT).parts
    and '__pycache__' not in p.relative_to(ROOT).parts
    and p.name not in {'.DS_Store', 'SHA256SUMS.txt'}
    and p.suffix != '.pyc'
}
check(actual_paths == manifest_paths, 'Manifest coverage differs from public files')

provenance = json.loads((ROOT / 'docs/evidence/provenance.json').read_text())
for asset in provenance['assets']:
    path = ROOT / asset['public_path']
    check(path.is_file() and digest(path) == asset['sha256'], f'Source copy mismatch: {asset["public_path"]}')
check(len(list((ROOT / 'assets/diagrams').glob('*_full.png'))) == 7, 'Expected seven full UML exports')
check(len(list((ROOT / 'assets/diagrams').glob('*_part*.png'))) == 12, 'Expected twelve reading panels')

requirements = json.loads((ROOT / 'analysis/requirements.json').read_text())['stories']
expected_story_ids = {f'{prefix}{i}' for prefix in ('FUS', 'NFUS') for i in range(1, 8)}
check({s['id'] for s in requirements} == expected_story_ids and len(requirements) == 14, 'Story IDs differ')
expected_ac_ids = {f'{story}.AC{i}' for story in expected_story_ids for i in range(1, 7)}
criteria = [c for story in requirements for c in story['criteria']]
check({c['id'] for c in criteria} == expected_ac_ids and len(criteria) == 84, 'Criterion IDs differ')
with (ROOT / 'analysis/acceptance-criteria.csv').open(newline='') as stream:
    rows = list(csv.DictReader(stream))
check({r['criterion_id']: r['criterion'] for r in rows} == {c['id']: c['text'] for c in criteria}, 'CSV and JSON criterion text differ')
with (ROOT / 'analysis/traceability.csv').open(newline='') as stream:
    trace = list(csv.DictReader(stream))
check({r['story_id'] for r in trace} == {f'FUS{i}' for i in range(1, 8)}, 'Functional traceability coverage differs')
with (ROOT / 'analysis/acceptance-review-scenarios.csv').open(newline='') as stream:
    scenarios = list(csv.DictReader(stream))
check(all(r['execution_status'] == 'not_executed_design_review_only' for r in scenarios), 'Review scenarios must remain labelled unexecuted')

record = json.loads((ROOT / 'docs/evidence/supplied-verification.json').read_text())
check(len(record['checks']) == 103 and all(c['status'] == 'PASS' for c in record['checks']), 'Historical static-check inventory differs')
copy_record = json.loads((ROOT / 'docs/evidence/validation-copy-hashes.json').read_text())
check(copy_record['source_sha256'] == copy_record['uq_validation_copy_snapshot_sha256'] == provenance['native_model_sha256'], 'Recorded model hashes differ')
ET.parse(ROOT / 'assets/design-overview.svg')

link_count = 0
for markdown in ROOT.rglob('*.md'):
    text = markdown.read_text()
    check(not re.search(r'\b(?:s\d{7}|\d{8})\b', text), f'Possible student identifier in {markdown.relative_to(ROOT)}')
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if re.match(r'^(https?://|mailto:)', target):
            continue
        location, _, fragment = unquote(target).partition('#')
        path = (markdown.parent / location).resolve() if location else markdown
        link_count += 1
        check(path.is_relative_to(ROOT) and path.is_file(), f'Broken internal link: {markdown.relative_to(ROOT)} -> {target}')
        if fragment and path.is_file() and path.suffix == '.md':
            headings = re.findall(r'^#{1,6}\s+(.+)$', path.read_text(), re.M)
            check(fragment in {anchor(h) for h in headings}, f'Broken heading anchor: {target}')
for path in ROOT.rglob('*'):
    if '.git' in path.relative_to(ROOT).parts:
        continue
    check(path.suffix.lower() not in {'.eapx', '.docx', '.pdf', '.ldb'}, f'Private source format found: {path.relative_to(ROOT)}')

result = {
    'result': 'PASS' if not failures else 'FAIL',
    'manifest_files': len(manifest_paths),
    'byte_identical_source_assets': len(provenance['assets']),
    'stories': len(requirements),
    'acceptance_criteria': len(criteria),
    'functional_traceability_rows': len(trace),
    'unexecuted_review_scenarios': len(scenarios),
    'internal_links_checked': link_count,
    'failures': failures,
    'scope': 'Public-package integrity and documentation only; historical EA checks read, not rerun; no PawPath runtime tests.'
}
print(json.dumps(result, indent=2))
sys.exit(bool(failures))
