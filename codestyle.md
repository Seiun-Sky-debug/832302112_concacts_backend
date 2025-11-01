# Backend Code Style Guide

This document outlines the code style and conventions for the Contacts API backend. This guide is based on [Python PEP8](https://legacy.python.org/dev/peps/pep-0008/ "PEP8 Community Guidelines").

## 1. Naming Conventions
- **Modules:** `lowercase_with_underscores`.

- **Classes:** `PascalCase (e.g., ContactModel, DatabaseClient)`.

- **Methods:** `lowercase_with_underscores` (e.g., `get_all_contacts`).

- **Variables:** `lowercase_with_underscores.`

- **Constants:** `UPPERCASE_WITH_UNDERSCORES` (e.g., `DATABASE_URL`).

## 2. Formatting
- **Indentation:** Use 4 spaces per indentation level. Do not use tabs.

- **Line Length:** Limit all lines to a maximum of 120 characters.

- **Imports:** Imports should be on separate lines and grouped in the following order:
    
     1.Standard library imports (e.g., `os`, `sys`).

     2.Third-party imports (e.g., `fastapi`, `beanie`).

     3.Local application/library imports (e.g., `from .models import ...`).

## 3. API Design
- **Path Naming:** Use plural nouns for resource paths (e.g., `/api/contacts`).

- **HTTP Methods:** Use standard HTTP methods correctly:

    - `GET`: Retrieve resources.

    - `POST`: Create new resources.

    - `PUT`: Update/replace existing resources.

    - `DELETE`: Remove resources.

- **Response Codes:** Use appropriate HTTP status codes (e.g., `200 OK`, `201 Created`, `404 Not Found`).

## 4. Type Hinting
- All function definitions must include type hints for arguments and return values.

- Use Pydantic models for all request and response bodies.