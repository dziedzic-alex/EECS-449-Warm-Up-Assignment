from __future__ import annotations
from jaclang.plugin.feature import JacFeature as _Jac
from jaclang.plugin.builtin import *
from dataclasses import dataclass as __jac_dataclass__

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class interact(_Jac.Walker):

    def return_message(self, _jac_here_: _Jac.RootType) -> None:
        _Jac.report({'response': 'Hello, world!'})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class interact_with_body(_Jac.Walker):
    name: str

    def return_message(self, _jac_here_: _Jac.RootType) -> None:
        _Jac.report({'response': 'Hello, ' + self.name + '!'})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('return_message', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class add_two_numbers(_Jac.Walker):
    number1: float
    number2: float

    def return_message(self, _jac_here_: _Jac.RootType) -> None:
        _Jac.report({'response': self.number1 + self.number2})

@_Jac.make_walker(on_entry=[_Jac.DSFunc('is_palindrome', _Jac.RootType)], on_exit=[])
@__jac_dataclass__(eq=False)
class strings(_Jac.Walker):
    string: str

    def is_palindrome(self, _jac_here_: _Jac.RootType) -> None:
        l = 0
        r = len(self.string) - 1
        response = f'{self.string} is a palindrom'
        while l < r:
            if self.string[l] != self.string[r]:
                response = f'{self.string} is not a palindrom'
                break
            l += 1
            r -= 1
        _Jac.report({'response': response})