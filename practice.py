import pinject


'''
Basic dependency injection

https://github.com/google/pinject#basic-dependency-injection
'''


class OuterClass(object):
    def __init__(self, inner_class):
        self.inner_class = inner_class


class InnerClass(object):
    def __init__(self):
        self.forty_two = 42


obj_graph = pinject.new_object_graph()
outer_class = obj_graph.provide(OuterClass)
print(outer_class.inner_class.forty_two)  # 42


'''
Finding classes and providers for implicit bindings

https://github.com/google/pinject#finding-classes-and-providers-for-implicit-bindings
'''


class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo


class Foo(object):
    def __init__(self):
        self.forty_two = 42


obj_graph = pinject.new_object_graph(modules=None, classes=[SomeClass])
# obj_graph.provide(SomeClass)  # would raise a NothingInjectableForArgError
obj_graph = pinject.new_object_graph(modules=None, classes=[SomeClass, Foo])
some_class = obj_graph.provide(SomeClass)
print(some_class.foo.forty_two)  # 42


obj_graph = pinject.new_object_graph(modules=None, classes=[Foo])
some_class = obj_graph.provide(SomeClass)
print(some_class.foo.forty_two)  # 42


'''
Binding spec configure() methods

https://github.com/google/pinject#binding-spec-configure-methods
'''


class SomeClass(object):
    def __init__(self, long_name):
        self.long_name = long_name


class SomeReallyLongClassName(object):
    def __init__(self):
        self.foo = 'foo'


class MyBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('long_name', to_class=SomeReallyLongClassName)


obj_graph = pinject.new_object_graph(binding_specs=[MyBindingSpec()])
some_class = obj_graph.provide(SomeClass)
print(some_class.long_name.foo)  # foo


class MainBindingSpec(pinject.BindingSpec):
    def configure(self, require):
        require('foo')


class RealFooBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_instance='a-real-foo')


class StubFooBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_instance='a-stub-foo')


class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo


obj_graph = pinject.new_object_graph(
    binding_specs=[MainBindingSpec(), RealFooBindingSpec()])
some_class = obj_graph.provide(SomeClass)
print(some_class.foo)  # a-real-foo
# pinject.new_object_graph(
#    binding_specs=[MainBindingSpec()])  # would raise a MissingRequiredBindingError


'''
Provider methods

https://github.com/google/pinject#provider-methods
'''


class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo


class SomeBindingSpec(pinject.BindingSpec):
    def provide_foo(self):
        return 'some-complex-foo'


obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
some_class = obj_graph.provide(SomeClass)
print(some_class.foo)  # some-complex-foo


'''
Safety

https://github.com/google/pinject#safety
'''


class ExplicitlyBoundClass(object):
    @pinject.inject()
    def __init__(self, foo):
        self.foo = foo


class ImplicitlyBoundClass(object):
    def __init__(self, foo):
        self.foo = foo


class SomeBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_instance='explicit-foo')


obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()],
                                     only_use_explicit_bindings=True)
# obj_graph.provide(ImplicitlyBoundClass)  # would raise a NonExplicitlyBoundClassError
some_class = obj_graph.provide(ExplicitlyBoundClass)
print(some_class.foo)  # explicit-foo


'''
Annotations

https://github.com/google/pinject#annotations
'''


class SomeClass(object):
    @pinject.annotate_arg('foo', 'annot')
    def __init__(self, foo):
        self.foo = foo


class SomeBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', annotated_with='annot', to_instance='foo-with-annot')
        bind('foo', annotated_with=12345, to_instance='12345-foo')


obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
some_class = obj_graph.provide(SomeClass)
print(some_class.foo)  # foo-with-annot


'''
Scopes

https://github.com/google/pinject#scopes
'''


class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo


class SomeBindingSpec(pinject.BindingSpec):
    def provide_foo(self):
        return object()


obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
some_class_1 = obj_graph.provide(SomeClass)
some_class_2 = obj_graph.provide(SomeClass)
print(some_class_1.foo is some_class_2.foo)  # True


class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo


class SomeBindingSpec(pinject.BindingSpec):
    @pinject.provides(in_scope=pinject.PROTOTYPE)
    def provide_foo(self):
        return object()


obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
some_class_1 = obj_graph.provide(SomeClass)
some_class_2 = obj_graph.provide(SomeClass)
print(some_class_1.foo is some_class_2.foo)  # False


class SomeClass(object):
    def __init__(self, foo):
        self.foo = foo


class OtherClass(object):
    def __init__(self, foo):
        self.foo = foo


class FooFoo(object):
    def __init__(self):
        self.bar = 'bar'


class SomeBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('foo', to_class=FooFoo, in_scope=pinject.SINGLETON)


obj_graph = pinject.new_object_graph(binding_specs=[SomeBindingSpec()])
some_class_1 = obj_graph.provide(SomeClass)
some_class_2 = obj_graph.provide(SomeClass)
other_class_1 = obj_graph.provide(OtherClass)
print(some_class_1.foo is some_class_2.foo)  # True
print(some_class_1.foo is other_class_1.foo)  # True
print(some_class_1.foo.bar)  # bar
