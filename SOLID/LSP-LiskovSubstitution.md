> If `S` is a subtype of `T`, then objects of type `T` in a program may be replaced with objects of type `S` without altering any of the desirable properties of that program.

<img src="https://user-images.githubusercontent.com/37804060/153056329-914cbbba-685b-452b-9dcf-4fcf6a4faabc.jpg"/>

:x: Before following LSP:

```typescript
class Tablet {
  readBook(): void {
    console.log("Enjoy reading!");
  }

  openBrowser(): void {
    console.log("Start searching ...");
  }
}

class KidsTablet extends Tablet {
  override openBrowser(): Error {
    throw Error("Kids haven't access to the browser!");
  }
}
```


:heavy_check_mark: After following LSP:

```typescript
class Tablet {
  readBook(): void {
    console.log("Enjoy reading!");
  }
}

class AdultsTablet extends Tablet {
  openBrowser(): void {
    console.log("Start searching ...");
  }
}
```