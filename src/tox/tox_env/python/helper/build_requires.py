"""
Get environment requires per PEP-517.
"""

import json
import sys

into = sys.argv[1]
backend_spec = sys.argv[2]
backend_obj = sys.argv[3] if len(sys.argv) >= 4 else None


backend = __import__(backend_spec, fromlist=[None])  # type: ignore[list-item]
if backend_obj:
    backend = getattr(backend, backend_obj)

for_build_requires = backend.get_requires_for_build_sdist(None)

with open(into, "w") as file_handler:
    json.dump(for_build_requires, file_handler)