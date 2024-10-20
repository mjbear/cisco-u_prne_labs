#!/usr/bin/env bash

/usr/bin/env python strings.py
/usr/bin/env python -c "print('=' * 80)"

/usr/bin/env python integers.py
/usr/bin/env python -c "print('=' * 80)"

/usr/bin/env python floats.py

echo -e "\nNote: Conversion from binary for float '0.3' results in it being
skipped until rounding is added"

/usr/bin/env python -c 'print(0.2 + 0.1)'
/usr/bin/env python -c "print('=' * 80)"

/usr/bin/env python booleans.py