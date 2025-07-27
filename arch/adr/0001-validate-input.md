# 0001. Validate Input in Every Service

## Status

Proposed

## Context

Errors in input received by a service can cause bugs that manifest in various parts of its code, and may even propagate to other components in the system workflow.

## Decision

It is proposed to perform all possible input validations in every service of the system.

## Consequences

This decision helps isolate errors originating from user input or preceding components from the logic of a given service. As a result, debugging is simplified and data corruption is detected at an early stage.