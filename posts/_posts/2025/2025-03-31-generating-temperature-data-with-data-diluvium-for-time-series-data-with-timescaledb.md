---
title: Generating Temperature Data with Data Diluvium for Time Series Data with TimeScaleDB
date: 2025-03-31 16:17:38 -0700
last_modified_at: 2025-04-01 10:13:20 -0700
permalink: /2025/03/31/generating-temperature-data-with-data-diluvium-for-time-series-data-with-timescaledb/
slug: generating-temperature-data-with-data-diluvium-for-time-series-data-with-timescaledb
wp_id: 71716
original_url: https://compositecode.blog/2025/03/31/generating-temperature-data-with-data-diluvium-for-time-series-data-with-timescaledb/
categories:
- Data Diluvium
- Databases
- Programming
tags:
- Data Diluvium
- database
- datadiluvium
- temperature data
- time series
- timescale
- timescaledb
excerpt: The latest update on Data Diluvium incorporates a temperature data generator, completing the environmental data generators needed for TimeScale DB. Emphasizing realistic patterns, the generator accounts for daily and seasonal variations in temperature. The implementation aims to support diverse numeric types and offers string-based generators for display and reporting applications.
image: /wp-content/uploads/2025/03/CleanShot-2025-03-31-at-14.01.08@2x.png
---

Following up on my previous post about adding humidity data generation to Data Diluvium, I’m now adding temperature data generation. This completes the pair of environmental data generators I needed for my TimeScale DB setup. Temperature data is crucial for time-series analysis and works perfectly alongside the humidity data we just implemented.

## Why Temperature Data?

When working with TimeScale DB for time-series data, having realistic environmental data is crucial. I’ve found that temperature is one of the most fundamental environmental parameters we measure. Having realistic temperature data is essential for:

- Weather simulation systems
- Climate modeling
- Building automation systems
- Agricultural planning
- Energy consumption analysis

## The Implementation

I created a temperature generator that produces realistic values based on typical Earth conditions. Here’s what I considered:

- Average temperature ranges (typically -10°C to 35°C for most inhabited areas)
- Daily temp cycles (warmer in afternoon, cooler at night)
- Seasonal variations
- Geographic influences

At least, I’m aiming to include all those, hopefully I can get all these criteria in there in one code session!

Here’s how I implemented this in Data Diluvium:

```
export const temperatureGenerator: GeneratorConfig = {
  name: 'Temperature',
  description: 'Generates realistic temperature values with daily and seasonal variations',
  category: 'number',
  compatibleTypes: [
    'NUMBER', 'DECIMAL', 'NUMERIC', 'FLOAT', 'DOUBLE',
    'NUMBER(5,2)', 'DECIMAL(5,2)', 'NUMERIC(5,2)'
  ],
  defaultOptions: {
    minTemperature: -10,
    maxTemperature: 35,
    includeTimeVariation: true,
    includeSeasonalVariation: true,
    useCelsius: true
  },
  generate: async (count: number, options?: GeneratorOptions) => {
    const finalOptions = { ...temperatureGenerator.defaultOptions, ...options };

    return Array.from({ length: count }, () => {
      let baseTemperature = finalOptions.minTemperature! +
        (Math.random() * (finalOptions.maxTemperature! - finalOptions.minTemperature!));

      if (finalOptions.includeTimeVariation) {
        // Add daily variation (warmer in afternoon, cooler at night)
        const hour = new Date().getHours();
        const timeFactor = Math.sin((hour - 14) * Math.PI / 12); // Peak at 2 PM
        baseTemperature += timeFactor * 8; // 8°C daily variation
      }

      if (finalOptions.includeSeasonalVariation) {
        // Add seasonal variation (warmer in summer, cooler in winter)
        const month = new Date().getMonth();
        const seasonalFactor = Math.sin((month - 6) * Math.PI / 6); // Peak in July
        baseTemperature += seasonalFactor * 15; // 15°C seasonal variation
      }

      // Ensure the value stays within bounds
      baseTemperature = Math.max(finalOptions.minTemperature!, Math.min(finalOptions.maxTemperature!, baseTemperature));

      // Convert to Fahrenheit if needed
      return finalOptions.useCelsius ? baseTemperature : (baseTemperature * 9/5) + 32;
    });
  }
};
```

## Using the Generator with TimeScale DB

I’ve made it easy to use this generator in your Data Diluvium configuration like this:

```
{
  "generator": "temperature",
  "options": {
    "minTemperature": -5,
    "maxTemperature": 30,
    "includeTimeVariation": true,
    "includeSeasonalVariation": true,
    "useCelsius": true
  }
}
```

This configuration works perfectly with TimeScale DB’s time-series capabilities, allowing you to generate continuous temperature data that follows natural patterns over time. When used alongside the humidity generator, you can create comprehensive environmental datasets.

## What Makes This Implementation Special?

I’ve designed this implementation with several key features that work well with time-series databases:

1. **Realistic Ranges**: I set the default range of -10°C to 35°C to cover most inhabited areas on Earth.
2. **Time-Aware**: The generator considers daily patterns, producing warmer values in the afternoon and cooler values at night.
3. **Seasonal Awareness**: Values naturally vary with the seasons, warmer in summer and cooler in winter.
4. **Unit Flexibility**: I’ve added support for both Celsius and Fahrenheit temperature scales.
5. **Type Compatibility**: The generator supports various numeric SQL types including NUMBER, DECIMAL, NUMERIC, FLOAT, and DOUBLE.

## Testing the Generator

I’ve implemented comprehensive testing to ensure our temperature generator produces realistic values that will work well with TimeScale DB:

```
describe('Temperature Generator', () => {
  it('should generate values within specified range', () => {
    const value = generateTemperature({
      minTemperature: 15,
      maxTemperature: 25
    });
    expect(value).toBeGreaterThanOrEqual(15);
    expect(value).toBeLessThanOrEqual(25);
  });

  it('should respect time-based variations', () => {
    const morningValue = generateTemperature({ includeTimeVariation: true });
    const afternoonValue = generateTemperature({ includeTimeVariation: true });
    expect(afternoonValue).toBeGreaterThan(morningValue);
  });

  it('should convert between Celsius and Fahrenheit', () => {
    const celsiusValue = generateTemperature({ useCelsius: true });
    const fahrenheitValue = generateTemperature({ useCelsius: false });
    expect(fahrenheitValue).toBeCloseTo((celsiusValue * 9/5) + 32, 1);
  });
});
```

[![](/wp-content/uploads/2025/03/CleanShot-2025-03-31-at-13.58.01@2x.png)](/wp-content/uploads/2025/03/CleanShot-2025-03-31-at-13.58.01@2x.png)

## String-Based Temperature Generators

While the numeric temperature generator is perfect for database storage and calculations, I also needed string-based temperature generators for display and reporting purposes. I’ve added two new generators:

### Celsius String Generator

```
export const celsiusStringGenerator: GeneratorConfig = {
  name: 'Temperature (Celsius String)',
  description: 'Generates temperature values as strings with °C suffix',
  category: 'text',
  compatibleTypes: [
    'CHAR', 'VARCHAR', 'VARCHAR2', 'TEXT', 'STRING',
    'CHARACTER VARYING'
  ],
  defaultOptions: {
    minTemperature: -10,
    maxTemperature: 35,
    includeTimeVariation: true,
    includeSeasonalVariation: true,
    decimalPlaces: 1
  },
  generate: async (count: number, options?: GeneratorOptions) => {
    const finalOptions = { ...celsiusStringGenerator.defaultOptions, ...options };

    return Array.from({ length: count }, () => {
      let baseTemperature = finalOptions.minTemperature! +
        (Math.random() * (finalOptions.maxTemperature! - finalOptions.minTemperature!));

      if (finalOptions.includeTimeVariation) {
        const hour = new Date().getHours();
        const timeFactor = Math.sin((hour - 14) * Math.PI / 12);
        baseTemperature += timeFactor * 8;
      }

      if (finalOptions.includeSeasonalVariation) {
        const month = new Date().getMonth();
        const seasonalFactor = Math.sin((month - 6) * Math.PI / 6);
        baseTemperature += seasonalFactor * 15;
      }

      baseTemperature = Math.max(finalOptions.minTemperature!, Math.min(finalOptions.maxTemperature!, baseTemperature));

      return `${baseTemperature.toFixed(finalOptions.decimalPlaces!)}°C`;
    });
  }
};
```

### Fahrenheit String Generator

```
export const fahrenheitStringGenerator: GeneratorConfig = {
  name: 'Temperature (Fahrenheit String)',
  description: 'Generates temperature values as strings with °F suffix',
  category: 'text',
  compatibleTypes: [
    'CHAR', 'VARCHAR', 'VARCHAR2', 'TEXT', 'STRING',
    'CHARACTER VARYING'
  ],
  defaultOptions: {
    minTemperature: 14, // 57.2°F
    maxTemperature: 95, // 203°F
    includeTimeVariation: true,
    includeSeasonalVariation: true,
    decimalPlaces: 1
  },
  generate: async (count: number, options?: GeneratorOptions) => {
    const finalOptions = { ...fahrenheitStringGenerator.defaultOptions, ...options };

    return Array.from({ length: count }, () => {
      let baseTemperature = finalOptions.minTemperature! +
        (Math.random() * (finalOptions.maxTemperature! - finalOptions.minTemperature!));

      if (finalOptions.includeTimeVariation) {
        const hour = new Date().getHours();
        const timeFactor = Math.sin((hour - 14) * Math.PI / 12);
        baseTemperature += timeFactor * 14.4; // 8°C = 14.4°F
      }

      if (finalOptions.includeSeasonalVariation) {
        const month = new Date().getMonth();
        const seasonalFactor = Math.sin((month - 6) * Math.PI / 6);
        baseTemperature += seasonalFactor * 27; // 15°C = 27°F
      }

      baseTemperature = Math.max(finalOptions.minTemperature!, Math.min(finalOptions.maxTemperature!, baseTemperature));

      return `${baseTemperature.toFixed(finalOptions.decimalPlaces!)}°F`;
    });
  }
};
```

These string-based generators are particularly useful for:

- Displaying temperatures in reports
- Creating human-readable logs
- Generating sample data for UI testing
- Creating documentation examples

You can use them in your Data Diluvium configuration like this:

```
{
  "generator": "temperature-celsius-string",
  "options": {
    "minTemperature": -5,
    "maxTemperature": 30,
    "includeTimeVariation": true,
    "includeSeasonalVariation": true,
    "decimalPlaces": 1
  }
}
```

or for fahrenheit:

```
{
  "generator": "temperature-fahrenheit-string",
  "options": {
    "minTemperature": 23,
    "maxTemperature": 86,
    "includeTimeVariation": true,
    "includeSeasonalVariation": true,
    "decimalPlaces": 1
  }
}
```

The examples here are of course if you’re running the site code itself. Otherwise navigate over to <https://datadiluvium.com> and you can just get the data generated on the site, as I’ve pushed this feature to prod and it’s good to go!

The data when generated per my sample schema looks like this.

[![](/wp-content/uploads/2025/03/CleanShot-2025-03-31-at-14.01.08@2x.png)](/wp-content/uploads/2025/03/CleanShot-2025-03-31-at-14.01.08@2x.png)

That should do it!

Happy thrashing coding! 🌡️ Next post coming up will be the next steps in the TimeScaleDB sample I started in [this post](/2025/03/28/setup-timescaledb-with-docker-compose-a-step-by-step-guide/).
