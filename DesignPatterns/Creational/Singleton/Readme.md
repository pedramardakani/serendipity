# Singleton

Reasons to implement:
- Ensure that a class has just a single instance.
- Provide a global access point to that instance.


**Use the Singleton pattern when you need stricter control over global variables.**

Unlike global variables, the Singleton pattern guarantees that there’s just one instance of a class. Nothing, except for the Singleton class itself, can replace the cached instance.

Note that you can always adjust this limitation and allow creating any number of Singleton instances. The only piece of code that needs changing is the body of the getInstance method.

---
Example: **Database instance**

### **How to Implement**

- Add a private static field to the class for storing the singleton instance.

- Declare a public static creation method for getting the singleton instance.

- Implement “lazy initialization” inside the static method. It should create a new object on its first call and put it into the static field. The method should always return that instance on all subsequent calls.

- Make the constructor of the class private. The static method of the class will still be able to call the constructor, but not the other objects.

- Go over the client code and replace all direct calls to the singleton’s constructor with calls to its static creation method.


Reference: 

https://refactoring.guru/design-patterns/singleton