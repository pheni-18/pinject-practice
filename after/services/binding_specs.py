from infrastructure.binding_specs import RepositoryBindingSpec
from infrastructure.user import UserRepository

import pinject


class ServiceBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind('user_repo', to_class=UserRepository, in_scope=pinject.SINGLETON)

    def dependencies(self):
        return [RepositoryBindingSpec()]
