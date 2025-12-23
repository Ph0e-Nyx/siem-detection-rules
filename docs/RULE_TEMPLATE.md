# Detection Rule Template

Use this template when creating new detection rules. Ensure all fields are filled out accurately to maintain quality and consistency.

## Rule Metadata

| Field        | Value                      |
| :---         | :---                       |
| **Title**    | [Descriptive Title]        |
| **ID**       | [UUID]                     |
| **Author**   | [Your Name/Handle]         |
| **Date**     | [YYYY-MM-DD]               |
| **Status**   | [experimental/test/stable] |
| **Severity** | [low/medium/high/critical] |

## Description

[Provide a detailed description of what this rule detects. Explain the attack technique and why it is malicious.]

## MITRE ATT&CK Mapping

- **Tactic**: [Tactic Name] (e.g., Execution)
- **Technique**: [Technique Name] (ID) (e.g., PowerShell - T1059.001)
- **Sub-technique**: [Sub-technique Name] (ID)

## Data Sources

- [Log Source 1] (e.g., Windows Security Event Log)
- [Log Source 2] (e.g., Sysmon)

## Detection Logic

### Sigma (Universal)

```yaml
title: [Title]
id: [UUID]
status: [Status]
description: [Description]
author: [Author]
date: [Date]
references:
    - [Link 1]
tags:
    - attack.[tactic]
    - attack.[technique_id]
logsource:
    category: [Category]
    product: [Product]
detection:
    selection:
        [Field]: [Value]
    condition: selection
falsepositives:
    - [False Positive 1]
level: [Level]
```

### Splunk (SPL)

```splunk
[Insert SPL Query Here]
```

### Elastic (EQL)

```eql
[Insert EQL Query Here]
```

### QRadar (AQL)

```sql
[Insert AQL Query Here]
```

## False Positives

- [Scenario 1]: [Explanation]
- [Scenario 2]: [Explanation]

## Blind Spots

- [Limitation 1]: [Explanation]

## Response Guidance

1. [Step 1]: [Action]
2. [Step 2]: [Action]
3. [Step 3]: [Action]
