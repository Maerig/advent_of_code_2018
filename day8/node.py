class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def metadata_sum(self):
        return sum(self.metadata) + sum(
            child.metadata_sum()
            for child in self.children
        )

    def value(self):
        if not self.children:
            return sum(self.metadata)
        return sum(
            self.children[i - 1].value()
            for i in self.metadata
            if 0 < i <= len(self.children)
        )
