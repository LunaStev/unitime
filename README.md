# Universal Time (UT)

**Universal Time (UT)** is a custom timekeeping system designed to replace Earth-based calendars and clocks with a consistent, universal framework.
Instead of relying on Earth's rotation and orbit, UT uses a unit-based structure defined by absolute constants.

## 🔹 Core Concept
- Epoch:
`1970-01-01 00:00:00 UTC` -> defined as UT 0000-01-01 00:00:00 (This ensures compatibility with Unix time.)

- Base Unit:
`1 sencond = 100,000,000 units`

- Time Structure:
  - 1 second = 100,000,000 units
  - 1 minute = 100 seconds
  - 1 hour = 100 minutes
  - 1 day = 10 hours
  - 1 month = 50 days
  - 1 year = 500 days (10 months x 50 days)
 
---

## 🔹 Calendar Layout
- Year: 500 days
- Month: 500 days
- Day: 10 hours
- Hour: 100 minutes
- Minute: 100 seconds
- Second: 100,000,000 units

This structure creates a uniform and highly scalable calendar system, completely independent of Earth's astronomy.

---

## 🔹 Example Conversion
Given `2025-09-10 04:11:11 UTC`, the Universal Time is:

```text
UT: 0035-02-25 07:74:71 + 4149795 units
```

Which corresponds to:
- Year: 35
- Month: 2
- Day: 25
- Hour: 7
- Minute: 74
- Scond: 71
- Units: 4,149,795

---

## 🔹 Output Example (Python Implementation)

```text
Current UTC: 2025-09-10 04:30:07.211Z
Universal Time (custom): 0035-02-25 07:86:07 + 21163511 units
Total units since epoch (1970-01-01Z): 175,747,860,721,163,520 units

Constants:
- 1 second = 100,000,000 units
- 1 minute = 100 seconds = 100 s
- 1 hour = 100 minutes = 10,000 s
- 1 day = 10 hours = 100,000 s
- 1 month = 50 days = 5,000,000 s
- 1 year = 500 days = 50,000,000 s

Current Universal Time: 35 Year 2 Month 25 Day 7 Hour 86 Minute 7 Second
```

---

## 🔹 Why Universal Time?
- Independent from Earth's orbit and rotation
- Scales to any application: operating systems, programming languages, simulations, games, or scientific models
- Simple hierchical structure (base-10 system)
- Provides a deterministic timeline for all universes
