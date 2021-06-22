# Javascript 

## Intoduction

[need some text]

## Tips and Tricks

!!! info "Don't use eval"
    Just don't.

Don't reassign function parameters

```js linenums="1"
function foo(bar) {
  bar = 1; // no!
}
```

Don't add or remove properties from objects.

```js linenums="1"
delete obj.x; // no!
```

```js linenums="1"
const obj = { y: 1 };
obj.x = 2; // no!
```

```js linenums="1"
class X {
  constructor() {
    this.y = 1;
  }

  method() {
    this.x = 2; // no!
  }
}
```

Use specific methods over generic loops where possible

```js linenums="1"
// no!
for (const item of array) {
  // ...
}

// yes!
array.forEach((item) => {
});
```

Don't create arrays with holes.

```js linenums="1"
// no!
const array = new Array(5).fill(0);
// yes!
let array = Array.from({ length: 5 }, () => 0);
```

Use strict equality

```js linenums="1"
// no!
a == b;
// yes!
a === b;
```