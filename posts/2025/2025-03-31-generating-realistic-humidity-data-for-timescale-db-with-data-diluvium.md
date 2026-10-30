---
title: Generating Realistic Humidity Data for TimeScale DB with Data Diluvium
date: 2025-03-31 13:01:21 -0700
last_modified_at: 2025-03-31 13:02:37 -0700
permalink: /2025/03/31/generating-realistic-humidity-data-for-timescale-db-with-data-diluvium/
slug: generating-realistic-humidity-data-for-timescale-db-with-data-diluvium
wp_id: 71689
original_url: https://compositecode.blog/2025/03/31/generating-realistic-humidity-data-for-timescale-db-with-data-diluvium/
categories:
- Coding Adventures
- Coding Patterns & Practices
- Data Diluvium
- Databases
tags:
- datadiluvium
- generating data
- humidity
- random data
- timescaledb
excerpt: The post discusses the creation of a humidity data generator for TimeScale DB, highlighting its significance in environmental monitoring and IoT applications. Key features include realistic humidity levels, time and seasonal variations, and compatibility with various numeric types. Comprehensive testing ensures the generator produces reliable values for further development.
image: /wp-content/uploads/2025/03/CleanShot-2025-03-31-at-12.01.33@2x.png
---

For next steps of why I [set up TimeScale DB](/2025/03/28/setup-timescaledb-with-docker-compose-a-step-by-step-guide/) up for local dev, and [being able to just do things](/2025/03/28/staying-in-software-dev-best-be-able-to-just-do-things/), I need two new data generators over on [Data Diluvium](https://www.datadiluvium.com/). One for humidity, which will be this post, and one for temperature, which will be next.

### Why Humidity Data?

When working with TimeScale DB for time-series data, having realistic environmental data is crucial. I’ve found that humidity is a particularly important parameter that affects everything from agriculture to HVAC systems. Having realistic humidity data is essential for:

- Testing environmental monitoring systems
- Simulating weather conditions
- Developing IoT applications
- Training machine learning models for climate prediction

### The Implementation

I created a humidity generator that produces realistic values based on typical Earth conditions. Here’s what I considered:

- Average humidity ranges (typically 30-70% for most inhabited areas)
- Daily variations (higher in the morning, lower in the afternoon)
- Seasonal patterns
- Geographic influences

With the definition of what needs to be generated, I created a table schema for Data Diluvium that would use this (and the temperature) data generators.

[![](/wp-content/uploads/2025/03/CleanShot-2025-03-31-at-11.59.08@2x.png)](/wp-content/uploads/2025/03/CleanShot-2025-03-31-at-11.59.08@2x.png)

```
CREATE TABLE TestingHumidityAndTemperature (
    Identifier UUID PRIMARY KEY,
    StampInTime DATETIME,
    Temperature DOUBLE,
    Humidity DOUBLE
);
```

Since both Temperature and Humidity generators will be double values, to test humidity while we implement, I’ll just set temperature to humidity too.

### The Data Diluvium App Code

Here’s how I implemented this in Data Diluvium:

```
export const humidityGenerator: GeneratorConfig = {
  name: 'Humidity',
  description: 'Generates realistic humidity values with daily and seasonal variations',
  category: 'number',
  compatibleTypes: [
    'NUMBER', 'DECIMAL', 'NUMERIC', 'FLOAT', 'DOUBLE',
    'NUMBER(5,2)', 'DECIMAL(5,2)', 'NUMERIC(5,2)'
  ],
  defaultOptions: {
    minHumidity: 30,
    maxHumidity: 70,
    includeTimeVariation: true,
    includeSeasonalVariation: true
  },
  generate: async (count: number, options?: GeneratorOptions) => {
    const finalOptions = { ...humidityGenerator.defaultOptions, ...options };

    return Array.from({ length: count }, () => {
      let baseHumidity = finalOptions.minHumidity! +
        (Math.random() * (finalOptions.maxHumidity! - finalOptions.minHumidity!));

      if (finalOptions.includeTimeVariation) {
        // Add daily variation (higher in morning, lower in afternoon)
        const hour = new Date().getHours();
        const timeFactor = Math.sin((hour - 6) * Math.PI / 12); // Peak at 6 AM
        baseHumidity += timeFactor * 10;
      }

      if (finalOptions.includeSeasonalVariation) {
        // Add seasonal variation (higher in winter, lower in summer)
        const month = new Date().getMonth();
        const seasonalFactor = Math.sin((month - 1) * Math.PI / 6); // Peak in January
        baseHumidity += seasonalFactor * 5;
      }

      // Ensure the value stays within bounds
      return Math.max(finalOptions.minHumidity!, Math.min(finalOptions.maxHumidity!, baseHumidity));
    });
  }
};
```

### Using the Generator with TimeScale DB

I’ve made it easy to use this generator in your Data Diluvium configuration like this:

```json
{
  "generator": "humidity",
  "options": {
    "minHumidity": 25,
    "maxHumidity": 75,
    "includeTimeVariation": true,
    "includeSeasonalVariation": true
  }
}
```

This configuration works perfectly with TimeScale DB’s time-series capabilities, allowing you to generate continuous humidity data that follows natural patterns over time.

## What Makes This Implementation Special?

I’ve designed this implementation with several key features that work well with time-series databases:

1. **Realistic Ranges**: I set the default range of 30-70% to cover most inhabited areas on Earth.
2. **Time-Aware**: The generator considers daily patterns, producing higher values in the morning and lower values in the afternoon.
3. **Seasonal Awareness**: Values naturally vary with the seasons, higher in winter and lower in summer.
4. **Flexible Configuration**: I’ve made it easy to customize the ranges and toggle features as needed.
5. **Type Compatibility**: The generator supports various numeric SQL types including NUMBER, DECIMAL, NUMERIC, FLOAT, and DOUBLE.

## Testing the Generator

I’ve implemented comprehensive testing to ensure our humidity generator produces realistic values that will work well with TimeScale DB:

```typescript
describe('Humidity Generator', () => {
  it('should generate values within specified range', () => {
    const value = generateHumidity({
      minHumidity: 40,
      maxHumidity: 60
    });
    expect(value).toBeGreaterThanOrEqual(40);
    expect(value).toBeLessThanOrEqual(60);
  });

  it('should respect time-based variations', () => {
    const morningValue = generateHumidity({ includeTimeVariation: true });
    const afternoonValue = generateHumidity({ includeTimeVariation: true });
    expect(morningValue).toBeGreaterThan(afternoonValue);
  });
});
```

Alright, next up I’m going to test this and see what I get. Clicking over to the generate data tab it looks like the data is generating as expected and what is being generated will work for what I need.

[![](/wp-content/uploads/2025/03/CleanShot-2025-03-31-at-12.01.33@2x.png)](/wp-content/uploads/2025/03/CleanShot-2025-03-31-at-12.01.33@2x.png)

Clicking through again to generate data, the humidity settings look *mostly* ok. I think I’ll come back to this after a while, and maybe change some parameters. But for now, this is good for what I’ll need for further testing and development.

[![](/wp-content/uploads/2025/03/CleanShot-2025-03-31-at-12.05.47@2x.png)](/wp-content/uploads/2025/03/CleanShot-2025-03-31-at-12.05.47@2x.png)

Next up I’ll add the temperature generator, tweak them until they’re effective, and will get a feature addition up at <https://datadiluvium.com> and you too can give em’ a try!

With that, until next time *happy thrashing coding*! 🚀
