# Proxy

## intent
Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

# Problem

I'd rather give you a real world example instead of explaining the issue.

```
A credit card is a proxy for a bank account, which is a proxy for a bundle of cash. Both implement the same interface: they can be used for making a payment. A consumer feels great because there’s no need to carry loads of cash around. A shop owner is also happy since the income from a transaction gets added electronically to the shop’s bank account without the risk of losing the deposit or getting robbed on the way to the bank.
```
### In programming world
Why would you want to control access to an object? Here is an example: you have a massive object that consumes a vast amount of system resources. You need it from time to time, but not always.

You could implement lazy initialization: create this object only when it’s actually needed. All of the object’s clients would need to execute some deferred initialization code. Unfortunately, this would probably cause a lot of code duplication.


In an ideal world, we’d want to put this code directly into our object’s class, but that isn’t always possible. For instance, the class may be part of a closed 3rd-party library. Pay attention to the following example

```
A library provides us with the video downloading class for Youtube. However, it’s very inefficient. If the client application requests the same video multiple times, the library just downloads it over and over, instead of caching and reusing the first downloaded file.

The proxy class implements the same interface as the original downloader and delegates it all the work. However, it keeps track of the downloaded files and returns the cached result when the app requests the same video multiple times.
```

# Applicability

- There are dozens of ways to utilize the Proxy pattern. Let’s go over the most popular uses.

- Lazy initialization (virtual proxy). This is when you have a heavyweight service object that wastes system resources by being always up, even though you only need it from time to time.

- Instead of creating the object when the app launches, you can delay the object’s initialization to a time when it’s really needed.

- Access control (protection proxy). This is when you want only specific clients to be able to use the service object; for instance, when your objects are crucial parts of an operating system and clients are various launched applications (including malicious ones).

- The proxy can pass the request to the service object only if the client’s credentials match some criteria.

- Local execution of a remote service (remote proxy). This is when the service object is located on a remote server.

- In this case, the proxy passes the client request over the network, handling all of the nasty details of working with the network.

- Logging requests (logging proxy). This is when you want to keep a history of requests to the service object.

- The proxy can log each request before passing it to the service.

- Caching request results (caching proxy). This is when you need to cache results of client requests and manage the life cycle of this cache, especially if results are quite large.

- The proxy can implement caching for recurring requests that always yield the same results. The proxy may use the parameters of requests as the cache keys.

- Smart reference. This is when you need to be able to dismiss a heavyweight object once there are no clients that use it.

- The proxy can keep track of clients that obtained a reference to the service object or its results. From time to time, the proxy may go over the clients and check whether they are still active. If the client list gets empty, the proxy might dismiss the service object and free the underlying system resources.

- The proxy can also track whether the client had modified the service object. Then the unchanged objects may be reused by other clients.

# How to Implement

1) If there’s no pre-existing service interface, create one to make proxy and service objects interchangeable. Extracting the interface from the service class isn’t always possible, because you’d need to change all of the service’s clients to use that interface. Plan B is to make the proxy a subclass of the service class, and this way it’ll inherit the interface of the service.

2) Create the proxy class. It should have a field for storing a reference to the service. Usually, proxies create and manage the whole life cycle of their services. On rare occasions, a service is passed to the proxy via a constructor by the client.

3) Implement the proxy methods according to their purposes. In most cases, after doing some work, the proxy should delegate the work to the service object.

4) Consider introducing a creation method that decides whether the client gets a proxy or a real service. This can be a simple static method in the proxy class or a full-blown factory method.

5) Consider implementing lazy initialization for the service object.

# Pros and Cons

- You can control the service object without clients knowing about it.
- You can manage the lifecycle of the service object when clients don’t care about it.
- The proxy works even if the service object isn’t ready or is not available.
- Open/Closed Principle. You can introduce new proxies without changing the service or clients.

- The code may become more complicated since you need to introduce a lot of new classes.
- The response from the service might get delayed.

Reference:
https://refactoring.guru/design-patterns/proxy