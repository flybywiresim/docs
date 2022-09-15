# A32NX Systems Guidelines

This page is pulled externally from the A32NX repository.

Please read through the guidelines described in this document. These guidelines are based upon pull request review comments. When reviewing pull requests, feel free to extend 
this document rather than repeating the same comment on pull requests over and over again.

# General

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '# General') }}

## Units of measurement

We use the [`uom`](https://crates.io/crates/uom) crate to provide us with units of measurement types. Whenever possible use these types instead of numeric types.

**Rationale:** Reduces the risk of computational errors such as mistaking a value in pounds with a value in kilograms. Using these types also reduces the risk of passing function arguments in the wrong order.

When reading and writing `uom` types using `SimulatorReader` and `SimulatorWriter`, don't convert to a specific unit unless the unit deviates from the default unit defined in [`systems/src/simulation/mod.rs`](https://github.com/flybywiresim/a32nx/blob/master/src/systems/systems/src/simulation/mod.rs).

**Rationale**: This leads to shorter and easier to read code. The default unit works for the majority of cases.

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## HashMap and HashSet') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## Testing') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## `assert_eq!` and `assert_ne!`') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## Law of Demeter') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## Explicit `match` pattern declaration') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## Implicit Enum variant value') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## Prefer monomorphisation') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## Passing data around') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## Do not re-read SimVars written by Rust code') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## Avoid repeating trait `where` clauses') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## Avoid copying default trait function implementations') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## Avoid `extern crate` usage') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## Limit item visibility') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## Avoid dependencies between child modules') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '## Single assignment for simple `if else`') }}

{{ external_markdown('https://raw.githubusercontent.com/flybywiresim/a32nx/master/src/systems/guidelines.md', '# Style') }}