# Interface Design for Testability

Good interfaces make testing natural:

1. **Accept dependencies, don't create them**
2. **Return results, avoid producing side effects**
3. **Small surface area**
   - Fewer methods = fewer tests needed
   - Fewer params = simpler test setup
