---
title: 'Building DataDiluvium: A Data Generation Tool – Part 2: Core Implementation and Schema Handling'
date: 2025-03-20 08:00:00 -0700
last_modified_at: 2025-03-21 12:17:17 -0700
permalink: /2025/03/20/building-datadiluvium-a-data-generation-tool-part-2-core-implementation-and-schema-handling/
slug: building-datadiluvium-a-data-generation-tool-part-2-core-implementation-and-schema-handling
wp_id: 71501
original_url: https://compositecode.blog/2025/03/20/building-datadiluvium-a-data-generation-tool-part-2-core-implementation-and-schema-handling/
categories:
- Programming
tags:
- coding
- data generation
- database
- programming
image: /wp-content/uploads/2025/03/2-data-diluvium-core-and-schema.png
---

In Part 1, we set up our development environment and outlined the project structure. Now, we’ll dive into implementing the core functionality of DataDiluvium, starting with SQL schema parsing and the user interface for schema input.

## SQL Schema Parsing Implementation

### 1. SQL Parser Setup

The SQL parser is implemented in `src/app/lib/parsers/sqlParser.ts`. This module is responsible for:

1. Parsing SQL schema definitions using the `node-sql-parser` library
2. Extracting table and column information
3. Mapping SQL data types to appropriate data generators

The parser works by:

1. Taking a SQL string input
2. Converting it to an Abstract Syntax Tree (AST)
3. Traversing the AST to extract:
   - Table names
   - Column names
   - Data types
   - Default values
   - Foreign key relationships

The `SchemaColumn` type defines the structure of our parsed columns:

```typescript
export type SchemaColumn = {
  tableName: string;
  columnName: string;
  dataType: string;
  defaultValue: string | null;
  generator?: string;
  referencedTable?: string;
  referencedColumn?: string;
};
```

### 2. Schema Validation

The validation system is implemented in `src/app/lib/validators/schemaValidator.ts`. This module performs several important validations:

1. Duplicate Column Check:

   - Ensures no duplicate column names exist within the same table
   - Uses a Map to track columns per table
2. Foreign Key Validation:

   - Verifies that referenced tables and columns exist
   - Checks for circular references
   - Validates data type compatibility

The validation results are structured as:

```typescript
type ValidationResult = {
  errors: ValidationError[];
  warnings: ValidationWarning[];
};
```

## User Interface Implementation

### 1. Schema Input Component

The main schema input interface is implemented in `src/app/components/SchemaInput.tsx`. This component provides:

1. A textarea for SQL schema input
2. Real-time validation feedback
3. A preview of the parsed schema
4. Error and warning displays

The component uses Tailwind CSS for styling and is structured as:

```tsx
<div className="space-y-4">
  {/* SQL Input Section */}
  <div className="flex flex-col space-y-2">
    <label>SQL Schema</label>
    <textarea
      value={schemaText}
      onChange={handleSchemaChange}
      className="w-full h-64 p-4 font-mono text-sm border rounded-md"
    />
  </div>

  {/* Validation Results Section */}
  <div className="space-y-2">
    {/* Error and Warning Displays */}
  </div>

  {/* Schema Preview Section */}
  <div className="mt-4">
    {/* Table Preview */}
  </div>
</div>
```

### 2. Real-time Validation and Error Handling

The debounced validation system is implemented in `src/app/lib/hooks/useDebounce.ts`. This custom hook:

1. Prevents excessive validation calls while typing
2. Waits for a specified delay before updating
3. Cleans up timeouts on unmount

Usage example:

```typescript
const debouncedSchema = useDebounce(schemaText, 500);
```

## Building the Foundation

### 1. State Management

The state management system is implemented in `src/app/lib/context/SchemaContext.tsx`. This context provides:

1. Global schema state
2. Validation results
3. State update methods

The context is wrapped around the application in `src/app/layout.tsx`:

```tsx
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <SchemaProvider>
          {children}
        </SchemaProvider>
      </body>
    </html>
  );
}
```

### 2. Navigation and Layout

The navigation component is implemented in `src/app/components/Navigation.tsx`. This component:

1. Provides consistent navigation across pages
2. Implements dark mode support
3. Uses Next.js Link components for client-side navigation

The layout structure follows Next.js 13+ app router conventions:

```
src/app/
├── layout.tsx        # Root layout with providers
├── page.tsx          # Home page
├── schema/
│   └── page.tsx      # Schema input page
├── generate/
│   └── page.tsx      # Data generation page
└── generated/
    └── page.tsx      # Generated data display page
```

## Next Steps

In Part 3, we’ll explore:

- Implementing the data generation system
- Creating the export functionality
- Adding dark mode support
- Implementing responsive design
- Adding error boundaries and loading states

Stay tuned for the final part of our series, where we’ll complete the DataDiluvium implementation!
