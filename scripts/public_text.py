"""Text cleanup shared by the public site and the fact-check package: removes internal shorthand (registry ids,
knowledge-base paths, pass names) from the written bases of oil-tier rulings so an outside reader sees only the reason."""
import re
INTERNAL = [r'knowledge-wiki/entities/\S+ ', r'registry E-\d+', r'E-\d{7}(/E-\d{7})?', r'O-\d{5}', r'\[matched on [^\]]*\]',
            r'^plan ruling(: flagged)?[.;:]? ?', r'^career carry-over: ', r"^explicit key for the \* ruling \(an official-and-zip 'unclassified' row outranked it\): ",
            r'people\.csv ', r'orgs\.csv ', r'\s*;\s*$']


def clean(basis):
    b = basis or ''
    b = re.sub(r"keyword '([^']+)'", r"filed employer or occupation names '\1'", b)
    b = re.sub(r'plan ruling \(([^)]*)\)', r'\1', b)
    b = re.sub(r'merged with him under \d{5} in the entity pass', 'files with him', b)
    for pat in INTERNAL + [r';?\s*registry\b', r'\bplan ruling\b[:;.]?', r'\bstrict\b', r'\bthe entity pass\b']:
        b = re.sub(pat, '', b)
    b = re.sub(r'\(\s*;?\s*', '(', b); b = re.sub(r'\s*;?\s*\)', ')', b)
    b = re.sub(r'(;\s*)+;', ';', b); b = re.sub(r'\s+([;,.:])', r'\1', b)
    b = re.sub(r'\(\)', '', b)
    return re.sub(r'\s{2,}', ' ', b).strip(' ;:,')


