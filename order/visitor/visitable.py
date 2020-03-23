from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING

from django.db.models import Model

if TYPE_CHECKING:
    from order.visitor.abstractvisitor import AbstractVisitor


class Visitable(Model):
    @abstractmethod
    def accept(self, visitor: AbstractVisitor):
        raise NotImplementedError

    class Meta:
        abstract = True
