---
title: 'Building DataDiluvium: A Data Generation Tool – Part 3: Data Generation and Final Implementation'
date: 2025-03-21 08:00:00 -0700
last_modified_at: 2025-03-21 12:13:18 -0700
permalink: /2025/03/21/building-datadiluvium-a-data-generation-tool-part-3-data-generation-and-final-implementation/
slug: building-datadiluvium-a-data-generation-tool-part-3-data-generation-and-final-implementation
wp_id: 71502
original_url: https://compositecode.blog/2025/03/21/building-datadiluvium-a-data-generation-tool-part-3-data-generation-and-final-implementation/
categories:
- Programming
tags:
- coding
- data generation
- database
- programming
excerpt: The content outlines the completion of DataDiluvium, a test data generator from SQL schemas. It details the data generation system with various built-in generators, supports multiple export formats, includes dark mode, features responsive design, and implements error handling and loading states. The application adheres to best practices for deployment.
image: /wp-content/uploads/2025/03/3-data-diluvium-data-gen.png
---

In Parts 1 and 2, I set up the development environment and implemented the schema parsing functionality. Now, I’ll explore the data generation system and final implementation details that make DataDiluvium a complete solution.

## Data Generation System

### 1. Generator Registry

I’ve implemented the generator system in `src/app/lib/generators/registry.ts`. This registry manages different types of data generators:

```typescript
import { Generator } from './types';
import { SequentialNumberGenerator } from './basic';
import { UsernameGenerator } from './basic';
import { DateGenerator } from './basic';
import { ForeignKeyGenerator } from './basic';

export const generatorRegistry = new Map<string, Generator>();

// Register built-in generators
generatorRegistry.set('Sequential Number', new SequentialNumberGenerator());
generatorRegistry.set('Username', new UsernameGenerator());
generatorRegistry.set('Date', new DateGenerator());
generatorRegistry.set('Foreign Key', new ForeignKeyGenerator());
```

### 2. Generator Types

I’ve defined the Generator interface in `src/app/lib/generators/types.ts`:

```typescript
export interface Generator {
  name: string;
  generate(count: number): Promise<any[]>;
  validate(value: any): boolean;
}
```

### 3. Built-in Generators

I’ve implemented several built-in generators in `src/app/lib/generators/basic.ts`:

```typescript
export class SequentialNumberGenerator implements Generator {
  private nextNumber: number = 1;

  async generate(count: number): Promise<number[]> {
    const numbers = Array.from(
      { length: count },
      () => this.nextNumber++
    );
    return numbers;
  }
}

export class UsernameGenerator implements Generator {
  async generate(count: number): Promise<string[]> {
    return Array.from({ length: count }, () =>
      faker.internet.userName()
    );
  }
}
```

## Export Functionality

### 1. Export Implementation

I’ve implemented the export functionality in `src/app/generated/page.tsx`. The export system supports multiple formats:

```typescript
const exportData = () => {
  if (!generatedData) return;

  Object.entries(generatedData).forEach(([tableName, tableData]) => {
    let content: string;
    let extension: string;
    let mimeType: string;

    switch (selectedExportFormat) {
      case 'json':
        content = JSON.stringify(tableData, null, 2);
        extension = '.json';
        mimeType = 'application/json';
        break;
      case 'json-rich':
        const richData = tableData.rows.map(row => {
          const obj: { [key: string]: any } = {};
          tableData.columns.forEach((col, index) => {
            obj[col] = row[index];
          });
          return obj;
        });
        content = JSON.stringify(richData, null, 2);
        extension = '.json';
        mimeType = 'application/json';
        break;
      case 'csv':
        // CSV implementation
        break;
      case 'xml':
        // XML implementation
        break;
      case 'txt':
        // Plain text implementation
        break;
      case 'sql':
        // SQL inserts implementation
        break;
    }
  });
};
```

## Dark Mode Support

### 1. Theme Implementation

I’ve implemented dark mode using Tailwind CSS and Next.js. The theme configuration is in `tailwind.config.ts`:

```typescript
module.exports = {
  darkMode: 'class',
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Custom color palette
      },
    },
  },
  plugins: [],
}
```

### 2. Theme Toggle

I’ve implemented the theme toggle in `src/app/components/ThemeToggle.tsx`:

```typescript
export function ThemeToggle() {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');

  useEffect(() => {
    const savedTheme = localStorage.getItem('theme') as 'light' | 'dark';
    if (savedTheme) {
      setTheme(savedTheme);
      document.documentElement.classList.toggle('dark', savedTheme === 'dark');
    }
  }, []);

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    document.documentElement.classList.toggle('dark');
  };

  return (
    <button
      onClick={toggleTheme}
      className="p-2 rounded-md hover:bg-gray-100 dark:hover:bg-gray-800"
    >
      {theme === 'light' ? '🌙' : '☀️'}
    </button>
  );
}
```

## Responsive Design

### 1. Layout Components

I’ve implemented the responsive layout across multiple components:

1. Navigation (`src/app/components/Navigation.tsx`):

```typescript
<nav className="fixed left-0 top-0 h-full w-48 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800">
  {/* Navigation content */}
</nav>
```

2. Main Content (`src/app/layout.tsx`):

```typescript
<div className="min-h-screen p-8 sm:p-20 ml-48">
  {children}
</div>
```

## Error Boundaries and Loading States

### 1. Error Boundary

I’ve implemented the error boundary in `src/app/components/ErrorBoundary.tsx`:

```typescript
export class ErrorBoundary extends React.Component<
  { children: React.ReactNode },
  { hasError: boolean }
> {
  constructor(props: { children: React.ReactNode }) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error: any) {
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="p-4 bg-red-50 dark:bg-red-900/20 text-red-700 dark:text-red-300 rounded-md">
          <h2 className="text-lg font-semibold">Something went wrong</h2>
          <p>Please try refreshing the page</p>
        </div>
      );
    }

    return this.props.children;
  }
}
```

### 2. Loading States

I’ve implemented loading states using React Suspense and loading.tsx files in the app directory:

```typescript
// src/app/loading.tsx
export default function Loading() {
  return (
    <div className="flex items-center justify-center min-h-screen">
      <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
    </div>
  );
}
```

## Conclusion

I’ve now completed DataDiluvium as a full solution for generating test data from SQL schemas. The application features:

- Robust SQL schema parsing
- Flexible data generation system
- Multiple export formats
- Dark mode support
- Responsive design
- Error handling and loading states

I’ve organized the code following Next.js 13+ best practices and used modern React patterns throughout. The application is ready for deployment and can be extended with additional generators and export formats as needed.
