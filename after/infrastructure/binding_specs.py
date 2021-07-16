from infrastructure.fake_db import FakeDB

import pinject


class RepositoryBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('db', to_instance=FakeDB(), in_scope=pinject.SINGLETON)
