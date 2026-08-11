# Mr.Holmes Architecture Overview

## Current structure
The project is organized around a set of core modules for OSINT tasks, reports, UI assets, and support functions.

## Suggested evolution
A future version could follow a more modular layout:

- core/: base orchestration and shared utilities
- modules/: domain, username, email, phone, DNS, and other investigation modules
- gui/: interface-related assets and views
- reports/: generated summaries, exports, and reports
- plugins/: optional integrations and extensions
- api/: REST endpoints for automation and integrations
- tests/: validation and regression coverage
- docs/: user and contributor documentation

## Design principles
- Keep the OSINT logic isolated from the UI layer
- Favor small, testable modules over tightly coupled functions
- Make reporting and presentation reusable across modules
- Prepare the project for future plugin extensions
